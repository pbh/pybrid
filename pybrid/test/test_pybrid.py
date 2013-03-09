import unittest2
import pybrid
import hey_dl
import re
import os

class HookTester(object):
    def __init__(self):
        self.called = False

    def __call__(self, runner):
        self.called = True

    def was_called(self):
        return self.called


class PybridTestCase(unittest2.TestCase):
    def setUp(self):
        self._l = pybrid.defaultReportLoader
        self._l.reset()
        self._dl = hey_dl.DirectoryLocalizer()
        self._dl.set()

    def tearDown(self):
        pass
    
    def fixture_dir(self, d):
        return self._dl.path('fixtures/%s' % d)


class LoaderTestCase(PybridTestCase):
    def test_flat_load(self):
        found_reports = self._l.discover(self.fixture_dir('test_flat_load'))
        self.assertEqual(len(found_reports), 2)

    def test_hier_load(self):
        found_reports = self._l.discover(self.fixture_dir('test_hier_load'))
        self.assertEqual(len(found_reports), 3)

    def test_misnamed_report_load(self):
        found_reports = self._l.discover(self.fixture_dir('test_misnamed_report_load'))
        self.assertEqual(len(found_reports), 2)

    def test_no_init_load(self):
        found_reports = self._l.discover(self.fixture_dir('test_no_init_load'))
        self.assertEqual(len(found_reports), 2)

class RunnerTestCase(PybridTestCase):
    def _new_output_dir(self):
        import warnings
        warnings.filterwarnings("ignore", "tempnam", RuntimeWarning)
        warnings.filterwarnings("ignore", "tmpnam", RuntimeWarning)

        self._run_output_dir = os.tempnam('/tmp')

    def _get_output_dir(self):
        return self._run_output_dir

    def _get_output_fn(self, fn):
        return os.path.join(self._get_output_dir(), fn)

    def _get_output_text(self, fn):
        return file(self._get_output_fn(fn)).read()

    def test_run_no_defaults(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        found_reports = self._l.discover(self.fixture_dir('test_run_no_defaults'))

        r = pybrid.ReportRunner(
            found_reports,
            out_dir,
            pre_hooks=[],
            report_filters=[],
            post_hooks=[]
            )

        r.run()

        self.assertTrue(
            re.search(
                'facilis et aut',
                self._get_output_text(
                    os.path.join(r.get_report_output_dirs()[0], 'index.html'))))


    def test_run_defaults(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        found_reports = self._l.discover(self.fixture_dir('test_run_defaults'))

        r = pybrid.ReportRunner(found_reports, out_dir)
        r.run()

        self.assertTrue(
            re.search(
                'quas voluptatem reiciendis',
                self._get_output_text(
                    os.path.join(r.get_report_output_dirs()[0], 'index.html'))))

    def test_run_main(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        r = pybrid.run(self.fixture_dir('test_run_main'), out_dir)

        self.assertTrue(
            re.search(
                'voluptatem sit et',
                self._get_output_text(
                    os.path.join(r.get_report_output_dirs()[0], 'index.html'))))

    def test_run_report_naming(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        pybrid.run(self.fixture_dir('test_run_report_naming'), out_dir, 
                       report_dir_mapping=pybrid.author_name_report_dir_mapping)

        self.assertTrue(
            re.search(
                'eos eaque soluta',
                self._get_output_text(
                    os.path.join(out_dir, 'cedrickschmitt_armstrongreport',
                                 'index.html'))))

    def test_output_dirs(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        r = pybrid.run(self.fixture_dir('test_output_dirs'), out_dir,
                       report_dir_mapping=pybrid.author_name_report_dir_mapping)

        o_dirs = r.get_report_output_dirs()

        expected_report_names = ['janicebarrows_ortizrutherfordreport',
                                 'mafaldamayer_bergnaumreport',
                                 'hebercassin_steuberreport']

        self.assertEqual(
            len([o_dir for o_dir in o_dirs if out_dir in o_dir]), 3) # 3 reports

        for er_name in expected_report_names:
            self.assertEqual(
                len([o_dir for o_dir in o_dirs if er_name in o_dir]), 1)
        
    def test_pre_hooks(self):
        uncalled_tester = HookTester()
        called_tester = HookTester()

        self.assertFalse(uncalled_tester.was_called())
        self.assertFalse(called_tester.was_called())

        self._new_output_dir()
        out_dir = self._get_output_dir()
        pybrid.run(self.fixture_dir('test_pre_hooks'), out_dir,
                   pre_hooks = [called_tester])

        self.assertTrue(called_tester.was_called())
        self.assertFalse(uncalled_tester.was_called())

    def test_post_hooks(self):
        called_tester1 = HookTester()
        called_tester2 = HookTester()

        self.assertFalse(called_tester1.was_called())
        self.assertFalse(called_tester2.was_called())

        self._new_output_dir()
        out_dir = self._get_output_dir()
        pybrid.run(self.fixture_dir('test_post_hooks'), out_dir,
                   post_hooks = [called_tester1, called_tester2])

        self.assertTrue(called_tester1.was_called())
        self.assertTrue(called_tester2.was_called())


    def test_author_filter(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        r = pybrid.run(
            self.fixture_dir('test_author_filter'), out_dir,
            report_filters=[
                pybrid.filters.AuthorFilter('reggiemorissette')])

        self.assertEqual(len(r.get_report_output_dirs()), 2)

    def test_name_filter(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        r = pybrid.run(
            self.fixture_dir('test_name_filter'), out_dir,
            report_filters=[
                pybrid.filters.NameFilter('koeppreport')])

        self.assertEqual(len(r.get_report_output_dirs()), 1)

    def test_group_filter(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        r = pybrid.run(
            self.fixture_dir('test_group_filter'), out_dir,
            report_filters=[
                pybrid.filters.GroupFilter(['group1', 'group2'])])

        self.assertEqual(len(r.get_report_output_dirs()), 3)

    def test_write_string(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        r = pybrid.run(self.fixture_dir('test_write_string'), out_dir)

        self.assertTrue(
            re.search(
                'quia officia aut',
                self._get_output_text(
                    os.path.join(r.get_report_output_dirs()[0], 'index.html'))))

    def test_april_copy(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        pybrid.run(self.fixture_dir('test_april_copy'), out_dir,
                   post_hooks = [pybrid.hooks.AprilCopyHook()])

        self.assertTrue(
            os.path.isdir(
                os.path.join(
                    out_dir, 'april_assets'
                    )
                )
            )

    def test_index_html_hook(self):
        self._new_output_dir()
        out_dir = self._get_output_dir()
        pybrid.run(self.fixture_dir('test_index_html_hook'), out_dir,
                   post_hooks = [pybrid.hooks.IndexHtmlGeneratorHook()],
                   report_dir_mapping=pybrid.author_name_report_dir_mapping)

        self.assertTrue(
            'lilianaweimann_jonesreport/index.html' in file(
                os.path.join(
                    out_dir, 'index.html'
                    )
                ).read()
            )

