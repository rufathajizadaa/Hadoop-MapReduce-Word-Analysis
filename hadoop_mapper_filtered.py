#!/usr/bin/env python3
import sys
import re

stopwords = set()
with open('stopword_list.txt', 'r') as f:
    for ln in f:
        stopwords.add(ln.strip().lower())

for ln in sys.stdin:
    ln = ln.strip().lower()
    words = re.findall(r"[a-zA-Z']+", ln)
    for word in words:
        if word not in stopwords:
            print(f"{word}\t1")
