
import pybrid
import os

class JonesReport(pybrid.PybridReport):
    AUTHOR = 'lilianaweimann'
    NAME = 'jonesreport'
    GROUPS = ['reichert', 'tremblay']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("doloribus veritatis dignissimos")
        f.close()
