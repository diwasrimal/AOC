from tools import empty_grid, print_grid


grid: list[list[int]] = []
with open("input.txt") as file:
    for row in file.read().splitlines():
        if not row: continue
        grid.append( list(map(int, [num for num in row])) )

X = len(grid)
Y = len(grid[0])

visible_left   = empty_grid(X, Y)
visible_right  = empty_grid(X, Y)
visible_top    = empty_grid(X, Y)
visible_bottom = empty_grid(X, Y)

# Find trees visible from left and right
for i in range(X):
    left_max_height   = -1
    right_max_height  = -1
    top_max_height    = -1
    bottom_max_height = -1

    for j in range(Y):

        # Tree is visible if it is longer than the longest tree (looking from left)
        if grid[i][j] > left_max_height:
            visible_left[i][j] = 1
            left_max_height = grid[i][j]

        # Tree is visible if it is longer than the longest tree (looking from right)
        if grid[i][Y - j - 1] > right_max_height:
            visible_right[i][Y - j - 1] = 1
            right_max_height = grid[i][Y - j - 1]

        # Tree is visible if it is longer than the longest tree (looking from top)
        if grid[j][i] > top_max_height:
            visible_top[j][i] = 1
            top_max_height = grid[j][i]

        # Tree is visible if it is longer than the longest tree (looking from bottom)
        if grid[Y - j - 1][i] > bottom_max_height:
            visible_bottom[Y - j - 1][i] = 1
            bottom_max_height = grid[Y - j - 1][i]

visible_trees = 0
for i in range(X):
    for j in range(Y):
        if visible_left[i][j] or visible_right[i][j] or visible_top[i][j] or visible_bottom[i][j]:
            visible_trees += 1

print(visible_trees)
