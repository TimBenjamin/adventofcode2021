distances = {
    ("A0","H0"): 3,
    ("A1","H0"): 4,
    ("A2","H0"): 5,
    ("A3","H0"): 6,
    ("A0","H1"): 2,
    ("A1","H1"): 3,
    ("A2","H1"): 4,
    ("A3","H1"): 5,
    ("A0","H3"): 2,
    ("A1","H3"): 3,
    ("A2","H3"): 4,
    ("A3","H3"): 5,
    ("A0","H5"): 4,
    ("A1","H5"): 5,
    ("A2","H5"): 6,
    ("A3","H5"): 7,
    ("A0","H7"): 6,
    ("A1","H7"): 7,
    ("A2","H7"): 8,
    ("A3","H7"): 9,
    ("A0","H9"): 8,
    ("A1","H9"): 9,
    ("A2","H9"): 10,
    ("A3","H9"): 11,
    ("A0","H10"): 9,
    ("A1","H10"): 10,
    ("A2","H10"): 11,
    ("A3","H10"): 12,

    ("B0","H0"): 5,
    ("B1","H0"): 6,
    ("B2","H0"): 7,
    ("B3","H0"): 8,
    ("B0","H1"): 4,
    ("B1","H1"): 5,
    ("B2","H1"): 6,
    ("B3","H1"): 7,
    ("B0","H3"): 2,
    ("B1","H3"): 3,
    ("B2","H3"): 4,
    ("B3","H3"): 5,
    ("B0","H5"): 2,
    ("B1","H5"): 3,
    ("B2","H5"): 4,
    ("B3","H5"): 5,
    ("B0","H7"): 4,
    ("B1","H7"): 5,
    ("B2","H7"): 6,
    ("B3","H7"): 7,
    ("B0","H9"): 6,
    ("B1","H9"): 7,
    ("B2","H9"): 8,
    ("B3","H9"): 9,
    ("B0","H10"): 7,
    ("B1","H10"): 8,
    ("B2","H10"): 9,
    ("B3","H10"): 10,

    ("C0","H0"): 7,
    ("C1","H0"): 8,
    ("C2","H0"): 9,
    ("C3","H0"): 10,
    ("C0","H1"): 6,
    ("C1","H1"): 7,
    ("C2","H1"): 8,
    ("C3","H1"): 9,
    ("C0","H3"): 4,
    ("C1","H3"): 5,
    ("C2","H3"): 6,
    ("C3","H3"): 7,
    ("C0","H5"): 2,
    ("C1","H5"): 3,
    ("C2","H5"): 4,
    ("C3","H5"): 5,
    ("C0","H7"): 2,
    ("C1","H7"): 3,
    ("C2","H7"): 4,
    ("C3","H7"): 5,
    ("C0","H9"): 4,
    ("C1","H9"): 5,
    ("C2","H9"): 6,
    ("C3","H9"): 7,
    ("C0","H10"): 5,
    ("C1","H10"): 6,
    ("C2","H10"): 7,
    ("C3","H10"): 8,

    ("D0","H0"): 9,
    ("D1","H0"): 10,
    ("D2","H0"): 11,
    ("D3","H0"): 12,
    ("D0","H1"): 8,
    ("D1","H1"): 9,
    ("D2","H1"): 10,
    ("D3","H1"): 11,
    ("D0","H3"): 6,
    ("D1","H3"): 7,
    ("D2","H3"): 8,
    ("D3","H3"): 9,
    ("D0","H5"): 4,
    ("D1","H5"): 5,
    ("D2","H5"): 6,
    ("D3","H5"): 7,
    ("D0","H7"): 2,
    ("D1","H7"): 3,
    ("D2","H7"): 4,
    ("D3","H7"): 5,
    ("D0","H9"): 2,
    ("D1","H9"): 3,
    ("D2","H9"): 4,
    ("D3","H9"): 5,
    ("D0","H10"): 3,
    ("D1","H10"): 4,
    ("D2","H10"): 5,
    ("D3","H10"): 6,
}

def getInitialState():
    return {
        "A0": "D",
        "A1": "D",
        "A2": "D",
        "A3": "D",
        "B0": "B",
        "B1": "C",
        "B2": "B",
        "B3": "A",
        "C0": "C",
        "C1": "B",
        "C2": "A",
        "C3": "D",
        "D0": "A",
        "D1": "A",
        "D2": "C",
        "D3": "C",
        "H0": ".",
        "H1": ".",
        "H3": ".",
        "H5": ".",
        "H7": ".",
        "H9": ".",
        "H10": ".",
    }

places = ["A0","A1","A2","A3","B0","B1","B2","B3","C0","C1","C2","C3","D0","D1","D2","D3","H0","H1","H3","H5","H7","H9","H10"]

costs = {
    "A":1,
    "B":10,
    "C":100,
    "D":1000
}

def visualise(state):
    global energy
    print("#############")
    print("#"+state["H0"]+state["H1"]+"."+state["H3"]+"."+state["H5"]+"."+state["H7"]+"."+state["H9"]+state["H10"]+"#")
    print("###"+state["A0"]+"#"+state["B0"]+"#"+state["C0"]+"#"+state["D0"]+"###")
    print("  #"+state["A1"]+"#"+state["B1"]+"#"+state["C1"]+"#"+state["D1"]+"#")
    print("  #"+state["A2"]+"#"+state["B2"]+"#"+state["C2"]+"#"+state["D2"]+"#")
    print("  #"+state["A3"]+"#"+state["B3"]+"#"+state["C3"]+"#"+state["D3"]+"#")
    print("  #########")
    print("Energy usage:", energy)
    print()

