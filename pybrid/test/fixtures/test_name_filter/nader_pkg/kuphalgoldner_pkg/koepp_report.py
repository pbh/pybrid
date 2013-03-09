
import pybrid
import os

class KoeppReport(pybrid.PybridReport):
    AUTHOR = 'spencerkozey'
    NAME = 'koeppreport'
    GROUPS = ['blickmills', 'beer']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("delectus in beatae")
        f.close()
