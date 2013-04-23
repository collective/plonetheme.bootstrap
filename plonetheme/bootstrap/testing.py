from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import TEST_USER_ID, TEST_USER_NAME
from plone.app.testing import login, setRoles
from plone.app.testing import FunctionalTesting
from plone.app.testing import selenium_layers

from plone.testing import z2
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE


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

BOOTSTRAPTHEME_ROBOT = FunctionalTesting(
    bases=(BOOTSTRAPTHEME_FIXTURE, z2.ZSERVER_FIXTURE),
    name='BootstrapTheme:Robot')

BOOTSTRAPTHEME_ROBOT_LOGGED_IN = FunctionalTesting(
    bases=(AUTOLOGIN_LIBRARY_FIXTURE, BOOTSTRAPTHEME_FIXTURE, z2.ZSERVER_FIXTURE),
    name='BootstrapTheme:Robot')