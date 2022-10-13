class Tournament:
    def __init__(self, name, location, date, teams, judges, rounds, speakers, results):
        self.name = name
        self.location = location
        self.date = date
        self.teams = teams
        self.judges = judges
        self.rounds = rounds
        self.speakers = speakers
        self.results = results
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

class Round:
    def __init__(self, num, debates, elim=False):
        self.num = num
        self.debates = debates
        self.elim = elim
    def __repr__(self):
        return f"Round {self.num}"
    def __str__(self):
        return f"Round {self.num}"

class Debate:
    def __init__(self, code, aff, neg, judge, room, winner):
        self.code = code
        self.aff = aff
        self.neg = neg
        self.judge = judge
        self.room = room
        self.winner = winner
    def __repr__(self):
        return f"{self.aff} vs {self.neg}"
    def __str__(self):
        return f"{self.aff} vs {self.neg}"

class Location:
    def __init__(self, name, address, rooms):
        self.name = name
        self.address = address
        self.rooms = rooms
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

class School:
    def __init__(self, name, teams, debaters, coaches, judges):
        self.name = name
        self.teams = teams
        self.debaters = debaters
        self.coaches = coaches
        self.judges = judges
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

class Team:
    def __init__(self, code, a2, n2, school, wins, losses, speaks):
        self.code = code
        self.a2 = a2
        self.n2 = n2
        self.school = school
        self.wins = wins
        self.losses = losses
        self.speaks = speaks
    def __repr__(self):
        return self.code
    def __str__(self):
        return self.code

class Debater:
    def __init__(self, name, speaks):
        self.name = name
        self.speaks = speaks
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

class Judge:
    def __init__(self, name, school, rounds_in):
        self.name = name
        self.school = school
        self.rounds_in = rounds_in
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name