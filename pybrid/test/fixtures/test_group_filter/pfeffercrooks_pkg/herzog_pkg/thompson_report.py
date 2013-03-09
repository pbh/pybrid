
import pybrid
import os

class ThompsonReport(pybrid.PybridReport):
    AUTHOR = 'tysonwelch'
    NAME = 'thompsonreport'
    GROUPS = ['cruickshankfahey', 'kihn']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("impedit occaecati sunt")
        f.close()
