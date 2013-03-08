
import pybrid
import os

class LefflerblandaReport(pybrid.PybridReport):
    AUTHOR = 'alfonzocummerata'
    NAME = 'lefflerblandareport'
    GROUPS = ['schimmel', 'lebsack']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("aut nemo error")
        f.close()
