import nltk
from xml.dom import minidom
import os
import re
from utils import *

directory = 'pan14-author-profiling-training-corpus-2014-04-16/mnt/nfs/tira/data/pan14-training-corpora-truth/pan14-author-profiling-training-corpus-english-blogs-2014-04-16'


def get_POS_Tags(authorFileName):
    author = {}
    file = directory+"/"+authorFileName
    xmldoc = minidom.parse(file)
    rawdocuments = xmldoc.getElementsByTagName('document')
    documents = []
    for document in rawdocuments:
        doc = {}
        text = document.firstChild.nodeValue.strip()
        text = removeTag_CDATA_section(text)
        tokens = nltk.word_tokenize(text)
        doc["pos_tags"] = nltk.pos_tag(tokens)
        documents.append(doc)
    author['documents'] = documents
    author['id'] = authorFileName[:-4]
    print author['id']
    return author

authorFileNames = os.listdir(directory)

authors = []
for file in authorFileNames:
    if file.endswith(".xml"):
        author = get_POS_Tags(file)
        authors.append(author)

import json
with open('POStags.txt', 'w') as outfile:
    json.dump(authors, outfile)
