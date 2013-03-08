
import pybrid
import os

class KonopelskiReport(pybrid.PybridReport):
    AUTHOR = 'jamelgibson'
    NAME = 'konopelskireport'
    GROUPS = ['effertzspencer', 'west']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("itaque occaecati aut")
        f.close()
