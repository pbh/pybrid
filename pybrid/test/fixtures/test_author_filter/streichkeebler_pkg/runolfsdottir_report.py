
import pybrid
import os

class RunolfsdottirReport(pybrid.PybridReport):
    AUTHOR = 'jerroldschmitt'
    NAME = 'runolfsdottirreport'
    GROUPS = ['sanford', 'emmerich']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("minus quia iusto")
        f.close()
