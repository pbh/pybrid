
import pybrid
import os

class AbshireReport(pybrid.PybridReport):
    AUTHOR = 'melyssawalsh'
    NAME = 'abshirereport'
    GROUPS = ['prohaskakuhn', 'schinner']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("expedita odit ut")
        f.close()
