#!/usr/bin/env python

"""
    hey_SKEL.SKEL
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    SKEL

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""


class AprilCopyHook(object):
    def __init__(self, april_asset_dir_name=None):
        self.april_asset_dir_name = april_asset_dir_name

    def __call__(self, runner):
        import hey_april

        hey_april.copy_assets(
            runner.get_output_dir(),
            self.april_asset_dir_name)
