import os

path=raw_input("PATH:")
listing = os.listdir(path)
sublist=os.listdir(path+"\\subtitles\\")
d={}
for filename in sublist:
    if not('.srt' in filename):
        pass
    else:
        j=''.join(x for x in filename if x.isalpha())
        j=j[:-5]
        d[j]=filename
        print j

for filename in listing:
    if not('.avi' in filename):
        pass
    else:
        a=filename[:-4]
        i=''.join(x for x in a if x.isalpha())
        print i
        max=''.join(y for y in d.keys() if ((y in i) or (i in y)))
        oldname=path+"\\subtitles\\"+d[max]
        newname=path+"\\subtitles\\"+a+'.en.srt'
        print oldname, newname
        os.rename(oldname,newname)
