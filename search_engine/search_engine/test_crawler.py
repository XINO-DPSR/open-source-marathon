import unittest
from ff_crawler import ff_crawler
from ff_crawler import ff_crawler_driver
import requests


class TestParser(unittest.TestCase):

    
    def test_ff_crawler(self):

        # When the domain disallows crawling, the crawler should
        # return an empty list as its third return value.

        self.assertListEqual(ff_crawler('http://coreis.us')[2], [])
        
        # No links should start with mailto: or tel:

        flag = False
        for link in ff_crawler('https://www.scottseverance.us/mailto.html')[2]:
            if link.startswith('mailto:') or link.startswith('tel:'):
                flag = True
                break

        self.assertEqual(flag, False)
        
    def test_ff_crawler_driver(self):

        # When depth is set to 1 for example.com, should return
        # dictionary with two levels.

        self.assertDictEqual(ff_crawler_driver('https://example.com', 1), 
            {0: ['https://example.com'], 1: ['http://www.iana.org/domains/example']})

    

if __name__ == '__main__':
    unittest.main()