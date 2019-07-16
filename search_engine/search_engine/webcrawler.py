import datetime
import re
import requests


def crawl(url):
    response = requests.get(url)
    page = response.text
    baseUrl = response.url
    matches = re.findall("<a((?!href).)* href=\"(?!\")([-a-zA-Z0-9@:%_\+.~#?&//=\s]*)\">", page)
    urls = []
    for match in matches:
        links = re.findall("href=\"(?!\")([-a-zA-Z0-9@:%_\+.~#?&//=\s]*)\">", match)
        for link in links:
            sub = link[6, -1]
            if sub.startswith('/'):
                urls.append(baseUrl+sub)
            else:
                urls.append(sub)
    return page, datetime.datetime.utcnow().timestamp(), urls
