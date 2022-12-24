def group_badge(group):
    for char in group[0]:
        if char in group[1] and char in group[2]:
            return char

groups = []
with open("./input/03.txt") as file:
    group = []
    for rucksack in file:
        rucksack = rucksack.rstrip()
        group.append(rucksack)
        if len(group) == 3:
            groups.append(group)
            group = []

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
for group in groups:
    priority_sum += priorities[group_badge(group)]

print(priority_sum)
