import re
import urllib2
from BeautifulSoup import BeautifulSoup

def get_start_url(listing):
    if(listing.endswith('/')):
        if(listing.startswith('w')):
            list="http://"+listing+where.capitalize()+'/'+what.capitalize()
        else:
            list=listing+where.capitalize()+'/'+what.capitalize()
    else:
        list="http://"+listing+'/'+where.capitalize()+'/'+what.capitalize()
    return list


keywordregex=re.compile('<span\sclass=["\']Ctitle["\']><a\shref=[\'"](.*?)[\'"]>(.*?)</a></span>.*?')

def get_html(url):
    msg=urllib2.urlopen(url).read()
    return msg

def get_links(tocrawl, crawled):
    links=[]
    while tocrawl:
        print "crawling", tocrawl
        msg = get_html(tocrawl)
        keywordlist = keywordregex.findall(msg)
        """
        link={}
        for i in range(0, len(keywordlist)):
            link[i]=keywordlist[i]
        print link
        """
        #links=linkregex.findall(msg)
        crawled.append(tocrawl)
        links=[x[0] for x in keywordlist]
        tocrawl=''
    return links

def get_next_link(msg):
    class_regex=re.compile('<div\sclass=[\'"]pagination[\'"]>(.*?)</div>')
    a_list=class_regex.findall(msg)
    a=a_list[0].split('</a>')
    a=[i for i in a if 'next' in i]
    link_regex=re.compile('<a\shref=[\'"](.*?)[\'"]>next\s')
    next_link=link_regex.findall(a[0])
    if len(next_link)>0:
        return next_link[0]
    else:
        return ''

def all_links(url,company_links):
    while 'http://' in url:
        company_links.append(get_links(url,crawled))
        #print company_links
        #url=get_next_link(get_html(url))
        url=''
        if url:
            if (' ' in url):
                url=url.replace(' ','%20')

    return company_links

def get_company_name(soup):
    cname=str(soup.find(id="cn"))
    cregex=re.compile('value=[\'"](.*?)[\'"]')
    c_name=cregex.findall(cname)
    if c_name:
        return c_name[0]
    else:
        return '-'

def get_person_name(soup):
    pname=soup.find(id="more").p.text
    if pname:
        return pname
    else:
        return '-'


def get_phone(soup):
    phone=soup.find(id="more").findAll('p')[1].text
    if phone:
        return phone
    else:
        return '-'

def get_add(soup):
    addr=str(soup.find(id="add"))
    aregex=re.compile('value=[\'"](.*?)[\'"]')
    add=aregex.findall(addr)
    if add:
        return add[0]
    else:
        return '-'

    
if __name__=='__main__':
    listing=raw_input("url:")
    where=raw_input("where?")
    what=raw_input("what?")
    url=get_start_url(listing)
    crawled=[]
    company_links=[]
 
    company_links=all_links(url,company_links)[0]
    #print company_links

    name=[]
    person=[]
    phone=[]
    add=[]
    
    while len(company_links)>0:
        soup=BeautifulSoup(get_html(company_links.pop(0)))
        name.append(get_company_name(soup))
        person.append(get_person_name(soup))
        phone.append(get_phone(soup))
        add.append(get_add(soup))
    print "names:",name
    print "person:",person
    print "phone:",phone
    print "add:",add


    

