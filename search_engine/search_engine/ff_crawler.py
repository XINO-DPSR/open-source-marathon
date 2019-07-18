#! /usr/bin/python
# ff_crawler.py - Make a fully-featured crawler.

import requests
import sys
import time
from html.parser import HTMLParser
from datetime import datetime
from os import path
from urllib import robotparser
from urllib.parse import urljoin


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attr = dict(attrs)
            if 'href' in attr and not attr['href'].startswith('mailto:') \
                    and not attr['href'].startswith('tel:'):
                self.links.append(attr)


def ff_crawler(url):

    rp = robotparser.RobotFileParser()
    rp.set_url(path.join(url, 'robots.txt'))
    crawl_delay = 0
    if not rp.read() is None:
        if not rp.can_fetch('*', url):
            return '', None, [], 0
        if not rp.crawl_delay('*') is None: 
            crawl_delay = rp.crawl_delay('*')

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
    return res.text, access_time, links, crawl_delay


def ff_crawler_driver(url, depth=5):
    toCrawl = ff_crawler(url)[2]
    all_urls = {0: [url], 1: toCrawl}
    crawled = [url]
    level = 1
    while level < depth:
        all_urls[level + 1] = []
        for link in all_urls[level]:
            if link not in crawled:
                try:
                    all_urls[level + 1] += ff_crawler(link)[2]
                    crawled.append(link)
                except:
                    continue
        level += 1
    return all_urls
