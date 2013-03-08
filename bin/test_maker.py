#!/usr/bin/env python

import faker
import sys
import re
import os
import jinja2

NAME_MAP = {}
FAKE_MAP = {}

def valid_node(s):
    return re.search(r'^[pr]\d+$', s)

def valid_struct(s):
    return re.search(r'r\d+$', s)


REPORT_TEMPLATE = """
import pybrid
import os

class {{ reportclass }}Report(pybrid.PybridReport):
    AUTHOR = '{{ author }}'
    NAME = '{{ reportname }}report'
    GROUPS = ['{{ group1 }}', '{{ group2 }}']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("{{ lorem }}")
        f.close()

"""

def make_report_file(f_word, fn):
    global REPORT_TEMPLATE

    t = jinja2.Template(REPORT_TEMPLATE)
    s = t.render(
        reportclass=f_word.capitalize(),
        author='%s%s' % (faker.name.first_name().lower(),
                         faker.name.last_name().lower()),
        reportname = f_word.lower(),
        group1 = faker.internet.domain_word(),
        group2 = faker.internet.domain_word(),
        lorem = ' '.join(faker.lorem.words())
        )
    
    if os.path.exists(fn):
        raise RuntimeError('%s already exists.' % fn)

    f = file(fn, 'w')
    f.write(s)
    f.close()

    print >>sys.stderr, "Made %s." % fn

def make_package(nodes, base_dir):
    global NAME_MAP
    
    mapped_nodes = [NAME_MAP[n] for n in nodes]
    
    parent_nodes = []

    for n in mapped_nodes:
        cur_dir = os.path.join(*([base_dir] + parent_nodes + [n]))
        init_file = os.path.join(cur_dir, '__init__.py')

        if not os.path.isdir(cur_dir):
            os.mkdir(cur_dir)
            print >>sys.stderr, 'Made %s (dir).' % cur_dir

            f = file(init_file, 'w')
            f.write('')
            f.close()
            print >>sys.stderr, 'Made %s.' % init_file

        parent_nodes.append(n)

def make_report(nodes, base_dir):
    global NAME_MAP

    mapped_nodes = [NAME_MAP[n] for n in nodes]
    
    report_fn = os.path.join(
        *([base_dir] + mapped_nodes))

    make_report_file(FAKE_MAP[nodes[-1]], report_fn)

def gen_structure(structure_args, base_dir):
    global NAME_MAP

    for s_arg in structure_args:
        nodes = s_arg.split('/')

        if not valid_struct(s_arg):
            raise RuntimeError('%s is not a valid structure string.' % s_arg)

        for node in nodes:
            if not valid_node(node):
                raise RuntimeError('%s is not valid node string.' % node)

            if node not in NAME_MAP:
                f_word = faker.internet.domain_word()
                FAKE_MAP[node] = f_word
                if node.startswith('p'):
                    NAME_MAP[node] = f_word + '_pkg'
                elif node.startswith('r'):
                    NAME_MAP[node] = f_word + '_report.py'

    for s_arg in structure_args:
        nodes = s_arg.split('/')
        parent_nodes = []

        for node in nodes:
            if node.startswith('p'):
                make_package(parent_nodes + [node], base_dir)
            elif node.startswith('r'):
                make_report(parent_nodes + [node], base_dir)
            else:
                raise RuntimeError('Not possible.')

            parent_nodes.append(node)

def main():
    if len(sys.argv) < 3:
        print >> sys.stderr, "Usage is %s {dir} p1/r1 p1/r2 ..." % sys.argv[0]

    cmd = sys.argv[0]
    output_dir = sys.argv[1]
    structure_args = sys.argv[2:]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    struct = gen_structure(structure_args, output_dir)


if __name__ == '__main__':
    main()
