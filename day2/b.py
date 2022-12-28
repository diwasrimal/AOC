from tools import Rock, Paper, Scissors


move = { "A": Rock, "B": Paper, "C": Scissors }
result = { "X": "lose", "Y": "draw", "Z": "win" }

points = 0
with open("input.txt") as file:
    for line in file:
        a, b = line.rstrip().split()
        their_move = move[a]()

        # Determine the outcome
        outcome = result[b]

        # Make move which gives the required outcome
        if outcome == "win":
            our_move = their_move.loses_against()
            points += 6 
        elif outcome == "lose":
            our_move = their_move.wins_against()
        else:
            our_move = their_move.draws_against()
            points += 3

        points += our_move.score


print(points)
