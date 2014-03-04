from Acquisition import aq_inner
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName

class BootstrapDropdownMenu(ViewletBase):

    def navtree(self):
        context = aq_inner(self.context)
        view = getMultiAdapter((context, self.request),
                               name='sitemap_builder_view')
        data = view.siteMap()
        bottomLevel = 5
        portal_tabs_view = getMultiAdapter((context, self.request),
                                           name='portal_tabs_view')
        portal_tabs = portal_tabs_view.topLevelTabs()
        selected_tabs = self.selectedTabs(portal_tabs=portal_tabs)
        selected_portal_tab = selected_tabs['portal']
        # XXX: The recursion should probably be done in python code

        return context.homepage_sections(
            children=data.get('children', []),
            level=1,
            bottomLevel=bottomLevel,
            selected_portal_tab=selected_portal_tab,
        )


    def selectedTabs(self, default_tab='index_html', portal_tabs=()):
        plone_url = getToolByName(self.context, 'portal_url')()
        plone_url_len = len(plone_url)
        request = self.request
        valid_actions = []

        url = request['URL']
        path = url[plone_url_len:]

        for action in portal_tabs:
            if not action['url'].startswith(plone_url):
                # In this case the action url is an external link. Then, we
                # avoid issues (bad portal_tab selection) continuing with next
                # action.
                continue
            action_path = action['url'][plone_url_len:]
            if not action_path.startswith('/'):
                action_path = '/' + action_path
            if path.startswith(action_path + '/') or path == action_path:
                # Make a list of the action ids, along with the path length
                # for choosing the longest (most relevant) path.
                valid_actions.append((len(action_path), action['id']))

        # Sort by path length, the longest matching path wins
        valid_actions.sort()
        if valid_actions:
            return {'portal' : valid_actions[-1][1]}

        return {'portal' : default_tab}