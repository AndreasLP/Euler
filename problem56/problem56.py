from digital_sum import digital_sum

max_sum = 0
for a in range(1,100):
    for b in range(1,100):
        d_sum = digital_sum(a**b)
        if d_sum > max_sum:
            max_sum = d_sum

print(max_sum)
