from Products.CMFCore.utils import getToolByName

import logging

PROFILE_ID = 'profile-plonetheme.bootstrap:default'


def common(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('plonetheme.bootstrap')

    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE_ID)

    logger.info("Migrated from previous version")


def remove_old_2_css(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('plonetheme.bootstrap')

    csstool = getToolByName(context, 'portal_css')
    csstool.unregisterResource('++resource++collective.js.bootstrap/css/bootstrap-responsive.min.css')

    logger.info("Migrated from previous version")
