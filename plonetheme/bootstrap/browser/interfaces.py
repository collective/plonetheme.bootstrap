from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Bootstrap Theme" theme, this interface must be its layer
       (in bootstrap/viewlets/configure.zcml).
    """


class IBootstrapUtils(Interface):
    def bootstrap():
        pass
