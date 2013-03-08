
import pybrid
import os

class OrtizrutherfordReport(pybrid.PybridReport):
    AUTHOR = 'janicebarrows'
    NAME = 'ortizrutherfordreport'
    GROUPS = ['mcculloughpaucek', 'simonis']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("voluptatem ducimus dolorem")
        f.close()
