
import pybrid
import os

class BergnaumReport(pybrid.PybridReport):
    AUTHOR = 'mafaldamayer'
    NAME = 'bergnaumreport'
    GROUPS = ['sanforddare', 'koelpintrantow']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("et doloribus deserunt")
        f.close()
