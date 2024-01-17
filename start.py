import os
from subprocess import Popen
from vars import *
from pathlib import Path

if downloads:
    folder = str(Path.home() / "Downloads")
else:
    folder = "C:\\Users\\Vishal\\Downloads\\pp"
files = os.listdir(folder)


for i in files:
    if os.path.isfile(folder+"\\"+i):
        pass
    else:
        Popen([python,worm,folder+"\\"+i])
Popen([python,worm,folder])
