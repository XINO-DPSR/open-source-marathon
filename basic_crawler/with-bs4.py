import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Crawler:
    def __init__(self, url):
        self.url = url

    def crawl(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html5lib')

        # Get title
        if soup.title.string is not None:
            now = datetime.now()
            current_time = now.strftime('%H:%M:%S')
            print('Found title: {} at {}'.format(
                soup.title.string, current_time))

        # Get meta tags
        for tag in soup.find_all('meta'):
            now = datetime.now()
            current_time = now.strftime('%H:%M:%S')
            if tag.get("property", None) == "og:title":
                print('Found meta title: {} at {}'.format(
                    tag.get("content", None), current_time))
            if tag.get("property", None) == "og:description":
                print('Found meta description: {} at {}\n'.format(
                    tag.get("content", None), current_time))

        # Get all URLs for scraping later
        for a in soup.find_all('a', href=True):
            now = datetime.now()
            current_time = now.strftime('%H:%M:%S')
            print('Found URL: {} at {}'.format(a['href'], current_time))


# URL to crawl
URL = 'https://techcrunch.com'

c = Crawler(URL)
c.crawl()