def isComplete(state):
    A = "".join([state["A0"],state["A1"],state["A2"],state["A3"]])
    B = "".join([state["B0"],state["B1"],state["B2"],state["B3"]])
    C = "".join([state["C0"],state["C1"],state["C2"],state["C3"]])
    D = "".join([state["D0"],state["D1"],state["D2"],state["D3"]])
    if A == "AAAA" and B == "BBBB" and C == "CCCC" and D == "DDDD":
        return True
    return False

def doMove(s, f, moves):
    global distances, state, places, energy, costs
    # s:C0 moves to f:H1
    state[f] = state[s]
    state[s] = "."
    if (f,s) in distances:
        d = distances[(f,s)]
    else:
        d = distances[(s,f)]
    cost = costs[state[f]] * d
    energy += cost
    moves.append([s,f])
    print(s + " moved to " + f + " at a cost of " + str(cost))
    return moves

def checkLegal(s, f):
    global state
    # can't move nothing:
    if state[s] == ".": return False
    # can't move to an occupied space:
    if state[f] != ".": return False
    # only the top one in a column can move:
    if s == "A1" and state["A0"] != ".": return False
    if s == "A2" and state["A1"] != ".": return False
    if s == "A3" and state["A2"] != ".": return False
    if s == "B1" and state["B0"] != ".": return False
    if s == "B2" and state["B1"] != ".": return False
    if s == "B3" and state["B2"] != ".": return False
    if s == "C1" and state["C0"] != ".": return False
    if s == "C2" and state["C1"] != ".": return False
    if s == "C3" and state["C2"] != ".": return False
    if s == "D1" and state["D0"] != ".": return False
    if s == "D2" and state["D1"] != ".": return False
    if s == "D3" and state["D2"] != ".": return False
    # no hall to hall moves allowed
    if s.startswith("H") and f.startswith("H"): return False
    # otherwise I can move into a hallway:
    if f.startswith("H"): return True
    # I can't move into a column that isn't my own:
    if state[s] == "A" and not f.startswith("A"): return False
    if state[s] == "B" and not f.startswith("B"): return False
    if state[s] == "C" and not f.startswith("C"): return False
    if state[s] == "D" and not f.startswith("D"): return False
    # from a column, I can only move into the hall:
    if (s.startswith("A") or s.startswith("B") or s.startswith("C") or s.startswith("D")) and not f.startswith("H"): return False
    # is there anything blocking my way into a hall location?
    if (s.startswith("A") or s.startswith("B") or s.startswith("C") or s.startswith("D")) and f.startswith("H"):
        if checkBlocked(s, f):
            return False
    # anything else is OK:
    return True

def checkBlocked(s, f):
    global state
    # s will be a column and f will be a hallway place
    assert((s.startswith("A") or s.startswith("B") or s.startswith("C") or s.startswith("D")) and f.startswith("H"))
    if s.startswith("A"):
        if f == "H0" and state["H1"] != ".": return False
        if f == "H5" and state["H3"] != ".": return False
        if f == "H7" and state["H3"] != "." and state["H5"] != ".": return False
        if f == "H9" and state["H3"] != "." and state["H5"] != "." and state["H7"] != ".": return False
        if f == "H10" and state["H3"] != "." and state["H5"] != "." and state["H7"] != "." and state["H9"] != ".": return False
    elif s.startswith("B"):
        if f == "H0" and state["H3"] != "." and state["H1"] != ".": return False
        if f == "H1" and state["H3"] != ".": return False
        if f == "H7" and state["H5"] != ".": return False
        if f == "H9" and state["H5"] != "." and state["H7"] != ".": return False
        if f == "H10" and state["H5"] != "." and state["H7"] != "." and state["H9"] != ".": return False
    elif s.startswith("C"):
        if f == "H0" and state["H5"] != "." and state["H3"] != "." and state["H1"] != ".": return False
        if f == "H1" and state["H5"] != "." and state["H3"] != ".": return False
        if f == "H3" and state["H5"] != ".": return False
        if f == "H9" and state["H7"] != ".": return False
        if f == "H10" and state["H7"] != "." and state["H9"] != ".": return False
    elif s.startswith("D"):
        if f == "H0" and state["H7"] != "." and state["H5"] != "." and state["H3"] != "." and state["H1"] != ".": return False
        if f == "H1" and state["H7"] != "." and state["H5"] != "." and state["H3"] != ".": return False
        if f == "H3" and state["H7"] != "." and state["H5"] != ".": return False
        if f == "H5" and state["H7"] != ".": return False
        if f == "H10" and state["H9"] != ".": return False
    return True

energy = 0
winningGames = []
numGames = 0
minEnergy = 1000000
while True:
    # not sure how to break out, so will limit the number of games for now
    if numGames == 4: break
    numGames += 1
    moves = []
    state = getInitialState()
    restart = False
    # BUG - this just runs the same game over and over...
    for s in places: # s = start, where we are moving from
        if restart: break
        for f in places: # f = finish, where we are moving to
            if s == f: continue
            if checkLegal(s,f):
                moves = doMove(s, f, moves)
                #visualise(state)
                if isComplete(state):
                    print("winning state found, total energy:", energy)
                    winningGames.append({
                        "moves":moves,
                        "energy":energy
                    })
                    if energy < minEnergy:
                        minEnergy = energy
                    restart = True
                    break
    # game finished but was not complete
    print("That game ended in gridlock! try another")
    


                
            