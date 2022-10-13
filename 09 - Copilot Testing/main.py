from classes import *
from random import choice, randint, uniform
import xlwt

def main():
    #create a new tournament
    tournament = Tournament(input("Tournament Name: "), Location("Building","123 Stupid Drive",[]), input("Date: "), [], [], [], [], [])

    firstnames = file_to_list("first_name.txt")
    lastnames = file_to_list("last_name.txt")
    schools = file_to_list("schools.txt")

    #let user create a certain amount of schools
    for i in range(int(input("How many schools are attending? "))):
        #create a new school
        #assign a random school name from schools to name
        name = schools[randint(0,len(schools)-1)]
        school = School(name, [], [], [], [])
        schools.remove(school.name)
        #let user create a certain amount of teams
        for j in range(randint(3,9)):
            #create two debaters
            a2 = Debater(f"{firstnames[randint(0,len(firstnames)-1)]} {lastnames[randint(0,len(lastnames)-1)]}",[])
            n2 = Debater(f"{firstnames[randint(0,len(firstnames)-1)]} {lastnames[randint(0,len(lastnames)-1)]}",[])
            #create a new team
            team = Team(f"{school.name} {a2.name.split()[1][0]}{n2.name.split()[1][0]}", a2, n2, school, 0, 0, [])
            #add team to school
            school.teams.append(team)
            #add team to tournament
            tournament.teams.append(team)
        #let user create a certain amount of judges
        for i in range(randint(1,7)):
            #create a new judge
            judge = Judge(f"{firstnames[randint(0,len(firstnames)-1)]} {lastnames[randint(0,len(lastnames)-1)]}", school, randint(0,6))
            #add judge to school
            school.judges.append(judge)
            #add judge to tournament
            tournament.judges.append(judge)
    
    #let the user add hired judges
    for i in range(int(input("How many hired judges are attending? "))):
        #create a new judge
        judge = Judge(f"{firstnames[randint(0,len(firstnames)-1)]} {lastnames[randint(0,len(lastnames)-1)]}", "Hired", randint(0,6))
        #add judge to tournament
        tournament.judges.append(judge)

    #ask user how many debates are preset?
    rounds = int(input("How many rounds are there? "))
    presets = int(input("How many rounds are preset? "))
    results = xlwt.Workbook()

    for i in range(rounds):
        create_round(i,presets,tournament.teams,tournament.judges,tournament)
        gen_results(i,tournament)
        gen_schematic(i,tournament,results)
    
def file_to_list(file):
    with open(file, "r") as f:
        return f.read().splitlines()

def create_round(num,preset,teams,judges,tournament):
    temp_judges = judges.copy()
    temp_teams = teams.copy()
    round = Round(num+1, [])

    for i in range(len(teams) // 2):
        if num < preset:
            #Randomly select an aff team
            aff = choice(temp_teams)
            temp_teams.remove(aff)

            #Randomly select a neg team if they are not the same school or team as the aff team
            neg = choice([team for team in temp_teams if team.school != aff.school])
            temp_teams.remove(neg)
        else:
            pass
    
        #Randomly select a judge that is not associated with either teams school
        judge = choice([judge for judge in temp_judges if judge.school != aff.school and judge.school != neg.school])
        temp_judges.remove(judge)

        #Substract one round from the judges rounds_in
        judge.rounds_in -= 1

        #Randomly select a room
        room = i + 1

        #Create a new debate
        debate = Debate(f"{aff.code} vs {neg.code}", aff, neg, judge, room, None)
        round.debates.append(debate)
    
    tournament.rounds.append(round)

def gen_results(round,tournament):
    #randomly select a winner for each debate
    for debate in tournament.rounds[round].debates:
        debate.winner = choice([debate.aff, debate.neg])

        #add a win to the winner
        debate.winner.wins += 1
        #add a loss to the loser
        if debate.winner == debate.aff:
            debate.neg.losses += 1
        else:
            debate.aff.losses += 1

        #set speaks for each debater
        debate.aff.a2.speaks.append(uniform(27,30))
        debate.aff.n2.speaks.append(uniform(27,30))
        debate.neg.a2.speaks.append(uniform(27,30))
        debate.neg.n2.speaks.append(uniform(27,30))

        debate.aff.speaks.append((debate.aff.a2.speaks[-1] + debate.aff.n2.speaks[-1]) / 2)
        debate.neg.speaks.append((debate.neg.a2.speaks[-1] + debate.neg.n2.speaks[-1]) / 2)

def gen_schematic(round,tournament,results):
    page = results.add_sheet(f"Round {round+1}")
    page.write(0,0,"Room")
    page.write(0,1,"Aff")
    page.write(0,2,"Neg")
    page.write(0,3,"Judge")
    page.write(0,4,"Winner")

    for i in range(len(round.debates)):
        page.write(i+1,0,round.debates[i].room)
        page.write(i+1,1,round.debates[i].aff.code)
        page.write(i+1,2,round.debates[i].neg.code)
        page.write(i+1,3,round.debates[i].judge.name)
        page.write(i+1,4,round.debates[i].winner.code)
    
    results.save("results.xls")

if __name__ == "__main__":
    main()