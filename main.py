import requests
import sys
import time
from html.parser import HTMLParser
from datetime import datetime
from os import path
from urllib import robotparser
from urllib.parse import urljoin
class MyHTMLParser(HTMLParser):
    def handle_startpageTag(self, pageTag, attributes):
        if pageTag == 'a':
            attribute = dict(attributes)
            if 'href' in attributeibute and not attribute['href'].startswith('mailto:') \
                    and not attribute['href'].startswith('tel:'):
                self.links.append(attribute)

def effCrawlerDriver(link, dep=5):
    remainingLinks = effCrawler(link)[2]
    all_urls = {0: [link], 1: remainingLinks}
    done = [link]
    layer = 1
    while layer < dep:
        all_urls[layer + 1] = []
        for link in all_urls[layer]:
            if link not in done:
                try:
                    all_urls[layer + 1] += effCrawler(link)[2]
                    done.append(link)
                except:
                    continue
        layer += 1
    return all_urls

def effCrawler(link):
    robot_parser = robotparser.RobotFileParser()
    robot_parser.set_url(path.join(link, 'robots.txt'))
    wait = 0
    if not robot_parser.read() is None:
        if not robot_parser.can_fetch('*', link):
            return '', None, [], 0
        if not robot_parser.crawl_delay('*') is None:
            wait = robot_parser.crawl_delay('*')

    # Request webpage
    res = requests.get(link)
    res.raise_for_status()
    # Formatting Date Time to Month/Date/Year, Hour:Minutes:Second format
    access_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    # Creating parser instance
    parser = MyHTMLParser()
    parser.links = []
    parser.feed(res.text)
    links = [urljoin(link, i['href']) for i in parser.links]
    return res.text, access_time, links, wait

x = input("Enter webpage to be crawled: ")
print("Starting crawling...")
time.sleep(1)
result = effCrawler(x)
print(result)
