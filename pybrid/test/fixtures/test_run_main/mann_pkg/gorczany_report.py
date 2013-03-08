
import pybrid
import os

class GorczanyReport(pybrid.PybridReport):
    AUTHOR = 'berniecehammes'
    NAME = 'gorczanyreport'
    GROUPS = ['langmonahan', 'harber']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("voluptatem sit et")
        f.close()
