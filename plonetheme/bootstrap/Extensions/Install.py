# -*- coding: utf-8 -*-

from Products.CMFPlone.utils import getToolByName


def isPlone42(portal):
    migration_tool = getToolByName(portal, 'portal_migration')
    core_versions = migration_tool.coreVersions()
    plone = core_versions.get('Plone', '')
    if plone:
        versions = plone.split('.')
        return versions[0] == '4' and versions[1] == '2'

    return False


def isPlone41(portal):
    migration_tool = getToolByName(portal, 'portal_migration')
    core_versions = migration_tool.coreVersions()
    plone = core_versions.get('Plone', '')
    if plone:
        versions = plone.split('.')
        return versions[0] == '4' and versions[1] == '1'

    return False


def uninstall(portal):
    """ Apply the correct so called uninstall-profile when uninstalling
        according to the installed Plone version
    """

    if isPlone42(portal):
        profile = 'profile-plonetheme.bootstrap:uninstall'
    elif isPlone41(portal):
        profile = 'profile-plonetheme.bootstrap:uninstall-plone41'
    else:
        profile = ''

    if profile:
        setup_tool = getToolByName(portal, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile(profile)
        return "Ran all uninstall steps."

    else:
        return "Nothing to uninstall"
