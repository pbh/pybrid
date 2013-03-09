
import pybrid
import os

class StantonReport(pybrid.PybridReport):
    AUTHOR = 'angelinaoconnell'
    NAME = 'stantonreport'
    GROUPS = ['johns', 'mann']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("magni id laudantium")
        f.close()
