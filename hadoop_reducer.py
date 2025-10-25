#!/usr/bin/env python3
import sys

curr_word = None
curr_cnt = 0

for ln in sys.stdin:
    word, cnt = ln.strip().split("\t")
    cnt = int(cnt)
    if curr_word == word:
        curr_cnt += cnt
    else:
        if curr_word:
            print(f"{curr_word}\t{curr_cnt}")
        curr_word = word
        curr_cnt = cnt

if curr_word:
    print(f"{curr_word}\t{curr_cnt}")
