#!/usr/bin/env python3
import sys
import re

for ln in sys.stdin:
    ln = ln.strip().lower()
    words = re.findall(r"[a-zA-Z']+", ln)
    for word in words:
        print(f"{word}\t1")
