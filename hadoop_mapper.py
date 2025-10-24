import sys

for ln in sys.stdin:
    ln = ln.strip().lower()
    words = ln.split()
    for word in words:
        print(f"{word}\t1")
