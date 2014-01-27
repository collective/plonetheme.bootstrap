from Acquisition import aq_inner
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter


class BootstrapDropdownMenu(ViewletBase):

    def navtree(self):
        context = aq_inner(self.context)
        view = getMultiAdapter((context, self.request),
                               name='sitemap_builder_view')
        data = view.siteMap()
        bottomLevel = 5
        # XXX: The recursion should probably be done in python code
        return context.homepage_sections(
            children=data.get('children', []),
            level=1,
            bottomLevel=bottomLevel
        )
