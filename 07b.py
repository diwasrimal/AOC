class Directory():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"[{self.name}, {self.size}]"


# Pops the current directory from stack adding its size to its parent
# Used in '$ cd ..'
def pop_dir_stack(dir_stack):
    popped_dir = dir_stack.pop()
    stack[-1].size += popped_dir.size
    return popped_dir


# Get the command line usage log
with open("input/07.txt") as file:
    commands = file.read().splitlines()

# Root dir initialized with size 0
stack = [ Directory('/', 0) ]
sizes = []

for cmd in commands:
    if not cmd or cmd == "$ cd /" or cmd == "$ ls" or cmd.startswith('dir'):
        continue

    if cmd.startswith('$ cd '):
        dir_name = cmd.split()[-1]

        # Coming one level back, pop the stack in this case
        if dir_name == '..':
            popped_dir = pop_dir_stack(stack)
            sizes.append(popped_dir.size)

        else:
            stack.append( Directory(dir_name, 0) )

    # Collect files of our current directory
    else:
        filesize, _ = cmd.split()
        stack[-1].size += int(filesize)

# Come back to root
while True:
    if len(stack) == 1: break
    popped_dir = pop_dir_stack(stack)
    sizes.append(popped_dir.size)

total_size = 70000000
update_size = 30000000

print("Stack: {}".format(stack))

root = stack[-1]
free_size = total_size - root.size
smallest_size = root.size
for size in sizes:
    if size + free_size >= update_size and size < smallest_size:
        smallest_size = size

print(smallest_size)
