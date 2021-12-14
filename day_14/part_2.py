template = ""
rules = {}
with open("input.txt") as file:
    # first line is starting template
    template = file.readline().strip()
    next(file)
    while line := file.readline().strip():
        pair = line.split(" -> ")
        rules[pair[0]] = pair[1]

tally = {}
steps = 10

# setup
removes = {}
bits = []
for i in range(len(template)-1):
    bit = template[i:i+2]
    #print(" bit: ", bit)
    bits.append(bit)
    if i < len(template)-2:
        #print(" remove: ", bit[1])
        if bit[1] in removes:
            removes[bit[1]] = removes[bit[1]] + 1
        else:
            removes[bit[1]] = 1

for i, bit in enumerate(bits):
    tally[bit] = 1

print("template: ", template)
print("initial tally:", tally)
print("removes: ", removes)

# each step
for step in range(steps):
    #print("step:", step+1)
    bits = {}
    # first I'm making a copy of tally so I can iterate it while tally changes
    # (and removing the zero values)
    for bit in tally:
        if tally[bit] > 0: 
            bits[bit] = tally[bit]
    #print("bits:", bits)
    #print("tally:", tally)
    
    for bit in bits:
        bitcount = bits[bit]
        tally[bit] -= bitcount # remove the last round's pairs
        triplet = bit[0]+rules[bit]+bit[1] # generate the new pairs
        # log the "doubled" letter AA -> AB, BA : remove a B
        # BUG HERE
        # I'm taking off too many
        if rules[bit] in removes:
            removes[rules[bit]] += bitcount
        else:
            removes[rules[bit]] = bitcount
    
        p1 = triplet[0:2]
        p2 = triplet[1:]
        #print(bit)
        #print(" -> ", p1, p2)
        if p1 in tally:
            tally[p1] += bitcount
        else:
            tally[p1] = bitcount
        if p2 in tally:
            tally[p2] += bitcount
        else:
            tally[p2] = bitcount
        #print("  = ", tally)

print("final tally:",tally)
letters = {}
for bit in tally.keys():
    if tally[bit] > 0:
        if bit[0] in letters:
            letters[bit[0]] += tally[bit]
        else:
            letters[bit[0]] = tally[bit]
        if bit[1] in letters:
            letters[bit[1]] += tally[bit]
        else:
            letters[bit[1]] = tally[bit]

print("letters: ", letters)
for r in removes:
    letters[r] -= removes[r]
print(" after removing spares:", letters)

scores = sorted(list(letters.values()))
scores.reverse()
print("sorted scores:", scores)
# test scores:
# B: 1749, N: 865, C: 298, H:161 


print(scores[0] - scores[len(scores)-1])
exit()

#print("most common is: "+most+" with count: ", most_count)
#print("least common is: "+least+" with count: ", least_count)
#print(most_count - least_count)

