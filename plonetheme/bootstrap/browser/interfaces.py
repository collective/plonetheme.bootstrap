from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """


class IBootstrapUtils(Interface):
    def bootstrap():
        pass


class IBootstrapView(Interface):
    """ """

    def getColumnsClasses(view=None):
        """ A helper method to return the clases for the columns of the site
            it should return a dict with three elements:'one', 'two', 'content'
            Each of them should contain the classnames for the first (leftmost)
            second (rightmost) and middle column
        """

    def getViewportValues(view=None):
        """ Determine the value of the viewport meta-tag """