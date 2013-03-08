
import pybrid
import os

class BlandaReport(pybrid.PybridReport):
    AUTHOR = 'kaileylegros'
    NAME = 'blandareport'
    GROUPS = ['bernhard', 'runte']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("facere eaque sunt")
        f.close()
