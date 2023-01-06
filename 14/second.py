from tools import is_rock, lowest_rock_y

# Boolean matrix to keep track of filled tiles
is_filled: list[list[bool]] = [ [ False for _ in range(1000) ] for _ in range(1000) ]

# Add rocks on the floor
floor_y = lowest_rock_y + 2
for i in range(0, 1000):
    is_rock[i][floor_y] = True


def can_be_filled(point: tuple[int, int]):
    x, y = point
    if is_filled[x][y] or is_rock[x][y]:
        return False
    return True


def pour(source: tuple[int, int]) -> bool:
    """Pours sand from source, returning True for a successful pour"""
    global is_filled
    x, y = source
    x_idxs = [-1, 0, 1]
    left, bottom, right = [ (x+i, y+1) for i in x_idxs ]

    # Try filling the bottom tile first
    if can_be_filled(bottom): 
        return pour(bottom)

    # Else try filling the left tile
    elif can_be_filled(left):
        return pour(left)

    # Else the right one
    elif can_be_filled(right):
        return pour(right)

    # Else try filling current tile
    elif can_be_filled(source):
        print(f"filling {source}")
        is_filled[x][y] = True
        return True

    # Nothing can left to fill, source is blocked
    else:
        return False


# Keep pouring sand from source until unsuccessful pour
sand_source = (500, 0)
fill_count = 0
while pour(sand_source): 
    fill_count += 1

print(fill_count)
