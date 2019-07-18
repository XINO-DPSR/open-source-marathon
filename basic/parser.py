import re
import requests
import time
from datetime import datetime


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
