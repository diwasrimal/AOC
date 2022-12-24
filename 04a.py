# Different sections of camp are to be cleaned.
# Each section has its own unique ID number
# Each elf is assigned a range of section IDs

# Return completely completely overlapping sections.

import re

def is_subset(a, b):
    """Check if list a is a subset of list b"""
    for item in a:
        if item not in b:
            return False
    return True

complete_overlappings = 0
with open("input/04.txt") as file:
    for line in file:
        line = line.rstrip()
        if matches:= re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line):
            ranges = [ int(digit) for digit in matches.groups() ]
            section1 = range(ranges[0], ranges[1] + 1)
            section2 = range(ranges[2], ranges[3] + 1)
            # print(f"Checking section {section1} and {section2}")
            if is_subset(section1, section2) or is_subset(section2, section1):
                # print("Overlapping")
                complete_overlappings += 1

print(complete_overlappings)

