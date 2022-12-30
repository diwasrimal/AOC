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
    dir_stack[-1].size += popped_dir.size
    return popped_dir

