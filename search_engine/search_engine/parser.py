#! /usr/bin/python
# parser.py - Reads the data fetched by the crawler, parses it,
# returns whatever metadata it needs to.

from html.parser import HTMLParser


class metaParser(HTMLParser):

    # Stores metadata in list of dictionaries.
    def handle_starttag(self, tag, attrs):
        if tag == 'meta' or tag == 'link' or tag == 'script' or \
                tag == 'title' or tag == 'style':
            attr = dict(attrs)
            attr['tag'] = tag
            self.metadata.append(attr)

    def handle_data(self, data):
        words = data.split(' ')
        for word in words:
            ascii_word = ''.join(
                [l if ord(l) < 128 and ord(l) > 32 else ' '
                    for l in word])
            ascii_word = ascii_word.split(' ')
            for w in ascii_word:
                if w != '':
                    self.source_text.append(w)


def parser(source_code):
    '''
    Input: Source code obtained as first return \
        value of crawler method.
    Returns: myParser.metadata - List of dictionaries \
                containing metadata information.
            data - Set of all individual words found \
                in source code.
    '''
    myParser = metaParser()
    myParser.metadata = []
    myParser.source_text = []
    myParser.feed(source_code)
    data = set(myParser.source_text)
    print(data)
    return myParser.metadata, data
