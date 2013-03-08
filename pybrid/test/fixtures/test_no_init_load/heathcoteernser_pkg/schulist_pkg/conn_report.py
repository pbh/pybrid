
import pybrid
import os

class ConnReport(pybrid.PybridReport):
    AUTHOR = 'jenningshagenes'
    NAME = 'connreport'
    GROUPS = ['lubowitzzboncak', 'marksterry']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("quasi mollitia in")
        f.close()
