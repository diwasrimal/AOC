from tools import Directory, pop_dir_stack

# Get the command line usage log
with open("input.txt") as file:
    commands = file.read().splitlines()

# Root dir initialized with size 0
stack = [ Directory('/', 0) ]

valid_size = 100000
valid_size_sum = 0

# The input is changing directories in depth-first manner
# We can push '<dir>' on to our stack everytime we see '$ cd <dir>' command
# And we can pop the current dir (top of stack) whenever we see '$ cd ..'
for cmd in commands:

    # We only care about lines starting with '$ cd' and lines with filesizes of current directory 
    if not cmd or cmd == "$ cd /" or cmd == "$ ls" or cmd.startswith('dir'):
        continue

    if cmd.startswith('$ cd '):
        dir_name = cmd.split()[-1]

        # Coming one level back, pop the stack in this case
        if dir_name == '..':
            popped_dir = pop_dir_stack(stack)
            if popped_dir.size <= valid_size:
                valid_size_sum += popped_dir.size

        # Else we push a new directory on to our stack
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
    if popped_dir.size <= valid_size:
        valid_size_sum += popped_dir.size

print(valid_size_sum)
