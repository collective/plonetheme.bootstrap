from zope.interface import Interface, implements
from zope.component import getMultiAdapter

from Products.Five.browser import BrowserView
from Acquisition import aq_inner, aq_parent

from plone.memoize.view import memoize
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.navigation.root import getNavigationRootObject

class INavigationRootView(Interface):
    def is_navigation_root_or_default_page():
        """ return whether the current object is the navigation
            root element or the default page of a navigation root
            item. This is similar to @@ploneview/isPortalOrPortalDefaultPage method
        """

    def navigation_root_title():
        """ return the title of the (upwards) nearest INavigationRoot
            enabled item
        """

class NavigationRoot(BrowserView):
    implements(INavigationRootView)

    @memoize
    def is_navigation_root_or_default_page(self):
        context = aq_inner(self.context)
        context_state = getMultiAdapter(
            (context, self.request), name=u'plone_context_state')
        if context_state.is_default_page():
            return INavigationRoot.providedBy(aq_parent(context))
        else:
            return INavigationRoot.providedBy(context)

    @memoize
    def navigation_root_title(self):
        context = aq_inner(self.context)
        portal = getMultiAdapter((context, self.request), name=u'plone_portal_state').portal
        navigation_root = getNavigationRootObject(context, portal)
        return navigation_root.Title()

    @memoize
    def navigation_root_url(self):
        context = aq_inner(self.context)
        portal = getMultiAdapter((context, self.request), name=u'plone_portal_state').portal
        navigation_root = getNavigationRootObject(context, portal)
        return navigation_root.absolute_url()
