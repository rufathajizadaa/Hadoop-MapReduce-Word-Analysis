#!/usr/bin/env python3
import sys

current_bigram = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        bigram, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue

    if current_bigram == bigram:
        current_count += count
    else:
        if current_bigram:
            print(f"{current_bigram}\t{current_count}")
        current_bigram = bigram
        current_count = count

# Print the last bigram
if current_bigram:
    print(f"{current_bigram}\t{current_count}")
