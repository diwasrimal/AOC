import re


# Stores scan data as [ ((sensor_x, sensor_y), (beacon_x, beacon_y)) ... ]
scan = []
with open("input.txt") as file:
    for line in file.read().splitlines():
        if not line: continue
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        scan.append( ((sx, sy), (bx, by)) )

