#!/usr/bin/env python

"""
    pybrid.loader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    ReportLoader lives here --- a class for loading reports dynamically.

    ReportLoader loads files in a particular directory that have *_report.py
    in their filename.

    Most of this module is derived from Michael Foord's unittest2, which I
    believe is in turn derived from the new unittest in the Python standard
    library.

    :copyright: (c) 2013 by Michael Foord and oDesk Corporation
    :license: BSD, see LICENSE for more details.
"""

import os
import re
import sys
from fnmatch import fnmatch
from os.path import relpath
import pybrid

VALID_MODULE_NAME = re.compile(r'[_a-z]\w*\.py$', re.IGNORECASE)

def _splitext_first(path):
    return os.path.splitext(path)[0]

class ReportLoader(object):
    """
    ReportLoader loads report.py files dynamically.

    It is derived from unittest2's TestLoader and has more advanced
    functionality as a result.
    """
    def __init__(self):
        self.reset()

    def reset(self):
        'Reset the top level dir, used for testing.'
        self._top_level_dir = None

    def loadReportsFromModule(self, module, use_load_tests=True):
        "Return all reports contained in the given module."
        reports = []

        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, pybrid.PybridReport):
                reports.append(obj)

        return reports

    def discover(self, start_dir, pattern='*report.py', top_level_dir=None):
        """
        Find and return all report modules from the specified start
        directory, recursing into subdirectories to find them and return all
        tests found within them. Only report files that match the pattern will
        be loaded. (Using shell style pattern matching.)

        All report modules must be importable from the top level of the project.
        If the report directory is not the top level directory then the top
        level directory must be specified separately.
        """
        set_implicit_top = False
        if top_level_dir is None and self._top_level_dir is not None:
            # make top_level_dir optional if called from load_tests in a package
            top_level_dir = self._top_level_dir
        elif top_level_dir is None:
            set_implicit_top = True
            top_level_dir = start_dir

        top_level_dir = os.path.abspath(top_level_dir)

        if not top_level_dir in sys.path:
            # all test modules must be importable from the top level directory
            sys.path.insert(0, top_level_dir)
        self._top_level_dir = top_level_dir

        is_not_importable = False
        if os.path.isdir(os.path.abspath(start_dir)):
            start_dir = os.path.abspath(start_dir)
            if start_dir != top_level_dir:
                is_not_importable = not os.path.isfile(os.path.join(start_dir, '__init__.py'))
        else:
            raise ImportError('Start directory is not importable: %r' % start_dir)

        reports = list(self._find_reports(start_dir, pattern))
        return reports

    def _get_name_from_path(self, path):
        path = _splitext_first(os.path.normpath(path))

        _relpath = relpath(path, self._top_level_dir)

        assert not os.path.isabs(_relpath), "Path must be within the project"
        assert not _relpath.startswith('..'), "Path must be within the project"

        name = _relpath.replace(os.path.sep, '.')
        return name

    def _get_module_from_name(self, name):
        __import__(name)
        return sys.modules[name]

    def _match_path(self, path, full_path, pattern):
        # override this method to use alternative matching strategy
        return fnmatch(path, pattern)

    def _find_reports(self, start_dir, pattern):
        """Used by discovery. Yields reports it loads."""
        paths = os.listdir(start_dir)

        for path in paths:
            full_path = os.path.join(start_dir, path)
            if os.path.isfile(full_path):
                if not VALID_MODULE_NAME.match(path):
                    # valid Python identifiers only
                    continue
                if not self._match_path(path, full_path, pattern):
                    continue
                # if the report file matches, load it
                name = self._get_name_from_path(full_path)
                try:
                    module = self._get_module_from_name(name)
                except:
                    raise
                    # raise RuntimeError('Failed to load report %s.' % name)
                else:
                    mod_file = os.path.abspath(getattr(module, '__file__', full_path))
                    realpath = _splitext_first(mod_file)
                    fullpath_noext = _splitext_first(full_path)
                    if realpath.lower() != fullpath_noext.lower():
                        module_dir = os.path.dirname(realpath)
                        mod_name = _splitext_first(os.path.basename(full_path))
                        expected_dir = os.path.dirname(full_path)
                        msg = ("%r module incorrectly imported from %r. Expected %r. "
                               "Is this module globally installed?")
                        raise ImportError(msg % (mod_name, module_dir, expected_dir))

                    for r in self.loadReportsFromModule(module):
                        yield r
            elif os.path.isdir(full_path):
                if not os.path.isfile(os.path.join(full_path, '__init__.py')):
                    continue

                # recurse into the package
                for report in self._find_reports(full_path, pattern):
                    yield report

defaultReportLoader = ReportLoader()
