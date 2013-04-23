from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import TEST_USER_ID, TEST_USER_NAME
from plone.app.testing import login, setRoles
from plone.app.testing import FunctionalTesting
from plone.app.testing import selenium_layers

from plone.testing import z2


class BootstrapTheme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plonetheme.bootstrap
        self.loadZCML(package=plonetheme.bootstrap)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_quickinstaller
        import ipdb;ipdb.set_trace()


BOOTSTRAPTHEME_FIXTURE = BootstrapTheme()

BOOTSTRAPTHEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BOOTSTRAPTHEME_FIXTURE,),
    name="BootstrapTheme:Functional")

BOOTSTRAPTHEME_ROBOT = FunctionalTesting(
    bases=(BOOTSTRAPTHEME_FIXTURE, z2.ZSERVER_FIXTURE),
    name='BOOTSTRAPTHEME_ROBOT')
