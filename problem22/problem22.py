import numpy as np
import csv
n = []
with open("names.txt",newline="") as names:
    reader = csv.reader(names)
    for name in reader:
        n.append(name)
n=n[0]
print(len(n))
#print(n)
n.sort()
sum_scores = 0
m = ord('A') - 1
for idx,name in enumerate(n):
    score = 0
    for c in name:
        score += ord(c)-m
    sum_scores += (idx+1)*score

print(sum_scores)    

