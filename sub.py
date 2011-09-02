import os

path=raw_input("PATH:")
listing = os.listdir(path)
sublist=os.listdir(path+"\\subtitles\\")
for filename in listing:
    i=filename[:-4]
    count=0
    for filename in sublist:
        if('.db' in filename):
            []
        else:
            pcount=0
            j=filename[:-4]
            max=j
            for a in range(0,len(i)):
                if((x for x in j if x.isalpha())==(y for y in i if y.isalpha())):
                    print x, y
                    pcount=pcount+1
            if(pcount>count):
                count=pcount
                max=j
    oldname=path+"\\subtitles\\"+max+".jpg"
    newname=path+"\\subtitles\\"+i+'.srt'
    print oldname, newname
    os.rename(oldname,newname)
