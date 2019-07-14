# web crawler by Sauhard Jain for xino os marathon
import requests
from bs4 import BeautifulSoup
from datetime import datetime


class spider:

    def __init__(self, url):
        self.url = url

    def spides(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')
if soup.title.string is not None:
            now = datetime.now()
            current_time = now.strftime('%H:%M:%S')
print('Sir, found title: {} at {}'.format(
                soup.title.string, current_time))
for a in soup.find_all('a', href=True):
            now = datetime.now()
            access_time = now.strftime('%H:%M:%S')
print('Sir, found page: {} at {}'.format(a['href'], current_time))
for tag in soup.find_all('meta'):
            now = datetime.now()
            current_time = now.strftime('%H:%M:%S')
if tag.get("property", None) == "ex:title":
    print('Found meta title: {} at {}'.format(
        tag.get("content", None), access_time))
if tag.get("property", None) == "ex:description":
    print('Sir found description: {} at {}\n'.format(
        tag.get("content", None), access_time))
spi = spider("http://wikipedia.com")
spi.spides()
