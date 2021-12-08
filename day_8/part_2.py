#    0:      1:      2:      3:      4:
#   aaaa    ....    aaaa    aaaa    ....
#  b    c  .    c  .    c  .    c  b    c
#  b    c  .    c  .    c  .    c  b    c
#   ....    ....    dddd    dddd    dddd
#  e    f  .    f  e    .  .    f  .    f
#  e    f  .    f  e    .  .    f  .    f
#   gggg    ....    gggg    gggg    ....
#
#    5:      6:      7:      8:      9:
#   aaaa    aaaa    aaaa    aaaa    aaaa
#  b    .  b    .  .    c  b    c  b    c
#  b    .  b    .  .    c  b    c  b    c
#   dddd    dddd    ....    dddd    dddd
#  .    f  e    f  .    f  e    f  .    f
#  .    f  e    f  .    f  e    f  .    f
#   gggg    gggg    ....    gggg    gggg

#correct_digits = {
#    0: "abcefg", # len: 6
#    1: "cf", # len: 2 <<
#    2: "acdeg", # len: 5
#    3: "acdfg", # len: 5
#    4: "bcdf", # len: 4 <<
#    5: "abdfg", # len: 5
#    6: "abdefg", # len: 6
#    7: "acf", # len: 3 <<
#    8: "abcdefg", # len: 7 <<
#    9: "abcdfg" # len: 6
#}

total = 0
with open("input.txt") as file:
    while line := file.readline().rstrip():
        signals, output = line.split(" | ")
        signals = signals.split(" ")
        output = output.split(" ")
        # these are jumbled, easier if they are alphabetical
        for s in range(len(signals)):
            segments = sorted(set(signals[s]))
            signals[s] = "".join(segments)
        for o in range(len(output)):
            segments = sorted(set(output[o]))
            output[o] = "".join(segments)
        
        decoded = {}

        for signal in signals:
            segments = sorted(set(signal))
            l = len(segments)
            if l == 2:
                decoded[1] = "".join(segments)
            elif l == 4:
                decoded[4] = "".join(segments)
            elif l == 3:
                decoded[7] = "".join(segments)
            elif l == 7:
                decoded[8] = "".join(segments)

        # of the len=5 [2,3,5], only 3 has both c and f
        cf = set(decoded[1])
        for signal in signals:
            if len(signal) == 5:
                segments = set(signal)
                if len(segments - cf) == 3:
                    decoded[3] = signal
                    break
        
        # 2 is the only char that does not have an f
        # 1 has a c and f
        candidates = []
        cf = decoded[1]
        for signal in signals:
            if cf[0] in signal:
                if cf[1] not in signal:
                    candidates.append(signal)
            if cf[1] in signal:
                if cf[0] not in signal:
                    candidates.append(signal)
        # the len6 one of candidates must be 6
        for c in candidates:
            if len(c) == 6:
                decoded[6] = c
                break
        # char in 6 but not in 5 is e
        for c in candidates:
            if len(c) == 5:
                if len(set(decoded[6]) - set(c)) == 1:
                    decoded[5] = c
                else:
                    decoded[2] = c
        
        # 0 has g, 9 has dg
        # 3 - 7 = dg
        candidates = set(signals) - set(decoded.values())
        dg = set(decoded[3]) - set(decoded[7])
        for c in candidates:
            if c != decoded[6]:
                if len(set(c) - dg) == 5:
                    decoded[0] = c
                else:
                    decoded[9] = c
        
        output_value = ""
        for o in output:
            for d in decoded:
                if decoded[d] == o:
                    output_value += str(d)
                    break
        total += int(output_value)
print(total)