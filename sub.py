import os

path=raw_input("PATH:")
listing = os.listdir(path)
sublist=[]
medialist=[]
for filename in listing:
    if '.en.srt' in filename:
        sublist.append(filename)
for filename in listing:
    if '.avi' in filename:
        medialist.append(filename)
d={}
for filename in sublist:
    if not('.srt' in filename):
        pass
    else:
        j=''.join(x for x in filename if x.isalpha())
        j=j.replace('ensrt','')
        d[j]=filename

for filename in medialist:
    if not('.avi' in filename):
        pass
    else:
        i=''.join(x for x in filename if x.isalpha())
        i=i.replace('avi','')
        max=''.join(y for y in d.keys() if ((y in i) or (i in y)))
        oldname=path+"\\"+d[max]
        newname=path+"\\"+filename.replace('.avi','')+'.en.srt'
        print oldname, newname
        os.rename(oldname,newname)
