
import pybrid
import os

class RennerReport(pybrid.PybridReport):
    AUTHOR = 'alyssonbednar'
    NAME = 'rennerreport'
    GROUPS = ['hermannglover', 'homenick']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("voluptatum impedit ut")
        f.close()
