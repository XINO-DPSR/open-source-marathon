#! /usr/bin/python
# __init__.py - Make a basic crawler.

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def crawler(url):
    res = requests.get(url)
    res.raise_for_status()
    access_time = datetime.strftime(datetime.now(), '%H:%M:%S')
    soup = BeautifulSoup(res.text)
    links = soup.select('a')
    return res.text, access_time, links