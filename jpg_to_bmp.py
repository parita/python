import sys
import os, time
import subprocess
 
path = raw_input("PATH:")
print path
listing = os.listdir(path)
for filename in listing:
    print "current file is: " + filename
    newname=path+filename[:-4]+'.bmp'
    print newname
    os.rename(path+filename,newname)
