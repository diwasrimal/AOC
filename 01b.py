elves = []
with open("input/01.txt") as infile:
    elf = []
    for calories in infile:
        if calories == "\n":
            elves.append(elf)
            elf = []
        else:
            elf.append(int(calories.rstrip()))

    if elf:
        elves.append(elf)

calorie_sums = [ sum(calories) for calories in elves ]

# Find the 3 highest calories
top3 = []
for _ in range(3):
    highest = 0
    for cal in calorie_sums:
        if cal > highest and cal not in top3:
            highest = cal
    top3.append(highest)

print(sum(top3))
