#! /usr/bin/python
# __init__.py - Make a basic crawler.

import requests, time
from bs4 import BeautifulSoup

def crawler(url):
    res = requests.get(url)
    res.raise_for_status()
    access_time = time.time()
    soup = BeautifulSoup(res.text)
    links = soup.select('a')
    return res.text, access_time, links