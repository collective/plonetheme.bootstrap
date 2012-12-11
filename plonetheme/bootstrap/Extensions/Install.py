# -*- coding: utf-8 -*-

from Products.CMFPlone.utils import getToolByName


def uninstall(portal):
    """ Apply the correct so called uninstall-profile when uninstalling
        according to the installed Plone version
    """

    profile = 'profile-plonetheme.bootstrap:uninstall'
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(profile)
    return "Ran all uninstall steps."
