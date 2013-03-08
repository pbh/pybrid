
import pybrid
import os

class OrnReport(pybrid.PybridReport):
    AUTHOR = 'alfcasper'
    NAME = 'ornreport'
    GROUPS = ['hagenes', 'kassulke']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("quas voluptatem reiciendis")
        f.close()
