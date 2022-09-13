def main():
    file = open(input("Input Filename: "),"r")
    temp = 0
    results = []

    for line in file:
        if temp == 0:
            temp += 1
        else:
            results.append(line.split(","))

    file.close()

    debaters = []

    for debater in results:
        times = []
        prefs = []

        for x in range(0,len(debater) - 14):
            times.append(debater[x + 2].strip())
        
        for x in range(len(debater) - 8, len(debater) - 4):
            prefs.append(int(debater[x]))
        
        debaters.append(Debater(debater[1],times,debater[len(times) + 2],debater[len(times) + 3],debater[len(times) + 4],debater[len(times) + 5],prefs))
    
    output = open("debaters.txt","w")

    for debater in debaters:
        output.write(str(debater))
        output.write(str(debater))
    
    output.close()

class Debater:
    def __init__(self,name,timeslots,amt_rounds,aff,negvpol,negvk,prefs):
        self.name = name
        self.amt = amt_rounds
        self.slots = ""
        self.prefs = ""

        if aff == "Plan":
            self.aff_strat = "Policy"
        else:
            self.aff_strat = "K"
        
        if negvpol == "Policy":
            self.neg_strat = "Policy vs. Policy Affs"
        else:
            self.neg_strat = "K vs. Policy Affs"

        if negvk == "T-USFG":
            self.neg_k_strat = "T-USFG vs. K Affs"
        else:
            self.neg_k_strat = "K vs. K Affs"
        
        for x in range(0,len(timeslots)):
            if x != len(timeslots) - 1:
                self.slots += f"{timeslots[x]}, "
            else:
                self.slots += f"{timeslots[x]}"

        for x in range(0,len(prefs)):
            if prefs[x] == 1:
                self.prefs += f"{x + 1}.) Aff, with a Plan, Versus Policy Neg.\n"
            elif prefs[x] == 2:
                self.prefs += f"{x + 1}.) Aff, with a Plan, Versus a K.\n"
            elif prefs[x] == 3:
                self.prefs += f"{x + 1}.) Aff, without a Plan, Versus T-USFG.\n"
            elif prefs[x] == 4:
                self.prefs += f"{x + 1}.) Aff, without a Plan, Versus a K.\n"
            elif prefs[x] == 5:
                self.prefs += f"{x + 1}.) Neg, Policy Strat, versus Policy Aff.\n"
            elif prefs[x] == 6:
                self.prefs += f"{x + 1}.) Neg, K Strat, versus Policy Aff.\n"
            elif prefs[x] == 7:
                self.prefs += f"{x + 1}.) Neg, T-USFG, versus K Aff.\n"
            elif prefs[x] == 8:
                self.prefs += f"{x + 1}.) Neg, K Strat, versus K Aff.\n"
        
    def __repr__(self):
        return f"{self.name}\nAvailable for {self.amt} of the following: {self.slots}\nStrat on the Aff: {self.aff_strat}\nStrat on the Neg: {self.neg_strat}, {self.neg_k_strat}\nPreferences:\n{self.prefs}\n"

if __name__ == "__main__":
    main()