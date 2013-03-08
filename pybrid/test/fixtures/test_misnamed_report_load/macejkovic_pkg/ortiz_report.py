
import pybrid
import os

class OrtizReport(pybrid.PybridReport):
    AUTHOR = 'theresiaeffertz'
    NAME = 'ortizreport'
    GROUPS = ['kleintowne', 'carter']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("illo quas non")
        f.close()
