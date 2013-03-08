
import pybrid
import os

class KoeppwillmsReport(pybrid.PybridReport):
    AUTHOR = 'reggiemorissette'
    NAME = 'koeppwillmsreport'
    GROUPS = ['cassinbashirian', 'sengerstark']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("ut rerum aut")
        f.close()
