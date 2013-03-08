#!/usr/bin/env python

"""
    hey_SKEL.SKEL
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    SKEL

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

import pybrid

def run(top_level_dir, *args, **kwargs):
    found_reports = pybrid.defaultReportLoader.discover(top_level_dir)
    r = pybrid.ReportRunner(found_reports, *args, **kwargs)
    r.run()

    return r

