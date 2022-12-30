# Return overlapping sections

import re

def are_overlapping(a, b):
    """Check if two lists have at least one common item (are overlapping simply)"""
    for item in a:
        if item in b:
            return True
    return False

overlappings = 0
with open("input.txt") as file:
    for line in file:
        line = line.rstrip()
        if matches:= re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line):
            ranges = [ int(digit) for digit in matches.groups() ]
            section1 = range(ranges[0], ranges[1] + 1)
            section2 = range(ranges[2], ranges[3] + 1)
            # print(f"Checking section {section1} and {section2}")
            if are_overlapping(section1, section2) or are_overlapping(section2, section1):
                # print("Overlapping")
                overlappings += 1

print(overlappings)



