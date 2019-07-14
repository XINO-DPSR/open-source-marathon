#! /usr/bin/python
# parser.py - Reads the data fetched by the crawler, parses it, returns whatever metadata it needs to.

from html.parser import HTMLParser
import requests
from datetime import datetime

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attr = dict(attrs)
            if 'href' in attr:
                self.links.append(attr)

def crawler(url):
    # Download webpage.
    res = requests.get(url)
    res.raise_for_status()

    # Format time of call as HH:MM:SS:MS.
    access_time = datetime.strftime(datetime.now(), '%H:%M:%S:%f')

    # Create parser object to search for links.
    parser = MyHTMLParser()
    parser.links = []
    parser.feed(res.text)   # feed source code to parser
    links = [link['href'] for link in parser.links]
    return res.text, access_time, links
# [{'tag': }]

class metaParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        if tag == 'head':
            metadata.setdefault(tag, [])
                   


def parser(source_code):
    myParser = metaParser()
    myParser.metadata = []
    myParser.feed(source_code)
    for m in myParser.metadata:
        print(m)
    return myParser.metadata

parser(crawler('https://pypi.org/project/metadata-parser/')[0])