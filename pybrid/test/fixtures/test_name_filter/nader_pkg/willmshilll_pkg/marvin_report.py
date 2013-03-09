
import pybrid
import os

class MarvinReport(pybrid.PybridReport):
    AUTHOR = 'fannymertz'
    NAME = 'marvinreport'
    GROUPS = ['huelstracke', 'kiehn']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("quaerat sed iste")
        f.close()
