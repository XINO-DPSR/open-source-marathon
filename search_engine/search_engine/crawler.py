import requests
import re
import datetime


def crawl_web(initial_url):
    crawl = []
    crawl.append(initial_url)
    while crawl:
        current_url = crawl.pop(0)
        r = requests.get(current_url)
        for url in re.findall('<a href="([^"]+)">', str(r.content)):
            if url[0] == '/':
                url = current_url + url[1:]
            pattern = re.compile('https?')
            if pattern.match(url):
                crawl.append(url)
        title = re.findall(r'<title>(.*)</title>', str(r.content))
        date = datetime.datetime.now()
        return crawl, title, date
print(crawl_web("https://xino.in/"))
