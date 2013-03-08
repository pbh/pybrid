
import pybrid
import os

class JakubowskiReport(pybrid.PybridReport):
    AUTHOR = 'adityacartwright'
    NAME = 'jakubowskireport'
    GROUPS = ['feeneykemmer', 'howe']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("alias dolores est")
        f.close()
