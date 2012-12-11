from Products.CMFCore.utils import getToolByName
from Persistence import PersistentMapping

import logging

PROFILE_ID = 'profile-plonetheme.bootstrap:default'


def upgrade_to_1001(context, logger=None):
    """Method to convert float Price fields to string.

    When called from the import_various method, 'context' is
    the plone site and 'logger' is the portal_setup logger.

    But this method will be used as upgrade step, in which case 'context'
    will be portal_setup and 'logger' will be None.

    """
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('plonetheme.bootstrap')

    # Run the catalog.xml step as that may have defined new metadata
    # columns.  We could instead add <depends name="catalog"/> to
    # the registration of our import step in zcml, but doing it in
    # code makes this method usable as upgrade step as well.
    # Remove these lines when you have no catalog.xml file.
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'browserlayer')
    setup.runImportStepFromProfile(PROFILE_ID, 'cssregistry')

    # Remove registered scripts
    portal_js = getToolByName(context, 'portal_javascripts')
    portal_js.unregisterResource('bootstrap-integration.js')
    portal_js.unregisterResource('bootstrap-dropdown.js')
    portal_js.unregisterResource('bootstrap-alerts.js')
    # install new provided JS files
    setup.runImportStepFromProfile(PROFILE_ID, 'jsregistry')
    # Remove previously registered skin folders
    portal_skins = getToolByName(context, 'portal_skins')
    selections = PersistentMapping()
    OLD_LAYERS = ['plonetheme_bootstrap_custom_images',
                  'plonetheme_bootstrap_custom_templates']
    for skin, layers in portal_skins.selections.items():
        if skin != 'Bootstrap Theme':
            new_layers = ','.join([l for l in layers.split(',') \
                    if l not in OLD_LAYERS])
            selections[skin] = new_layers

    del portal_skins.selections['Bootstrap Theme']

    setup.runImportStepFromProfile(PROFILE_ID, 'skins')


    logger.info("Migrated from plonetheme.bootstrap 1.0a1 version")