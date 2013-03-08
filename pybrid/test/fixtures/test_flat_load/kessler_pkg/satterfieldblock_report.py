
import pybrid
import os

class SatterfieldblockReport(pybrid.PybridReport):
    AUTHOR = 'tyrelkuphal'
    NAME = 'satterfieldblockreport'
    GROUPS = ['welch', 'shanahan']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("fugit vitae debitis")
        f.close()
