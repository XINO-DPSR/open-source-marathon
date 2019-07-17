import datetime
import re
import requests


def crawl(url):
    response = requests.get(url)
    page = response.text
    baseurl = response.url
    matches = re.findall('<a((?!href).)* href=\"(?!\")([-a-zA-Z0-9@:%_\+.~#?&//=\s]*)\">', page)
    urls = []
    for match in matches:
        if match[1].startswith('/'):
            urls.append(baseurl+match[1])
        else:
            urls.append(match[1])
    return page, datetime.datetime.utcnow().timestamp(), urls
