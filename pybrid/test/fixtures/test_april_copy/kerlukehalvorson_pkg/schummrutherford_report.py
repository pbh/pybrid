
import pybrid
import os

class SchummrutherfordReport(pybrid.PybridReport):
    AUTHOR = 'keondach'
    NAME = 'schummrutherfordreport'
    GROUPS = ['wilkinson', 'rath']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("quis est quia")
        f.close()
