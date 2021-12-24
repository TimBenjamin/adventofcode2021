#start = 384615384616 # lowest number that produces 14-digit result
start = 427350427351 # lowest number that produces 14-digit result of 1's or more
start = 3846153846153 # highest number 
c = 1
while True:
    res = (26 * start)
    if len(str(res)) == 14:
        if "0" not in str(res):
            print(res, start)
    elif len(str(res)) != 14:
        print("len out of bounds: ", res, len(res))
        break
    break
    start -= 1
    