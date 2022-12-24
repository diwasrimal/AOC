class Rock():
    def __init__(self):
        self.wins_against = Scissors
        self.loses_against = Paper
        self.draws_against = Rock
        self.score = 1

class Paper():
    def __init__(self):
        self.wins_against = Rock
        self.loses_against = Scissors
        self.draws_against = Paper
        self.score = 2

class Scissors():
    def __init__(self):
        self.wins_against = Paper
        self.loses_against = Rock
        self.draws_against = Scissors
        self.score = 3

move = { "A": Rock, "B": Paper, "C": Scissors }
result = { "X": "lose", "Y": "draw", "Z": "win" }

points = 0
with open("input/02.txt") as file:
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
