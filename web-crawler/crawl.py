import re
import urllib2
import urlparse
listing=raw_input("url:")
where=raw_input("where?")
what=raw_input("what?")

if(listing.endswith('/')):
    if(listing.startswith('w')):
        list="http://"+listing+where.capitalize()+'/'+what.capitalize()
    else:
        list=listing+where.capitalize()+'/'+what.capitalize()
else:
    list="http://"+listing+'/'+where.capitalize()+'/'+what.capitalize()

tocrawl=set([list])
crawled=set([])
keywordregex=re.compile('<span\sclass=["\']Ctitle["\']><a\shref=[\'"](.*?)[\'"]>(.*?)</a></span>.*?')
#linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
count=0
while 1:
    try:
        crawling=tocrawl.pop()
        print crawling
    except KeyError:
        raise StopIteration            
    
    url = urlparse.urlparse(crawling)
    try:
        response = urllib2.urlopen(crawling)
    except:
        continue
    msg = response.read()
    
    startPos = msg.find('<title>')
    if startPos != -1:
        endPos = msg.find('</title>', startPos+7)
    if endPos != -1:
        title = msg[startPos+7:endPos]
        print title
    link={}
    keywordlist = keywordregex.findall(msg)
    print keywordlist[0]
    for i in range(0, len(keywordlist)):
        link['1']=keywordlist[i]
    print link
    #links=linkregex.findall(msg)
    crawled.add(crawling)
    links=[x[0] for x in keywordlist]
    print links

"""    for link in (links.pop(0) for _ in xrange(len(links))):
        if link.startswith('/'):
            link = 'http://' + url[1] + link
        elif link.startswith('#'):
            link = 'http://' + url[1] + url[2] + link
        elif not link.startswith('http'):
            link = 'http://' + url[1] + '/' + link
        if link not in crawled:
            tocrawl.add(link)

"""


    

