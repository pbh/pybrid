
import pybrid
import os

class GislasonReport(pybrid.PybridReport):
    AUTHOR = 'eunadonnelly'
    NAME = 'gislasonreport'
    GROUPS = ['wisokyjacobi', 'streich']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("facilis et aut")
        f.close()
