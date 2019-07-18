from html.parser import HTMLParser


class parseMetaData(HTMLParser):

    # Saves all the pages metadata
    def handle_tag(self, pageTag, attributes):
        if pageTag == 'meta' or pageTag == 'link' or pageTag == 'script' or \
                pageTag == 'title' or pageTag == 'style':
            attribute = dict(attributes)
            attribute['pageTag'] = pageTag
            self.metadata.append(attribute)

    def handle_data(self, myData):
        myWord = myData.split(' ')
        for word in myWord:
            asciiw = ''.join(
                [l if ord(l) < 128 and ord(l) > 32 else ' '
                    for l in word])
            asciiw = asciiw.split(' ')
            for w in asciiw:
                if w != '':
                    self.text.append(w)


def parser(source_code):
    '''
    Input: Crawler returns the source code.
    Returns: metadata from the source code
            set of words found in source code
    '''
    myParser = parseMetaData()
    myParser.metadata = []
    myParser.text = []
    myParser.feed(source_code)
    myWord = set(myParser.text)
    return myParser.metadata, myWord, source_code
