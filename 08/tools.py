def empty_grid(length, breadth):
    """Return a 2D list of length * breadth initialized with 0"""
    return [ [ 0 for _ in range(length) ] for _ in range(breadth) ]

def print_grid(grid, desc="Grid"):
    print(desc)
    for i in range(len(grid)):
        print(grid[i])
