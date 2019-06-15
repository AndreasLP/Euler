import numpy as np
import csv
n = []
with open("words.txt",newline="") as names:
    reader = csv.reader(names)
    for name in reader:
        n.append(name)
n=n[0]
#print(len(n))
max_len=(max([len(i) for i in n]))
tri = [(i*(i+1))/2 for i in range(1,26*max_len+1)]
m = ord('A')-1
count = 0
#n = ["SKY"]
for word in n:
    score = 0
    #print(word)
    for c in word:
        score += ord(c)-m
    if score in tri:
        count += 1
print(count)
