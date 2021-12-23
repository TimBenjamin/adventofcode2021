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
        "A3": "C",
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
        "D3": "B",
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
    print("#############")
    print("#"+state["H0"]+state["H1"]+"."+state["H3"]+"."+state["H5"]+"."+state["H7"]+"."+state["H9"]+state["H10"]+"#")
    print("###"+state["A0"]+"#"+state["B0"]+"#"+state["C0"]+"#"+state["D0"]+"###")
    print("  #"+state["A1"]+"#"+state["B1"]+"#"+state["C1"]+"#"+state["D1"]+"#")
    print("  #"+state["A2"]+"#"+state["B2"]+"#"+state["C2"]+"#"+state["D2"]+"#")
    print("  #"+state["A3"]+"#"+state["B3"]+"#"+state["C3"]+"#"+state["D3"]+"#")
    print("  #########")
    print()

def isComplete(state):
    A = "".join([state["A0"],state["A1"],state["A2"],state["A3"]])
    B = "".join([state["B0"],state["B1"],state["B2"],state["B3"]])
    C = "".join([state["C0"],state["C1"],state["C2"],state["C3"]])
    D = "".join([state["D0"],state["D1"],state["D2"],state["D3"]])
    if A == "AAAA" and B == "BBBB" and C == "CCCC" and D == "DDDD":
        return True
    return False

def doMove(s, f, moves, energy, state):
    global distances, places, costs
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
    print(s + "(" + state[f] + ") moved to " + f + " at a cost of " + str(cost))
    return moves, energy

def checkLegal(s, f, state):
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
    # I can't move into a column that isn't my own:
    if state[s] == "A" and not f.startswith("A") and not f.startswith("H"): return False
    if state[s] == "B" and not f.startswith("B") and not f.startswith("H"): return False
    if state[s] == "C" and not f.startswith("C") and not f.startswith("H"): return False
    if state[s] == "D" and not f.startswith("D") and not f.startswith("H"): return False
    # from a column, I can only move into the hall:
    if (s.startswith("A") or s.startswith("B") or s.startswith("C") or s.startswith("D")) and not f.startswith("H"): return False
    # is there anything blocking my way into a hall location?
    if (s.startswith("A") or s.startswith("B") or s.startswith("C") or s.startswith("D")) and f.startswith("H"):
        if blocked(s, f, state):
            return False
    # am I in a hall location, trying to move to my column, is there anything in the way? (already prevented H to H moves)
    if s.startswith("H"):
        print("try hallblocked for: ", s, f)
        if hallBlocked(s,f,state):
            return False
    # if I'm an A and I'm in the A column and there is nothing below me that's not an A, stay put
    if s.startswith("A") and state[s] == "A" and state["A0"] == "A" and (state["A1"] == "A" or state["A1"] == ".") and (state["A2"] == "A" or state["A2"] == ".") and (state["A3"] == "A" or state["A3"] == "."): return False
    if s.startswith("B") and state[s] == "B" and state["B0"] == "B" and (state["B1"] == "B" or state["B1"] == ".") and (state["B2"] == "B" or state["B2"] == ".") and (state["B3"] == "B" or state["B3"] == "."): return False
    if s.startswith("C") and state[s] == "C" and state["C0"] == "C" and (state["C1"] == "C" or state["C1"] == ".") and (state["C2"] == "C" or state["C2"] == ".") and (state["C3"] == "C" or state["C3"] == "."): return False
    if s.startswith("D") and state[s] == "D" and state["D0"] == "D" and (state["D1"] == "D" or state["D1"] == ".") and (state["D2"] == "D" or state["D2"] == ".") and (state["D3"] == "D" or state["D3"] == "."): return False
    # anything else is OK:
    return True

