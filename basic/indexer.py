import re


common_words = ['the', 'of', 'a', 'that', 'will', 'was', 'their',
                'those', 'these', 'why', 'whether',
                'when', 'then', 'to', 'or', 'on', 'its', 'it', 'is',
                'in', 'has', 'for', 'and', 'an', 'a', 'The', 'the', 'with']


class Indexer:
    def __init__(self, links_with_words):
        self.links_with_words = links_with_words

    def index(self):
        original_words = []
        inverted_index = {}
        for link in self.links_with_words:
            for word in link['words']:
                if word in common_words:
                    link['words'].remove(word)
                elif word not in original_words:
                    original_words.append(word)

        for i in range(len(self.links_with_words)):
            for word in self.links_with_words[i]['words']:
                if word in original_words:
                    if inverted_index.get(word, None) is not None:
                        inverted_index[word].append(i)
                    elif inverted_index.get(word, None) is None:
                        inverted_index[word] = [i]

        return inverted_index
