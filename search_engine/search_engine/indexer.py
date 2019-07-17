#! /usr/bin/python
# indexer.py - Make a basic indexer and database structure.

import json
import parser
import requests

# Test code
# res = requests.get('https://sayamkanwar.com')
# metadata, words, source_code = parser.parser(res.text)

def indexer(metadata, words, source_code):
    inverted_index =  {}
    for i in range(len(words)):
        inverted_index[words[i]] = [i]
        inverted_index[words[i]].append(source_code.index(words[i]))
    db = open('jsonDB.json', 'w')
    jsonString = json.dumps(inverted_index)
    db.write(jsonString)
    db.close()

# indexer(metadata, list(words), source_code)