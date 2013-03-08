#!/usr/bin/env python

"""
    hey_SKEL.SKEL
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    SKEL

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

import os

class PybridReport(object):

    def write(self, output_dir):
        # if the class has a write_string shortcut method,
        # use that to generate a report.
        if hasattr(self, 'write_string'):
            res_string = self.write_string(output_dir)

            f = file(os.path.join(output_dir, 'index.html'), 'w')
            f.write(res_string)
            f.close()
        else:
            # otherwise, this method should be overridden
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
