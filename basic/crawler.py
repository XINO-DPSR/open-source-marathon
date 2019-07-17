import re
import requests
import random
import time
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

        robots = requests.get(self.url + '/robots.txt').text

        if robots is not None:
            for instruction in robots.splitlines():
                print(instruction)
                if instruction.startswith('Allow:'):
                    subfolder = re.findall(
                        r'Allow: (.*?)', str(instruction))[0]
                    links.append(self.url + subfolder)
                if instruction.startswith('Disallow:'):
                    for link in links:
                        if instruction in link:
                            links.remove(link)

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

            # time.sleep(random.randint(1, 5))

        return title, links_and_data, current_time, main_source
