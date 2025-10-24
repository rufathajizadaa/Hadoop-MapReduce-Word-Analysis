from collections import Counter

word_cnt = Counter()
with open("output_wordcount/part-00000", "r", encoding="utf-8") as f:
    for ln in f:
        sb = ln.strip().split("\t")
        if len(sb) != 2:
            continue
        word, cnt = sb
        word_cnt[word] = int(cnt)

total_words = sum(word_cnt.values())
print("Total words:", total_words)

top_10 = word_cnt.most_common(10)
print("\nTop 10 most frequent words:")
for word, cnt in top_10:
    print(f"{word}: {cnt}")

unique_cnt = len(word_cnt)
print("\nUnique words:", unique_cnt)
