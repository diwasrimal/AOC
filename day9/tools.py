class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, units):
        match direction:
            case 'L': return Point(self.x, self.y - units)
            case 'R': return Point(self.x, self.y + units)
            case 'U': return Point(self.x - units, self.y)
            case 'D': return Point(self.x + units, self.y)
            case _: raise ValueError("Invalid movement direction")

    def is_adjacent_to(self, point):
        """Checks if current point is adjacent to the given point"""
        for i in range(self.x-1, (self.x+1) + 1):
            for j in range(self.y-1, (self.y+1) + 1):
                if point.x == i and point.y == j:
                    return True
        return False

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


def follow_point(source, target):
    """Follows a non-adjacent target, returning new point adjacent to target"""
    new_x = target.x
    if target.x < source.x:  new_x = (source.x - 1)
    if target.x > source.x:  new_x = (source.x + 1)

    new_y = target.y
    if target.y < source.y:  new_y = (source.y - 1)
    if target.y > source.y:  new_y = (source.y + 1)

    return Point(new_x, new_y)


def print_grid(grid, desc="Grid"):
    print(desc)
    for i in range(len(grid)):
        print(grid[i])


moves: list[tuple[str, int]] = []

with open("input.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        if not line: continue
        direction, distance = line.split()
        moves.append( (direction, int(distance)) )
