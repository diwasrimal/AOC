from tools import pairs, in_order


idx_sum = 0
for i, pair in enumerate(pairs):
    result = in_order(pair)
    if result > 0:
        idx_sum += i + 1
        
print(idx_sum)

