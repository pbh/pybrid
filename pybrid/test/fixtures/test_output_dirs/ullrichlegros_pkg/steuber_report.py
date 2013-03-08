
import pybrid
import os

class SteuberReport(pybrid.PybridReport):
    AUTHOR = 'hebercassin'
    NAME = 'steuberreport'
    GROUPS = ['bogisich', 'trantowboehm']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("asperiores vel rerum")
        f.close()
