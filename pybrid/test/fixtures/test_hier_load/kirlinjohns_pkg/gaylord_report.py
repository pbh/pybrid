
import pybrid
import os

class GaylordReport(pybrid.PybridReport):
    AUTHOR = 'eddiekeebler'
    NAME = 'gaylordreport'
    GROUPS = ['rolfson', 'feil']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("sapiente possimus rerum")
        f.close()
