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
