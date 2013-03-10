#!/usr/bin/env python

"""
    pybrid.runner
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    The home of ReportRunner, a class for generating reports.

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

import copy
import os

def author_name_report_dir_mapping(report_instance):
    'Map from report classes to directory names as {author}_{report}.'
    return '%s_%s' % (report_instance.get_author(),
                      report_instance.get_name())


class ReportRunner(object):
    
    """
    A class for generating reports by running PybridReport classes.

    get_output_dir() --- the directory reports will be output to.
    run() --- execute the report generation.
    get_report_output_dirs() --- get the dirs where reports were output to.
    get_report_metadata() --- get data about report running (best to avoid).
    """
    
    def __init__(self, report_cls_lst, output_dir,
                 pre_hooks=None, report_filters=None, post_hooks=None,
                 report_dir_mapping=None):
        """
        Create a new ReportRunner.

        report_cls_list --- a list of PybridReports (usually from ReportLoader).
        output_dir --- directory to output reports to.
        pre_hooks --- list of callables to run before reports.
        report_filters --- list of callables that filter reports.
        post_hooks --- list of callables that run after reports.
        report_dir_mapping --- a mapping from reports to output directory names.
        """
        self.report_cls_lst = report_cls_lst

        self.output_dir = output_dir

        if pre_hooks is None:
            self.pre_hooks = []
        else:
            self.pre_hooks = pre_hooks

        if report_filters is None:
            self.report_filters = []
        else:
            self.report_filters = report_filters

        if post_hooks is None:
            self.post_hooks = []
        else:
            self.post_hooks = post_hooks

        if report_dir_mapping is None:
            self.report_dir_mapping_fn = author_name_report_dir_mapping
        else:
            self.report_dir_mapping_fn = report_dir_mapping

        self.report_metadata = [
            {'class': cls, 'instance': cls()} for cls in self.report_cls_lst]

    def get_output_dir(self):
        'Return path to report output directory.'
        return self.output_dir

    def _get_report_metadata(self, cls):
        l = [m for m in self.report_metadata if m['class'] == cls]
        if len(l) != 1:
            raise RuntimeError(
                'Class %s not found in report metadata.' % str(cls))

        return l[0]

    def run(self):
        'Execute PybridReports, generating reports in output directory.'
        for pre_hook in self.pre_hooks:
            pre_hook(self)

        for report_filter in self.report_filters:
            self.report_cls_lst = report_filter(self.report_cls_lst)

        for report_cls in self.report_cls_lst:
            m = self._get_report_metadata(report_cls)

            m['output_dir'] = os.path.join(
                self.output_dir,
                self.report_dir_mapping_fn(m['instance']))
          
            m['author'] = m['instance'].get_author()
            m['name'] = m['instance'].get_name()
            m['groups'] = m['instance'].get_groups()

            os.makedirs(m['output_dir'])
            m['instance'].write(m['output_dir'])
            m['run'] = True
        
        for post_hook in self.post_hooks:
            post_hook(self)

    def get_report_metadata(self):
        'Get internal report metadata information.'
        return copy.deepcopy(self.report_metadata)

    def get_report_output_dirs(self):
        'Get directories (within output_dir) where reports sent output.'
        return [r['output_dir']
                for r in self.report_metadata
                if r.has_key('output_dir')]
