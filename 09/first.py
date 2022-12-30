from tools import Point, moves, follow_point, print_grid


visited = []
visit_count = 0

# Arbitrary starting index
head = Point(0, 0)
tail = Point(0, 0)

for direction, distance in moves:
    for _ in range(distance):

        # Move head 
        head = head.move(direction, units=1)

        # If head remains adjacent to tail after the move, the tail doesnot move.
        # But, if the head moves such that it doesnot remain adjacent to tail anymore,
        # tail follows head
        if not tail.is_adjacent_to(head):
            tail = follow_point(tail, head)

        if not (tail.x, tail.y) in visited:
            visited.append( (tail.x, tail.y) )
            visit_count += 1

print(visit_count)

