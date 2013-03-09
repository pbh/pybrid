
import pybrid
import os

class UllrichkassulkeReport(pybrid.PybridReport):
    AUTHOR = 'cordiesipes'
    NAME = 'ullrichkassulkereport'
    GROUPS = ['group2', 'okon']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("mollitia eveniet dolorum")
        f.close()
