
import pybrid
import os

class KulasprosaccoReport(pybrid.PybridReport):
    AUTHOR = 'reggiemorissette'
    NAME = 'kulasprosaccoreport'
    GROUPS = ['hilpert', 'cruickshank']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("sed nesciunt vel")
        f.close()
