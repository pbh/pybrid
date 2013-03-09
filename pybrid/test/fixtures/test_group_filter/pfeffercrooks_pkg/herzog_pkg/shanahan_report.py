
import pybrid
import os

class ShanahanReport(pybrid.PybridReport):
    AUTHOR = 'josiejohnston'
    NAME = 'shanahanreport'
    GROUPS = ['group1', 'nicolastorphy']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("distinctio molestiae rerum")
        f.close()
