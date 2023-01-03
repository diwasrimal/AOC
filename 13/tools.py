def in_order(pair) -> int:
    """Check if a given pair is in right order"""
    left, right = pair
    if type(left) == type(right) == int:
        if left < right: return 1       # Are in order
        if left > right: return -1      # Not in order
        if left == right: return 0      # Skip

    # Convert both to list
    if not type(left) == list: left = [ left ]
    if not type(right) == list: right = [ right ]

    N = max(len(left), len(right))
    for i in range(N):
        try:
            a = left[i]
        except IndexError:
            return 1            # If left list runs out, right order
        try:
            b = right[i]
        except IndexError:
            return -1           # If right list runs out, wrong order
        result = in_order( (a, b) )
        if result == 0:
            continue
        return result

    # Loop ended but no correct order found
    return 0


pairs = []
with open("input.txt") as file:
    for pair in file.read().split('\n\n'):
        if not pair: continue
        left, right = map(eval, pair.split('\n'))
        pairs.append((left, right))
