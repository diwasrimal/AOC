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

