
import pybrid
import os

class HuelsReport(pybrid.PybridReport):
    AUTHOR = 'reinahuel'
    NAME = 'huelsreport'
    GROUPS = ['champlin', 'fadelhirthe']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("ex ut veniam")
        f.close()
