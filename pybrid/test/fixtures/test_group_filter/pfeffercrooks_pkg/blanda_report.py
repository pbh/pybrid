
import pybrid
import os

class BlandaReport(pybrid.PybridReport):
    AUTHOR = 'marielahaley'
    NAME = 'blandareport'
    GROUPS = ['lowefritsch', 'bartell']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("quasi distinctio dolorem")
        f.close()
