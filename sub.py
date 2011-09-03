import os

path=raw_input("PATH:")
listing = os.listdir(path)
sublist=os.listdir(path+"\\subtitles\\")
for filename in listing:
    if not('.avi' in filename):
        []
    else:
        a=filename[:-4]
        count=0
        i=''
        for x in a:
            if x.isalpha():
                i=i+x
        maxc=''
        for filename in sublist:
            if not('.srt' in filename):
                []
            else:
                pcount=0
                b=filename[:-4]
                j=''
                for y in b:
                    if y.isalpha():
                        j=j+y
                for z in range(0,min(len(i),len(j))):
                    if(i[z]==j[z]):
                        pcount=pcount+1
                if(pcount>count):
                    count=pcount
                    maxc=b
        oldname=path+"\\subtitles\\"+maxc+".srt"
        newname=path+"\\subtitles\\"+a+'.srt'
        print oldname, newname
        os.rename(oldname,newname)

    
