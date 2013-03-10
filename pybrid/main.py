#!/usr/bin/env python

"""
    pybrid.main
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    Top level pybrid methods for initiating runs.

    Pybrid is usually run in one of two ways.  If you are running pybrid
    automatically, pybrid.run() is a simple interface to generating
    reports.  If you are running pybrid from the command line,
    pybrid.main() will parse command line options and then run the
    appropriate pybrid functions.

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

import pybrid
import optparse
import sys
import datetime
import os

def run(top_level_dir, *args, **kwargs):
    'Discover reports in top_level_dir and then run ReportRunner.'
    found_reports = pybrid.defaultReportLoader.discover(top_level_dir)
    r = pybrid.ReportRunner(found_reports, *args, **kwargs)
    r.run()

    return r

def main(top_level_dir, *args, **kwargs):
    'Parse command line options, discover, and run ReportRunner.'
    parser = optparse.OptionParser()

    # actions:
    parser.add_option('-r', '--run',
                      action="store_true", dest="run", default=False,
                      help="generate reports")
    parser.add_option('-l', '--list',
                      action="store_true", dest="list", default=False,
                      help="list reports")

    # params:
    parser.add_option("-d", "--output_dir", dest="output_dir",
                      help="write reports to DIR", metavar="DIR")
    parser.add_option("-e", "--executable",
                      help="execute command CMD with report HTML index",
                      metavar="CMD", dest='executable')
    parser.add_option('--reports-in-timestamp-dir',
                      action="store_true", dest="timestamp_dir", default=False,
                      help="put reports in timestamp rather than base dir")

    # filters
    parser.add_option("-g", "--group",
                      action="append", dest="include_groups",
                      help="generate reports in this GROUP (may be repeated)")
    parser.add_option("-a", "--author",
                      help="generate reports by this AUTHOR",
                      metavar="AUTHOR", dest='author')
    parser.add_option("-n", "--name",
                      help="generate report with this NAME",
                      metavar="NAME", dest='name')

    (options, args) = parser.parse_args()

    if (not (options.run or options.list) or
        (options.run and options.list)):
        print >>sys.stderr, 'Must either list or run reports.'
        parser.print_help()
        sys.exit(1)

    if options.run and not options.output_dir:
        print >>sys.stderr, 'Output dir is required for running reports.'
        parser.print_help()
        sys.exit(1)
        
    if options.list:
        found_reports = pybrid.defaultReportLoader.discover(top_level_dir)
        reports = []
        for found_report in found_reports:
            inst = found_report()
            reports.append((inst.get_name(),
                            inst.get_author(),
                            inst.get_groups(),
                            str(found_report)))

        for name, author, groups, cls_s in list(sorted(reports)):
            print name, author, groups, cls_s

    if options.run:
        if not kwargs.has_key('pre_hooks'):
            kwargs['pre_hooks'] = []

        if not kwargs.has_key('report_filters'):
            kwargs['report_filters'] = []

        if not kwargs.has_key('post_hooks'):
            kwargs['post_hooks'] = []

        if options.include_groups:
            kwargs['report_filters'].append(
                pybrid.filters.GroupFilter(options.include_groups)
                )

        if options.author:
            kwargs['report_filters'].append(
                pybrid.filters.AuthorFilter(options.author))

        if options.name:
            kwargs['report_filters'].append(
                pybrid.filters.NameFilter(options.name))

        if options.executable:
            kwargs['post_hooks'].append(
                pybrid.hooks.ExecuteCommandOnIndexHook(options.executable)
                )
        
        modified_output_dir = options.output_dir

        if options.timestamp_dir:
            modified_output_dir = os.path.join(
                options.output_dir, 
                datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'))

        found_reports = pybrid.defaultReportLoader.discover(top_level_dir)
        r = pybrid.ReportRunner(
            found_reports, modified_output_dir, *args, **kwargs)
        r.run()
        
        return r
