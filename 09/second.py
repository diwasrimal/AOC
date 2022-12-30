from tools import Point, moves, follow_point, print_grid


KNOTS = 10

visited = []
visit_count = 0

# Arbitrary starting index for all knots
knots = [ Point(0, 0) for _ in range(KNOTS) ]

for direction, distance in moves:
    for _ in range(distance):

        # Move head 
        knots[0] = knots[0].move(direction, units=1)

        # Move knots after head
        for i in range(1, KNOTS):
            prev_knot = knots[i - 1]

            # If current knot is adjacent to the previous knot, current knot will not move
            # Neither will the knots following the current knot
            if knots[i].is_adjacent_to(prev_knot): 
                break

            # Else the current knot will follow the previous knot
            else:
                knots[i] = follow_point(knots[i], prev_knot)

        # Update points visited by tail
        tail = knots[KNOTS - 1]
        if not (tail.x, tail.y) in visited:
            visited.append( (tail.x, tail.y) )
            visit_count += 1

print(visit_count)
