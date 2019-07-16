#! /usr/bin/python
# webcrawler.py - Make a basic crawler.

import requests, sys, time
from html.parser import HTMLParser
from datetime import datetime
from os import path


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attr = dict(attrs)
            if 'href' in attr and not attr['href'].startswith('mailto:') \
                    and not attr['href'].startswith('tel:'):
                self.links.append(attr)


def ffs_crawler(url):

    headers = {'User-Agent': 'Slurp'}
    possible_uas = ['*', 'Slurp']
    # Download robots.txt file.
    robots_txt = requests.get(path.join(url, 'robots.txt'), headers=headers)
    try:
        robots_txt.raise_for_status()
        text = robots_txt.text.split('\n')
        text_dict = {'Disallow:': [], 'Crawl-delay:': []}
        lineNum = 0
        while lineNum < len(text):
            if text[lineNum].split(' ')[0] in possible_uas:
                print(text[lineNum])
                for i in range(lineNum + 1, len(text)):
                    if text[i].startswith('User-agent:'):
                        lineNum = i - 1
                        break
                    line = text[i].split(' ')
                    print(line)
                    keyword = line[0]
                    if keyword in text_dict:
                        text_dict[keyword].append(path.join(url, line[1]))
            lineNum += 1
        if text_dict['Crawl-delay:']:
            delay = max(text_dict['Crawl-delay:'])
        else:
            delay = 0

        print(text_dict)
        if url in text_dict['Disallow:']:
            print('Cannot crawl:', url)
            sys.exit()

    except Exception as err:
        print('robots.txt file for', url, 'returned:', err)
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
    return res.text, access_time, links, delay

def ffs_crawler_driver(url):
    try:
        while True:
            data = list(ffs_crawler(url))
            time.sleep(data[3])
    except KeyboardInterrupt:
        print('Done crawling.')

ffs_crawler_driver('https://buzzfeed.com')
