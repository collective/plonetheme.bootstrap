# -*- coding: utf-8 -*-
import os

from plone.app.testing.interfaces import PLONE_SITE_ID
from plone.testing import z2


PORT = os.environ.get('ZSERVER_PORT', z2.ZServer.port)
PORT = os.environ.get('PLONE_TESTING_PORT', PORT)
ZSERVER_PORT = PORT
SELENIUM_IMPLICIT_WAIT = os.environ.get('SELENIUM_IMPLICIT_WAIT', '0.1s')
SELENIUM_TIMEOUT = os.environ.get('SELENIUM_IMPLICIT_WAIT', '20s')

ZOPE_HOST = os.environ.get('ZOPE_HOST', "localhost")
ZOPE_URL = os.environ.get('ZOPE_URL', "http://%s:%s" % (ZOPE_HOST, PORT))
PLONE_SITE_ID = os.environ.get('PLONE_SITE_ID', PLONE_SITE_ID)
PLONE_URL = os.environ.get('PLONE_URL', "%s/%s" % (ZOPE_URL, PLONE_SITE_ID))
BROWSER = os.environ.get('BROWSER', "Firefox")
REMOTE_URL = os.environ.get('REMOTE_URL', "")
DESIRED_CAPABILITIES = os.environ.get('DESIRED_CAPABILITIES', "")

TEST_FOLDER = os.environ.get('TEST_FOLDER', "%s/robot-test-folder" % PLONE_URL)

# Imports to fill in variables
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import TEST_USER_PASSWORD
from plone.app.testing import TEST_USER_ID