def hallBlocked(s, f, state):
    # like blocked() but starting with hallway places
    assert(s.startswith("H"))
    # end of hall blocked:
    if s == "H0" and state["H1"] != ".": return True # H0 is blocked
    if s == "H10" and state["H9"] != ".": return True # H10 is blocked
    # if we're just above the room we're going into:
    if (s == "H0" or s == "H1" or s == "H3") and f.startswith("A"): return False # OK
    if (s == "H3" or s == "H5") and f.startswith("B"): return False # OK
    if (s == "H5" or s == "H7") and f.startswith("C"): return False # OK
    if (s == "H7" or s == "H9" or s == "H10") and f.startswith("D"): return False # OK
    # cases where a clear hall is needed:
    if (s == "H0" or s == "H1") and f.startswith("B") and state["H3"] != ".": return True
    if (s == "H0" or s == "H1") and f.startswith("C") and (state["H3"] != "." or state["H5"] != "."): return True
    if (s == "H0" or s == "H1") and f.startswith("D") and (state["H3"] != "." or state["H5"] != "." or state["H7"] != "."): return True # blocked
    if s == "H3" and f.startswith("C") and state["H5"] != ".": return True # H5 blocked
    if s == "H3" and f.startswith("D") and (state["H5"] != "." or state["H7"] != "."): return True # H5 or H7 blocked
    if s == "H5" and f.startswith("A") and state["H3"] != ".": return True # H3 blocked
    if s == "H5" and f.startswith("D") and state["H7"] != ".": return True # H7 blocked
    if s == "H7" and f.startswith("A") and (state["H5"] != "." or state["H3"] != "."): return True # H3 or H5 blocked
    if s == "H7" and f.startswith("B") and state["H5"] != ".": return True # H5 blocked
    if (s == "H9" or s == "H10") and f.startswith("A") and (state["H7"] != "." or state["H5"] != "." or state["H3"] != "."): return True
    if (s == "H9" or s == "H10") and f.startswith("B") and (state["H7"] != "." or state["H5"] != "."): return True
    if (s == "H9" or s == "H10") and f.startswith("C") and state["H7"] != ".": return True # H7 blocked
    return False # OK

def blocked(s, f, state):
    # s will be a column and f will be a hallway place
    assert((s.startswith("A") or s.startswith("B") or s.startswith("C") or s.startswith("D")) and f.startswith("H"))
    if s.startswith("A"):
        if f == "H0" and state["H1"] != ".": return True
        elif f == "H5" and state["H3"] != ".": return True
        elif f == "H7" and (state["H3"] != "." or state["H5"] != "."): return True
        elif f == "H9" and (state["H3"] != "." or state["H5"] != "." or state["H7"] != "."): return True
        elif f == "H10" and (state["H3"] != "." or state["H5"] != "." or state["H7"] != "." or state["H9"] != "."): return True
    elif s.startswith("B"):
        if f == "H0" and (state["H3"] != "." or state["H1"] != "."): return True
        elif f == "H1" and state["H3"] != ".": return True
        elif f == "H7" and state["H5"] != ".": return True
        elif f == "H9" and (state["H5"] != "." or state["H7"] != "."): return True
        elif f == "H10" and (state["H5"] != "." or state["H7"] != "." or state["H9"] != "."): return True
    elif s.startswith("C"):
        if f == "H0" and (state["H5"] != "." or state["H3"] != "." or state["H1"] != "."): return True
        elif f == "H1" and (state["H5"] != "." or state["H3"] != "."): return True
        elif f == "H3" and state["H5"] != ".": return True
        elif f == "H9" and state["H7"] != ".": return True
        elif f == "H10" and (state["H7"] != "." or state["H9"] != "."): return True
    elif s.startswith("D"):
        if f == "H0" and (state["H7"] != "." or state["H5"] != "." or state["H3"] != "." or state["H1"] != "."): return True
        elif f == "H1" and (state["H7"] != "." or state["H5"] != "." or state["H3"] != "."): return True
        elif f == "H3" and (state["H7"] != "." or state["H5"] != "."): return True
        elif f == "H5" and state["H7"] != ".": return True
        elif f == "H10" and state["H9"] != ".": return True
    return False

def playGame(moves, energy, state):
    global winningGames, places, minEnergy
    # BUG - this just runs the same game over and over...
    while True:
        moved = False
        for s in places: # s = start, where we are moving from
            for f in places: # f = finish, where we are moving to
                if s == f: continue
                # speed optimisation - if energy is already over minEnergy, don't bother carrying on!
                # if energy > minEnergy:
                #     print("energy is already too high")
                #     return False
                if checkLegal(s, f, state):
                    moved = True
                    moves, energy = doMove(s, f, moves, energy, state)
                    #visualise(state)
                    if isComplete(state):
                        print("winning state found, total energy:", energy)
                        winningGames.append({
                            "moves": moves,
                            "energy": energy
                        })
                        if energy < minEnergy:
                            minEnergy = energy
                        return True
                else:
                    moved = False
            print(s + "(" + state[s] + ") cannot move")
        
        if not moved:
            # game finished but was not complete
            visualise(state)
            print("That game ended in gridlock! try another")
            return False

winningGames = []
numGames = 0
minEnergy = 1000000
moves = []
energy = 0
state = getInitialState()
result = playGame(moves, energy, state)
print(minEnergy)
    


                
            