
import pybrid
import os

class WeimannschusterReport(pybrid.PybridReport):
    AUTHOR = 'allenedickens'
    NAME = 'weimannschusterreport'
    GROUPS = ['cummeratajast', 'cummeratajast']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("fuga iusto perferendis")
        f.close()
