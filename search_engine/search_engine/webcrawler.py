#! /usr/bin/python
# webcrawler.py - Make a basic crawler.

import requests
import os
from html.parser import HTMLParser
from datetime import datetime
from urllib.parse import urljoin


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attr = dict(attrs)
            if 'href' in attr and not attr['href'].startswith('mailto:') \
                    and not attr['href'].startswith('tel:'):
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
    links = [urljoin(url, link['href']) for link in parser.links]
    return res.text, access_time, links
