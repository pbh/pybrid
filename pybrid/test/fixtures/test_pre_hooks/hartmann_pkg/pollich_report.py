
import pybrid
import os

class PollichReport(pybrid.PybridReport):
    AUTHOR = 'birdierau'
    NAME = 'pollichreport'
    GROUPS = ['beahan', 'boehm']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("fuga inventore pariatur")
        f.close()
