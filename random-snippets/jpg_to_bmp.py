import sys
import os, time
import subprocess
 
path = raw_input("PATH:")
print path
listing = os.listdir(path)
for filename in listing:
    if not ('.jpg' in filename):
        pass
    else:
        print "current file is: " + filename
        newname=filename.replace('.jpg','.bmp')
        print newname
        os.rename(path+'\\'+filename,newname)
