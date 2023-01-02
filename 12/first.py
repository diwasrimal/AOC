from tools import Point, Node, maze, is_movable

# Dimensions of maze
M = len(maze)
N = len(maze[0])

# Find start and endpoint of maze and update their elevations
start, end = Point(0,0), Point(0,0)
for i in range(M):
    for j in range(N):
        if maze[i][j] == 'S':
            start = Point(i, j)
            maze[i][j] = 'a'
        elif maze[i][j] == 'E':
            end = Point(i, j)
            maze[i][j] = 'z'

# We find the shortest path using breadth first search
# Initialze the queue with starting node having distance 0
queue: list[Node] = [ Node(start, 0) ]

# Make a visited array and mark the start as visited
visited = [ [ False for _ in range(N) ] for _ in range(M) ]
visited[start.x][start.y] = True

# These two arrays are used to find the position of 4 adjacent nodes
adj_x = [-1, 0, 0, 1]
adj_y = [0, -1, 1, 0]

while True:
    if not queue:
        print(f"Couldn't find suitable path from {start} to {end}.")
        break

    # Dequeue first node
    node = queue.pop(0)

    # Reached destination
    if node.pos.x == end.x and node.pos.y == end.y:
        print("Distance:", node.distance)
        break
    
    # Find four movable adjacent nodes
    movable = []
    for i in range(4):
        x = node.pos.x + adj_x[i]
        y = node.pos.y + adj_y[i]
        p = Point(x, y)
        if is_movable(node.pos, p, maze) and not visited[p.x][p.y]:
            visited[p.x][p.y] = True
            movable.append(Node(p, node.distance + 1))

    # Enqueue movable nodes
    queue.extend(movable)
