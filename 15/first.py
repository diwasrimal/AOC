from tools import scan


def points_on_line_with_manhattan(point: tuple[int, int], manhattan, a) -> list[tuple[int, int]]:
    """Returns points on line y=a that are given manhattan distance away from given point"""

    # Check the perpendicular distance
    x, y = point
    distance = abs(y - a)
    if manhattan < distance:
        return []
    if manhattan > distance:
        extra_distance = manhattan - distance
        return [ (x-extra_distance, a), (x+extra_distance, a) ]
    return [ (x, a) ]


Y = 2000000
not_beacons = set()

# Collect points that lie on line y=Y which aren't beacons
# Points that are 'manhattan' away or less from sensors
for sensor, beacon in scan:
    manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    while True:
        points = points_on_line_with_manhattan(sensor, manhattan, Y)
        if not points: break
        for point in points:
            if point == beacon: continue
            not_beacons.add(point)
        manhattan -= 1

print(len(not_beacons))

