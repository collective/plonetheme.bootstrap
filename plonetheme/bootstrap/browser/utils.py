from zope.component import getMultiAdapter
from zope.interface import implements
from Products.Five import BrowserView
from plone.app.layout.navigation.navtree import buildFolderTree
from Products.CMFPlone.browser.navtree import NavtreeQueryBuilder
from interfaces import IBootstrapUtils, IBootstrapView


class BootstrapView(BrowserView):
    implements(IBootstrapView)

    def getViewportValues(self, view=None):
        """ Determine the value of the viewport meta-tag """
        return {'width': 'device-width',
                'initialscale': '0.6666',
                'maximumscale': '1.0',
                'minimumscale': '0.6666',
                }

    def getColumnsClasses(self, view=None):
        """ Determine whether a column should be shown. The left column is
            called plone.leftcolumn; the right column is called
            plone.rightcolumn.
        """

        plone_view = getMultiAdapter(
            (self.context, self.request), name=u'plone')
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state')

        sl = plone_view.have_portlets('plone.leftcolumn', view=view)
        sr = plone_view.have_portlets('plone.rightcolumn', view=view)

        isRTL = portal_state.is_rtl()

        # pre-fill dictionary
        columns = dict(one="", content="", two="")

        if not sl and not sr:
            # we don't have columns, thus conten takes the whole width
            columns['content'] = "span12"

        elif sl and sr:
            # In case we have both columns, content takes 50% of the whole
            # width and the rest 50% is spread between the columns
            columns['one'] = "span3"
            columns['content'] = "span6"
            columns['two'] = "span3"

        elif (sr and not sl) and not isRTL:
            # We have right column and we are NOT in RTL language
            columns['content'] = "span9"
            columns['two'] = "span3"

        elif (sl and not sr) and isRTL:
            # We have left column and we are in RTL language
            columns['one'] = "span3"
            columns['content'] = "span9"

        elif (sl and not sr) and not isRTL:
            # We have left column and we are in NOT RTL language
            columns['one'] = "span3"
            columns['content'] = "span9"

        # # append cell to each css-string
        # for key, value in columns.items():
        #     columns[key] = "cell " + value

        return columns
