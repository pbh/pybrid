
import pybrid
import os

class WolffhermanReport(pybrid.PybridReport):
    AUTHOR = 'isabellamills'
    NAME = 'wolffhermanreport'
    GROUPS = ['bauchsauer', 'group1']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("cumque repellat sequi")
        f.close()
