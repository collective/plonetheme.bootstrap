from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import FunctionalTesting

from plone.testing import z2
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.robotframework import RemoteLibraryLayer, AutoLogin
from plonetheme.bootstrap.tests.check_error_log import CheckErrorLog


class BootstrapTheme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plonetheme.bootstrap
        self.loadZCML(package=plonetheme.bootstrap)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_quickinstaller
        portal.portal_quickinstaller.installProduct('plonetheme.bootstrap')
        # A different install profile will be chosen for Plone>4.1

        portal.portal_css.cookResources()
        portal.portal_javascripts.cookResources()


BOOTSTRAPTHEME_FIXTURE = BootstrapTheme()

CHECK_ERROR_LOG_FIXTURE = RemoteLibraryLayer(
    bases=(PLONE_FIXTURE,),
    libraries=(CheckErrorLog, AutoLogin),
    name="CheckErrorLogRemoteLibrary:RobotRemote"
)

BOOTSTRAPTHEME_ROBOT = FunctionalTesting(
    bases=(CHECK_ERROR_LOG_FIXTURE, BOOTSTRAPTHEME_FIXTURE, z2.ZSERVER_FIXTURE),
    name='BootstrapTheme:Robot')
