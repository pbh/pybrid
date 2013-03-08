#!/usr/bin/env python

"""
    hey_SKEL.SKEL
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    SKEL

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

import copy
import os

def author_name_report_dir_mapping(report_instance):
    return '%s_%s' % (report_instance.get_author(),
                      report_instance.get_name())


class ReportRunner(object):
    def __init__(self, report_cls_lst, output_dir,
                 pre_hooks=None, report_filters=None, post_hooks=None,
                 report_dir_mapping=None):
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

    def _get_report_metadata(self, cls):
        l = [m for m in self.report_metadata if m['class'] == cls]
        if len(l) != 1:
            raise RuntimeError(
                'Class %s not found in report metadata.' % str(cls))

        return l[0]

    def run(self):
        for pre_hook in self.pre_hooks:
            pre_hook(self)

        for report_filter in self.report_filters:
            self.report_cls_lst = report_filter(self.report_cls_lst)

        for report_cls in self.report_cls_lst:
            m = self._get_report_metadata(report_cls)

            m['output_dir'] = os.path.join(
                self.output_dir,
                self.report_dir_mapping_fn(m['instance']))

            os.makedirs(m['output_dir'])
            m['instance'].write(m['output_dir'])
            m['run'] = True
        
        for post_hook in self.post_hooks:
            post_hook(self)

    def get_report_metadata(self):
        return copy.deepcopy(self.report_metadata)

    def get_report_output_dirs(self):
        return [r['output_dir']
                for r in self.report_metadata
                if r.has_key('output_dir')]
