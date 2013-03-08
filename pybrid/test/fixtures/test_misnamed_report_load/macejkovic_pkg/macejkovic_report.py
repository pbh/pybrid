
import pybrid
import os

class MacejkovicReport(pybrid.PybridReport):
    AUTHOR = 'martaschimmel'
    NAME = 'macejkovicreport'
    GROUPS = ['hamill', 'hills']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("numquam id tenetur")
        f.close()
