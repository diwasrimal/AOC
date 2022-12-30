from tools import Rock, Paper, Scissors


move = { "A": Rock, "B": Paper, "C": Scissors, "X": Rock, "Y": Paper, "Z": Scissors }

points = 0
with open("input.txt") as file:
    for line in file:

        # Find their and our moves
        a, b = line.rstrip().split()
        their_move, our_move = move[a](), move[b]()

        # A move's score is always added
        points += our_move.score

        # Win adds 6 points
        if our_move.wins_against == their_move.__class__:
            points += 6
        
        # Draw adds 6 points
        elif our_move.draws_against == their_move.__class__:
            points += 3

print(points)
