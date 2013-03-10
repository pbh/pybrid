#!/usr/bin/env python

"""
    pybrid.filters.*
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    This module is a collection of filters for filtering reports.
    They are used by Pybrid.Runner to filter_reports based on
    various criteria like AUTHOR, NAME, or GROUP.

    Of course, you can write your own filters, you just have
    to have a callable object that returns a subset of the 
    reports you received.

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

class AuthorFilter(object):
    'Filter that returns reports matching author_name.'
    def __init__(self, author_name):
        self.author_name = author_name

    def __call__(self, report_cls_list):
        for cls in report_cls_list:
            inst = cls()
            
            if inst.get_author() == self.author_name:
                yield cls

class NameFilter(object):
    'Filter that returns reports matching report name.'
    def __init__(self, name):
        self.name = name

    def __call__(self, report_cls_list):
        for cls in report_cls_list:
            inst = cls()
            
            if inst.get_name() == self.name:
                yield cls

class GroupFilter(object):
    'Filter that returns reports with at least one of the included groups.'
    def __init__(self, groups):
        self.groups = groups

    def __call__(self, report_cls_list):
        for cls in report_cls_list:
            inst = cls()
            
            if len(set(inst.get_groups()) & set(self.groups)) > 0:
                yield cls

