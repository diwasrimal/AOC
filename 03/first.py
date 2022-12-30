# Each rucksack has two large compartments.
# 'a' and 'A' refer to two different types of items
# List of items for each rucksack is given in a single line.

# A given rucksack always has the same number of items in each of 
# its two compartments, so the first half of the characters 
# represent items in the first compartment, while the second half 
# of the characters represent items in the second compartment

with open("input.txt") as file:
    rucksacks = [ rucksack.rstrip() for rucksack in file ] 

# Priority of each item type
priorities = {}
idx = 1
for i in range(ord('a'), ord('z') + 1):
    priorities[chr(i)] = idx
    idx += 1

for i in range(ord('A'), ord('Z') + 1):
    priorities[chr(i)] = idx
    idx += 1

priority_sum = 0
for rucksack in rucksacks:
    mid = len(rucksack) // 2
    compartment1 = rucksack[:mid]
    compartment2 = rucksack[mid:]

    common_items = []
    for c in compartment2:
        if c in compartment1 and c not in common_items:
            priority_sum += priorities[c]
            common_items.append(c)

print(priority_sum)
