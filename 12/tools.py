class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

class Node():
    def __init__(self, pos: Point, distance: int):
        self.pos = pos
        self.distance = distance

    def __repr__(self):
        return f"[{self.pos} dist: {self.distance}]"


def is_movable(src: Point, dest: Point, maze: list[list[str]]):
    """Checks if moving from src to dest is valid."""

    # Point is out of bounds
    if not 0 <= dest.x < len(maze) or not 0 <= dest.y < len(maze[0]):
        return False

    # Point has invalid elevation
    if ord(maze[dest.x][dest.y]) > ord(maze[src.x][src.y]) + 1:
        return False

    return True

# Parse the maze into a two dimensinal array
maze: list[list[str]] = []
with open("input.txt") as file:
    for line in file.read().splitlines():
        if not line: break
        maze.append(list(line))

