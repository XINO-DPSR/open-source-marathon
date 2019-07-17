import datetime
import re
import requests
import time


toCrawlUrls = []  # an array of array of urls, sorted according to domains
toCrawl = []  # an array of domain names
lastCrawled = []  # an array to store when was the domain last crawled


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
    return page, datetime.datetime.utcnow().timestamp(), urls, response.url


def loop():
    try:
        index = lastCrawled.index(min(lastCrawled))
        if datetime.datetime.utcnow().timestamp()-lastCrawled[index] < 1:
            time.sleep(1)
            try:
                url = toCrawlUrls.pop(0)
                result = crawl(url)
                for link in result[3]:
                    addLink(link)
                # do something with data obtained
            except IndexError:
                toCrawl.pop(index)
                toCrawlUrls.pop(index)
                lastCrawled.pop(index)

        loop()
    except IndexError:
        # no tasks left. sleep for some time and try again.
        time.sleep(2)
        loop()


def addLink(url):
    response = requests.get(url)
    baseUrl = response.url
    domain = re.find("https?:\/\/(www\.)?([-a-zA-Z0-9@:%._\+~#=]{1,256}\.)*[a-z]{2,4}", baseUrl)
    robots = requests.get(url).text.splitlines()
    for line in robots:
        if line.startswith('Disallow: '):
            if baseUrl[len(domain):].startswith(line[10:]):
                return

    try:
        index = toCrawlUrls.index(domain)
        lastCrawled[index] = datetime.datetime.utcnow().timestamp()
        try:
            toCrawl[index].index(url)
        except IndexError:
            toCrawl[index].append(url)
    except IndexError:
        toCrawl.append(domain)
        toCrawlUrls.append([url])
        lastCrawled.append(datetime.datetime.utcnow().timestamp())


def parse(data):
    metadata = []

    pattern = "<meta (?!content).*(?:author|description|keywords).*content=\"(?!\")([-a-zA-Z0-9@:%_\+., ~#?&//=\s]*)\">"
    matches = re.findall(pattern, data)
    for match in matches:
        content = re.findall("content=\"(?!\")([-a-zA-Z0-9@:%_\+., ~#?&//=\s]*)\"", match)[0]
        metadata.append(content[9:-1])

    pattern = "<title>.*<\/title>"
    matches = re.findall(pattern, data)
    for match in matches:
        content = match[7:-8].strip()
        metadata.append(content)

    pattern = "<(?:p|h\d{1})>((?!<).)*<\/(?:p|h\d{1})>"
    matches = re.findall(pattern, data)
    for match in matches:
        content = re.findall(">((?!<).)*<\/", match)
        metadata.append(content[1:-2].strip())

    return metadata
