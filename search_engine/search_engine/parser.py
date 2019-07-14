#! /usr/bin/python
# parser.py - Reads the data fetched by the crawler, parses it, returns whatever metadata it needs to.

from html.parser import HTMLParser


class metaParser(HTMLParser):

    # Stores metadata in list of dictionaries.
    def handle_starttag(self, tag, attrs):
        if tag == 'meta' or tag == 'link' or tag == 'script' or \
                tag == 'title' or tag == 'style':
            attr = dict(attrs)
            attr['tag'] = tag
            self.metadata.append(attr)


def parser(source_code):
    myParser = metaParser()
    myParser.metadata = []
    myParser.feed(source_code)
    return myParser.metadata
