import unittest2
import pybrid
import hey_dl
import re
import os


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
        r = pybrid.run(self.fixture_dir('test_run_report_naming'), out_dir, 
                       report_dir_mapping=pybrid.author_name_report_dir_mapping)

        self.assertTrue(
            re.search(
                'eos eaque soluta',
                self._get_output_text(
                    os.path.join(out_dir, 'cedrickschmitt_armstrongreport',
                                 'index.html'))))
