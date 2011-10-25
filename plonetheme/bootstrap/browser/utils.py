from zope.component import getMultiAdapter
from zope.interface import implements
from Products.Five import BrowserView
from plone.app.layout.navigation.navtree import buildFolderTree
from Products.CMFPlone.browser.navtree import NavtreeQueryBuilder
from interfaces import IBootstrapUtils


class BootstrapUtils(BrowserView):
    implements(IBootstrapUtils)

    def navigation(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                        name='plone_portal_state')
        portal = portal_state.portal()
        queryBuilder = NavtreeQueryBuilder(portal)
        query = queryBuilder()
        query['path']['depth'] = 2

        tree = buildFolderTree(portal, obj=portal, query=query)['children']
#        for 
        return tree
