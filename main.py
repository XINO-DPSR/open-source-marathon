import urllib2 # Libraries
import sys
import HTMLParser # HTMLParser
import robots
import time

global baseURL
baseURL = ''

class URLParser():
    def __init__(self):
        self.urlconvs = ["https://", "http://"]
        self.doNots = ["mailto:", "tel:"]
    def parse(self, url, baseurl=False):
        if url[0:2] == "//":
            url = "http:" + url
        if baseurl:
            if '/' not in url:
                url = baseurl+"/"+url
            if baseurl[-1] == "/":
                baseurl = baseurl[0:len(baseurl)-1]
            if '#' in url:
                url = baseurl+url
            if url[0] == "/":
                url = baseurl+url
        for i in self.doNots:
            if i in url:
                return ''
        okurl = False
        
        for i in self.urlconvs:
            if i in url:
                okurl = True
        if okurl == False:
            url = "http://" + url
        return url

crawled = []

allows = []
disallows = []

class Parser(HTMLParser.HTMLParser):

   anchors = list()
   data = ""

   #HTML Parser Methods
   def handle_starttag(self, startTag, attrs):
       if startTag == "a":
           for attr in attrs:
               if attr[0] == "href":
                   urlparser = URLParser()
                   newurl = urlparser.parse(attr[1], baseURL)
                   if newurl == '':
                       pass
                   else:
                        self.anchors.append(newurl)
   def handle_data(self, data):
       self.data+=data

class Crawler():
    def __init__(self, baseurl):
        urlparser = URLParser()
        baseurl2 = urlparser.parse(baseurl)
        if baseurl2 not in crawled:
            print "Starting Crawler on " + baseurl
            print ''
        self.baseURL = baseurl
        self.externalURLs = []
        self.toCrawl = []
        self.crawl(self.baseURL)
    def crawl(self, url): # Main Function
        urlparser = URLParser()
        newurl = urlparser.parse(url)
        if newurl not in crawled:
            global baseURL
            if baseURL in newurl:
                headers = {} # Initializes header
                headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36" # Sets User Agent
                req = urllib2.Request(newurl, headers = headers) # Initializes Request
                res = urllib2.urlopen(req) # Gets Response
                info = res.info() # Gets Request info
                if str(res.code)[0] == "2":
                    parser = Parser()
                    parser.baseurl = self.baseURL
                    parser.feed(res.read())
                    f = open("data/"+time.strftime("%Y-%m-%d-%H-%M-%S")+".txt", "w+")
                    f.write("# "+newurl+"\n"+parser.data)
                    f.close()
                    print "Visited " + newurl + ","
                    print "at " + info['date'] + "."
                    print ''
                    print 'Found links:'
                    print ''
                    for i in parser.anchors:
                        print i
                        self.toCrawl.append(i)
                    print ''
                    crawled.append(newurl)
                    for i in self.toCrawl:
                        if baseURL in i and baseURL != i[0:len(i)-1]:
                            global allows
                            global disallows
                            allowed = True
                            for index in disallows:
                                if type(index) == list:
                                    yes = True
                                    for j in index:
                                        if j in index:
                                            yes = False
                                        else:
                                            yes = True
                                            break
                                    allowed = yes
                                    if allowed == False:
                                        break
                                elif index in i:
                                    allowed = False
                                    break
                            for index in allows:
                                if type(index) == list:
                                    yes = False
                                    for j in index:
                                        if j in index:
                                            yes = True
                                        else:
                                            yes = False
                                            break
                                    allowed = yes
                                    if allowed == False:
                                        break
                                elif index in i:
                                    allowed = False
                                    break
                            if allowed:
                                time.sleep(0.1)
                                newcrawler = Crawler(i)
                else:
                    print 'Could not access webpage.'
            else:
                self.externalURLs.append(newurl)
                self.crawled.append(newurl)

def main(url):
    parser = robots.Parser(url)
    global allows
    global disallows
    if '*' in parser.allows:
        for i in parser.allows["*"]:
            allows.append(i)
    if 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' in parser.allows:
        for i in parser.allows["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"]:
            allows.append(i)
    if '*' in parser.disallows:
        for i in parser.disallows["*"]:
            disallows.append(i)
    if 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' in parser.disallows:
        for i in parser.disallows["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"]:
            disallows.append(i)
    urlparser = URLParser()
    newurl = urlparser.parse(url)
    global baseURL
    baseURL = url
    crawler = Crawler(newurl)
    

if __name__ == '__main__': # Only runs file as long as it's not used as a library.
    main(sys.argv[1]) # Passes in URL as parameter ex. (python main.py https://google.com)
