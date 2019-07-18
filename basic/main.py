from crawler import Crawler
from parser import Parser

# URL to crawl
URL = 'https://techcrunch.com'

c = Crawler(URL)
title, links_and_data, current_time, main_source = c.crawl()

print('Title: {}\n'.format(title))

# for link in links:
#     print('Found URL: {} at {}'.format(link, current_time))

p = Parser(links_and_data)
links_with_words = p.parse()
