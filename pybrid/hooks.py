#!/usr/bin/env python

"""
    hey_SKEL.SKEL
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    SKEL

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

import os

class AprilCopyHook(object):
    DEFAULT_ASSET_DIR_NAME = 'april_assets'

    def __init__(self, april_asset_dir_name=None):
        import hey_april
        if april_asset_dir_name is None:
            april_asset_dir_name = self.DEFAULT_ASSET_DIR_NAME

        self.april_asset_dir_name = april_asset_dir_name
        hey_april.set_default_asset_prefix(
            os.path.join('..', april_asset_dir_name))

    def __call__(self, runner):
        import hey_april

        hey_april.copy_assets(
            runner.get_output_dir(),
            self.april_asset_dir_name)


class IndexHtmlGeneratorHook(object):
    INDEX_HTML_HEADER = """
<html>
<head><title>Pybrid Index</title></head>
<body>
"""
    INDEX_HTML_FOOTER = """
</body>
</html>
"""

    def __init__(self):
        pass

    def __call__(self, runner):
        rel_paths = [
            os.path.relpath(
                output_dir,
                runner.get_output_dir())
                for output_dir in runner.get_report_output_dirs()]

        f = file(os.path.join(runner.get_output_dir(), 'index.html'), 'w')

        f.write(self.INDEX_HTML_HEADER)
        for rel_path in rel_paths:
            f.write('<a href="%s/index.html">%s</a><br/>' % (rel_path, rel_path))
        f.write(self.INDEX_HTML_FOOTER)
        f.close()


class ExecuteCommandOnIndexHook(object):
    def __init__(self, cmd):
        self.cmd = cmd

    def __call__(self, runner):
        os.system(
            '%s %s' % (self.cmd, 
                       os.path.join(runner.get_output_dir(),
                                    'index.html'))
            )
