#!/usr/bin/env python

"""
    hey_SKEL.SKEL
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    SKEL

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

class PybridReport(object):

    def write(self, output_dir):
        'Implement this in your reports.'
        raise NotImplementedError

    def _get_metadata(self, name):
        if hasattr(self, name):
            return getattr(self, name)
        return None

    def get_author(self):
        return self._get_metadata('AUTHOR')

    def get_name(self):
        return self._get_metadata('NAME')

    def get_groups(self):
        return self._get_metadata('GROUPS')
