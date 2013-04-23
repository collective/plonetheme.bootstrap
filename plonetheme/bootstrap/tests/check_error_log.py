# -*- coding: utf-8 -*-
from plone.app.robotframework.remote import RemoteLibrary


class CheckErrorLog(RemoteLibrary):

    def error_log_is_empty(self, *args):
        """
        Ensure the site error_log has no entries in it
        """
        entries = self.aq_parent.aq_base.error_log.getLogEntries()
        if entries:
            error = u"Expected zero entries in site error log, found %i instead: %s"
            raise Exception(error % len(entries), repr(entries))
