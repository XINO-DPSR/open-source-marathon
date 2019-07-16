import urllib.request
from html.parser import HTMLParser
import time



with urllib.request.urlopen('https://sayamkanwar.com/') as response:
   src = response.read()

url = 'https://sayamkanwar.com/'

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            attrs = dict(attrs)
            if 'href' in attrs and attrs['href'].startswith('https'):
                print(attrs['href'])

with urllib.request.urlopen(url) as response:
   src = response.read().decode('utf-8')

parser = MyHTMLParser()
parser.feed(src)


print(src)
print("Timestamp: " + time.strftime('%a %H:%M:%S'))
