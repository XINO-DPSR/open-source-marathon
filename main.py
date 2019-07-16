import urllib2
import sys
import HTMLParser


class Parser(HTMLParser.HTMLParser):

    anchors = list()

    # HTML Parser Methods
    def handle_starttag(self, startTag, attrs):
        if startTag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.anchors.append(attr[1])


def main(url):
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
    req = urllib2.Request(url, headers=headers)
    res = urllib2.urlopen(req)
    info = res.info()
    parser = Parser()
    parser.feed(res.read())
    print "Made request to: " + url + ","
    print "at " + info['date'] + "."
    print ''
    print 'Found links:'
    print ''
    for i in parser.anchors:
        print i


if __name__ == '__main__':
    # Passes in URL as parameter ex. (python main.py https://google.com)
    main(sys.argv[1])
