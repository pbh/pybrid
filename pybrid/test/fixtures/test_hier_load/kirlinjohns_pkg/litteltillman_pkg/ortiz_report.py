
import pybrid
import os

class OrtizReport(pybrid.PybridReport):
    AUTHOR = 'petraokuneva'
    NAME = 'ortizreport'
    GROUPS = ['davisprosacco', 'dickenskutch']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("animi est quia")
        f.close()
