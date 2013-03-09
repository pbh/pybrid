#!/usr/bin/env python

"""
    hey_SKEL.SKEL
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    SKEL

    :copyright: (c) 2013 by oDesk Corporation.
    :license: BSD, see LICENSE for more details.
"""

class AuthorFilter(object):
    def __init__(self, author_name):
        self.author_name = author_name

    def __call__(self, report_cls_list):
        for cls in report_cls_list:
            inst = cls()
            
            if inst.get_author() == self.author_name:
                yield cls

class NameFilter(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, report_cls_list):
        for cls in report_cls_list:
            inst = cls()
            
            if inst.get_name() == self.name:
                yield cls
