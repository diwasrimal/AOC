elves = []
with open("input.txt") as infile:
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
print(max(calorie_sums))
