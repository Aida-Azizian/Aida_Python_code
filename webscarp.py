import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
def get_wanted_article(search_term):
    try:
        search_term = search_term.encode('utf-8')
        wiki = "https://en.wikipedia.org/wiki/"+search_term
        page = urllib2.urlopen(wiki)
        soup = BeautifulSoup(page,'html.parser')
        for paragraph in soup.find_all('p'):
            print(str(paragraph.text))    
    except urllib2.HTTPError:
        sys.exit("Unfortunately your request has led to a HTTPError and page was not found,please refine your search further")
    

get_wanted_article(sys.argv[1])

    

