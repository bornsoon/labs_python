"""
문서 비교
"""
import re
import matplotlib.pyplot as plt

text1_words = None
with open('datasets/pg1661.txt', mode='rt', encoding="utf-8") as f:
    content = f.read()
    text1_words = [w.lower().strip('.,!?";') for w in content.replace('\n', ' ').split()]
    # print(text1_words)

text2_words = None
with open('datasets/120-0.txt', mode='rt', encoding="utf-8") as f:
    content = f.read()
    text2_words = [w.lower().strip('.,!?"') for w in content.replace('\n', ' ').split()]
    # print(text2_words)

print(len(text1_words), len(text2_words))

text1_set = set(text1_words) - set(['', ' ', 'the', 'a', 'is', 'at'])
text2_set = set(text2_words) - set(['', ' ', 'the', 'a', 'is', 'at'])
# print(text2_set)

diff_words = text1_set ^ text2_set
intsec_words = text1_set & text2_set
union_words = text1_set | text2_set

print(len(diff_words)/len(union_words))
print(len(intsec_words)/len(union_words))

labels = ['Diff', 'IntSec']
ratio = [len(diff_words)/len(union_words), len(intsec_words)/len(union_words)]

plt.figure(figsize=(20, 20))
plt.pie(ratio, labels=labels, shadow=True, autopct='%.1f%%', startangle=90)
plt.show()