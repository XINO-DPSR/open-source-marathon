import re
import requests
from datetime import datetime


class Crawler:
    def __init__(self, url):
        self.url = url

    def crawl(self):
        links_and_data = []
        r = requests.get(self.url)
        main_source = r.content

        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')

        title = re.findall(r'<title>(.*?)</title>', str(main_source))[0]
        links = re.findall(r'<a href="(.*?)"', str(main_source))

        for link in links:
            if link.startswith('mailto:') or link.startswith('tel:') \
               or link.startswith('#'):
                continue
            r = requests.get(link)
            source = r.content
            link_data = {
                'title': title,
                'link': link,
                'source_code': source,
            }

            print('Found URL {} with title {}'.format(
                link_data['link'], link_data['title']))

            links_and_data.append(link_data)

        return title, links_and_data, current_time, main_source


# URL to crawl
URL = 'https://techcrunch.com'

c = Crawler(URL)
title, links_and_data, current_time, source_code = c.crawl()

print('Title: {}'.format(title))

for link in links_and_data:
    print('Found URL: {} with title {} at {}'.format(
        link['link'], link['title'], current_time))

print('\nComplete source code of the start document: {}'.format(source_code))
