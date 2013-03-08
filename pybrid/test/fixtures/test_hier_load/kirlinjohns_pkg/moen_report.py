
import pybrid
import os

class MoenReport(pybrid.PybridReport):
    AUTHOR = 'lerakris'
    NAME = 'moenreport'
    GROUPS = ['dooley', 'waters']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("ut esse dolor")
        f.close()
