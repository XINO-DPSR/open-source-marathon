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
                'words': []
            }

            print('Found URL: {} with Title: {}'.format(
                link_data['link'], link_data['title']))

            links_and_data.append(link_data)

        return title, links_and_data, current_time, main_source


class Parser:
    def __init__(self, links_and_data):
        self.links_and_data = links_and_data

    def parse(self):
        for link in self.links_and_data:
            title = re.findall(r'<title>(.*?)</title>',
                               str(link['source_code']))[0]
            meta_description = re.findall(
                r'<meta name="description" content="(.*?)"',
                str(link['source_code']))[0]

            if meta_description is not None:
                def removeSpecialChars(s): return re.sub(
                    '[^A-Za-z0-9]+', ' ', s)

                title = removeSpecialChars(title)
                meta_description = removeSpecialChars(meta_description)

                words = title.split() + meta_description.split()

                for linkk in range(len(words)):
                    link['words'].append(words[linkk])

                print('Found {} at {}\n'.format(link['words'], link['link']))

        return self.links_and_data


# URL to crawl
URL = 'https://techcrunch.com'

c = Crawler(URL)
title, links_and_data, current_time, main_source = c.crawl()

print('Title: {}\n'.format(title))

# for link in links:
#     print('Found URL: {} at {}'.format(link, current_time))

p = Parser(links_and_data)
links_with_words = p.parse()
