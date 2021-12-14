template = ""
rules = {}
with open("input.txt") as file:
    # first line is starting template
    template = file.readline().strip()
    next(file)
    while line := file.readline().strip():
        pair = line.split(" -> ")
        rules[pair[0]] = pair[1]

#print("initial template:", template)

adds = {} # will contain the letters that are going to be added, plus the initial letters
# starting with the template:
for t in list(template):
    if t in adds:
        adds[t] += 1
    else:
        adds[t] = 1
#print("adds:", adds)

# set up the initial pairs for expansion
bits = []
for i in range(len(template)-1):
    bit = template[i:i+2]
    bits.append(bit)

# set up a tally of how many of each pair we have
tally = {}
for bit in bits:
    if bit in tally:
        tally[bit] += 1
    else:
        tally[bit] = 1

#print("template: ", template)
#print("initial tally:", tally)

# each step
steps = 40
for step in range(steps):
    #print("step:", step+1)
    bits = {}
    # "bits" is the dict of pairs from the last step's tally that are going to be expanded this round
    for bit in tally:
        bits[bit] = tally[bit]
    #print("bits:", bits)
    
    tally = {} # keep track of what pairs we are expanding this round
    for bit in bits:
        bitcount = bits[bit] # how many of this pair there are
        add = rules[bit]
        triplet = bit[0] + add + bit[1] # expand the pair, i.e. add a new letter to template
        
        # log the letter that we added:
        if add in adds:
            adds[add] += bitcount
        else:
            adds[add] = bitcount
    
        # record which pairs are now to be expanded next round
        p1 = triplet[0:2]
        p2 = triplet[1:]
        #print(bit)
        #print(" -> ", p1, p2, "x", bitcount)
        #print("adds", adds)
        if p1 in tally:
            tally[p1] += bitcount
        else:
            tally[p1] = bitcount
        if p2 in tally:
            tally[p2] += bitcount
        else:
            tally[p2] = bitcount
        #print("  = ", tally)

#print("adds:", adds)
scores = sorted(list(adds.values()))
scores.reverse()
#print("sorted scores:", scores)

print(scores[0] - scores[len(scores)-1])
