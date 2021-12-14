
template = ""
rules = {}
tally = {}
with open("input.txt") as file:
    # first line is starting template
    template = file.readline().strip()
    next(file)
    while line := file.readline().strip():
        pair = line.split(" -> ")
        rules[pair[0]] = pair[1]
        tally[pair[1]] = 0

for x in list(template):
    tally[x] += 1

steps = 10
for step in range(steps):
    newTemplate = ""
    for i in range(len(template)-1):
        x = rules[template[i:i+2]]
        newTemplate += template[i] + x
        tally[x] += 1
    newTemplate += template[-1]
    template = newTemplate

print("After step "+str(step+1)+" template is length:", len(template))
least = list(tally.keys())[0]
most = list(tally.keys())[0]
least_count = list(tally.values())[0]
most_count = list(tally.values())[0]
for letter in tally:
    if tally[letter] < least_count:
        least_count = tally[letter]
        least = letter
    elif tally[letter] > most_count:
        most_count = tally[letter]
        most = letter

print("most common is: "+most+" with count: ", most_count)
print("least common is: "+least+" with count: ", least_count)
print(most_count - least_count)
