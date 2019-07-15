import unittest
from crawler import crawl_web


class Tests(unittest.TestCase):

    def setup(self):
        pass

    def test(self):
        self.assertEqual(crawl_web.title("https://xino.in"), "XINO 2019")
