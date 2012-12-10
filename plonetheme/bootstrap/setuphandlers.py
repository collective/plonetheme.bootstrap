from Products.CMFCore.ActionInformation import Action
from Products.CMFCore.utils import getToolByName


def setupVarious(context):
    """ Only in plonetheme.sunburst profile """

    if context.readDataFile('plonetheme.bootstrap_various.txt') is None:
        return

    # Do what plonetheme.sunburst does
    # Copy the plone_setup action to the user category
    atool = getToolByName(context.getSite(), 'portal_actions')
    user_category = atool.user
    if 'plone_setup' in user_category:
        return

    state = dict(atool.site_actions.plone_setup.propertyItems())
    state['visible'] = True
    new_action = Action('plone_setup', **state)
    user_category['plone_setup'] = new_action

    position = user_category.getObjectPosition('preferences') + 1
    user_category.moveObjectToPosition('plone_setup', position)
