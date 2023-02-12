from subprocess import Popen
import sys
import os
exefile='winword.exe'
pathfile=r'c:/Program Files'

class checkdir:

    

    def find_all(self, exefile, pathfile):
        result = []
        for root, dirs, files in os.walk(pathfile):
            if exec in files:
                result.append(os.path.join(root, exefile))
        return True
    



