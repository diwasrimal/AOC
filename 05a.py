import re


def print_stacks(stacks):
    print("Stacks:")
    for i in range(len(stacks)):
        print(f"{i + 1}: {stacks[i]}")
    print()


def print_top_of_stacks(stacks):
    top = ""
    for stack in stacks:
        top += stack[-1]
    print(top)


# Split stacks and moves
with open("input/05.txt") as file:
    data = file.read().split('\n\n')
    stack_input = data[0]
    moves = data[1]

# Make stacks required to store crates
lines = stack_input.split('\n')
stacks = [ [] for _ in range(len(lines[0][1::4])) ] 

# Add crates to corresponding stacks from top
for line in lines[:-1]:
    crates = line[1::4]
    for i in range(len(crates)):
        if crates[i] != ' ':
            stacks[i].insert(0, crates[i])

# Move crates
for move in moves.splitlines():
    no_of_crates, src, dest = list(map(int, re.findall(r'\d+', move)))
    for _ in range(no_of_crates):
        stacks[dest - 1].append(stacks[src - 1].pop())

# Show crates at top of each stack after movement
print_top_of_stacks(stacks)
