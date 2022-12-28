grid: list[list[int]] = []
with open("input.txt") as file:
    for row in file.read().splitlines():
        if not row: continue
        grid.append( list(map(int, [num for num in row])) )

X = len(grid)
Y = len(grid[0])

max_scenic_score = 0

for i in range(X):
    for j in range(Y):

        # NOTE: 
        # We'll always see one tree,
        # but if that tree's height >= height of the tree we're on (grid[i][j]),
        # all other trees won't be visible from our level

        # Suppose current elem is at index [2][2]

        # Score from left -> right
        # 2[2]  2[3] .. 2[Y]
        #  :)    :)      :(
        curr = j
        right = curr + 1
        score_right = 0
        while True:
            if right == Y: break
            score_right += 1                           
            if grid[i][right] >= grid[i][curr]: break  
            right += 1

        # Score from left <- right
        # 2[-1] .. 2[1]  2[2]
        #  :(       :)    :)
        curr = j
        left = curr - 1
        score_left = 0
        while True:
            if left == -1: break
            score_left += 1                           
            if grid[i][left] >= grid[i][curr]: break  
            left -= 1

        # Score from top -> bottom
        # [1]2 :)
        # [2]2 :)
        # .. 
        # [X]2 :(
        curr = i
        bottom = curr + 1
        score_bottom = 0
        while True:
            if bottom == X: break
            score_bottom += 1                       
            if grid[bottom][j] >= grid[curr][j]: break                               
            bottom += 1

        # Score from top <- bottom
        # [-1]2 :(
        # .. 
        # [1]2 :)
        # [2]2 :)
        curr = i
        top = i - 1
        score_top = 0
        while True:
            if top == -1: break
            score_top += 1
            if grid[top][j] >= grid[curr][j]: break
            top -= 1

        scenic_score = score_left * score_right * score_top * score_bottom
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)
