from pathlib import Path
import time
import os
import uuid
import sys
folder = sys.argv[1]

ofiles = []
for i in os.listdir(folder):
    if os.path.isfile(folder+"\\"+i):
        ofiles.append(folder+"\\"+i)
while True:
    time.sleep(5)
    for i in os.listdir(folder):
        if os.path.isfile(folder+"\\"+i):
            if folder+"\\"+i in ofiles:
                print("no change")
                pass
            else:
                print("change")
                newname = uuid.uuid4().hex
                os.rename(folder+"\\"+i,folder+"\\"+newname)
                f = open(folder+"\\"+newname,"w")
                f.close()
                
