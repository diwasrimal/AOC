class Crt():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = [ [ '.' for _ in range(width) ] for _ in range(height) ]

    def update(self, cycle, x):
        """Checks if pixel drawn by the crt during the given cycle overlaps with
        the pixels of sprite, and updates the crt's screen accordingly"""

        # If crt.width == 40
        # Cycle 1 -> # ... # <- Cycle 40
        # Index      0 ... 39
        crt_pixel_pos = (cycle - 1) % self.width

        # if x = 3, sprite = ..[###].....
        # index              01[234]5 ..
        sprite_pixels_positions = [ pos for pos in range(x-1, x+2) ]

        # Update crt's pixel from '.' to '#' if overlapping
        overlapping = any(pos == crt_pixel_pos for pos in sprite_pixels_positions)
        if overlapping:
            row = (cycle - 1) // self.width    # cycle 40 draws on row 0, while 41 on 1
            self.screen[row][crt_pixel_pos] = '#'

    def print(self):
        for row in self.screen:
            print(''.join(row))
        print()


data = []

with open("input.txt") as file:
    for line in file.read().splitlines():
        if not line: continue
        data.append(line)
