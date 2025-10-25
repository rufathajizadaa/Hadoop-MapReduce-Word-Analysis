#!/usr/bin/env python3
import sys
import re
import os

STOPWORD_FILE = os.path.join(os.getcwd(), "stopword_list.txt")

stopwords = set()
try:
    with open(STOPWORD_FILE, "r") as f:
        stopwords = {line.strip().lower() for line in f}
except FileNotFoundError:
    sys.stderr.write("Stopword file not found\n")
    stopwords = set()

for ln in sys.stdin:
    words = re.findall(r'\b[a-zA-Z]+\b', ln.lower())
    filtered = [w for w in words if w not in stopwords]
    for i in range(len(filtered) - 1):
        bigram = f"{filtered[i]} {filtered[i+1]}"
        print(f"{bigram}\t1")
