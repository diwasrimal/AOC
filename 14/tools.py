# Boolean matrix that stores rocks 
is_rock: list[list[bool]] = [ [ False for _ in range(1000) ] for _ in range(1000) ]

# Lowest positon of rock. If sand touches this tile, it goes into endless void
lowest_rock_y: int = 0

with open("input.txt") as file:
    for line in file.read().splitlines():

        if not line: continue
        last = None
        points = line.split(' -> ')
        for point in points:

            # Get x and y coordinates of curr point and join it with last point
            x, y = map(int, point.split(','))

            if last is None:
                last = (x, y)
                continue

            # Collect points joining last point and current point
            lx, ly = last

            # 498, [4]  last point
            # 498, ...
            # 498, [6]
            if lx == x:
                new_y_coords = range(ly, y) if y > ly else range(ly, y, -1)
                for j in new_y_coords:
                    is_rock[x][j] = True
                    if j > lowest_rock_y: 
                        lowest_rock_y = j
                
            # [496], 6   ..., 6    [498], 6 
            #                      last point
            if ly == y:
                new_x_coords = range(lx, x) if x > lx else range(lx, x, -1)
                for i in new_x_coords:
                    is_rock[i][y] = True

            # Mark the current point as last point
            last = (x, y)

        # Mark the last rock (end point of rock line) as rock
        if last is not None:
            ex, ey = last
            is_rock[ex][ey] = True
            if ey > lowest_rock_y:
                lowest_rock_y = ey
