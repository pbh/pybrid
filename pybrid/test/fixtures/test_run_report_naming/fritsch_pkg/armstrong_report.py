
import pybrid
import os

class ArmstrongReport(pybrid.PybridReport):
    AUTHOR = 'cedrickschmitt'
    NAME = 'armstrongreport'
    GROUPS = ['medhurst', 'langturcotte']    

    def write(self, output_dir):
        f = file(os.path.join(output_dir, 'index.html'), 'w')
        f.write("eos eaque soluta")
        f.close()
