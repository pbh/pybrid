#!/usr/bin/env python

"""
    pybrid.report
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    Base classes for reports (currently only pybrid.PybridReport).

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

import os

class PybridReport(object):
    """
    The base class for pybrid reports.

    A PybridReport mainly just outputs itself when write() is called
    with an output directory.

    If you give it a NAME, AUTHOR, or GROUPS, it will return those
    when requested via get_author, get_name, or get_groups.

    Lastly, if you implement a write_string() method, PybridReport
    will call your method and write out your returned string
    as {output_dir}/index.html.
    """
    
    def write(self, output_dir):
        """
        A report writes itself by implementing write() or write_string().

        This write method either calls write_string if that method is
        implemented, or raises NotImplementedError (because you should
        have overridden write()).
        """
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
        'Get the author of this report.'
        return self._get_metadata('AUTHOR')

    def get_name(self):
        'Get the name of this report.'
        return self._get_metadata('NAME')

    def get_groups(self):
        'Get the groups assigned to this report.'
        return self._get_metadata('GROUPS')
