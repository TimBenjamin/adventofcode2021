import math

dirty_lookup = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}
with open("input.txt") as file:
    line = file.readline().strip()
binString = ""
hex = list(line)
for h in hex:
    binString += dirty_lookup[h]

pointer = 0

def analysePacket(binString, pointer):
    version = int(binString[pointer:pointer+3], 2)
    pointer += 3

    typeId = int(binString[pointer:pointer+3], 2)
    pointer += 3

    result = None # this will be a literal value if there is one

    print("version:", version)
    print("typeId:", typeId)
    if typeId == 4:
        # literal type
        # the binary number is padded with leading zeroes until its length is a multiple of four bits,
        # and then it is broken into groups of four bits.
        # Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit.
        literal = ""
        while True:
            bit = binString[pointer:pointer+5]
            literal += bit[1:]
            pointer += 5
            if bit[0] == "0":
                break
        result = int(literal, 2)
        print(" => Literal type, value:", result)
    else:
        # operator types
        # contain other packets
        lengthTypeId = binString[pointer]
        pointer += 1
        print(" => Operator type, lengthTypeId:", lengthTypeId)
        
        results = [] # store the outputs of the operator type sub-packets
        if lengthTypeId == "0":
            # next 15 bits are a number
            # that represents the total length in bits of all the sub-packets in this packet
            subPacketLength = int(binString[pointer:pointer+15], 2)
            pointer += 15
            print(" ==> subPacketLength:", subPacketLength)
            limit = pointer + subPacketLength
            while pointer < limit:
                print("--- Sub Packet ---")
                pointer, result = analysePacket(binString, pointer)
                results.append(result)
        elif lengthTypeId == "1":
            # next 11 bits are a number
            # that represents the number of sub-packets contained by this packet
            numSubPackets = int(binString[pointer:pointer+11], 2)
            pointer += 11
            print(" ==> numSubPackets:", numSubPackets)
            for _ in range(numSubPackets):
                print("--- Sub Packet ---")
                pointer, result = analysePacket(binString, pointer)
                results.append(result)
        if typeId == 0:
            result = sum(results)
        elif typeId == 1:
            result = math.prod(results)
        elif typeId == 2:
            result = min(results)
        elif typeId == 3:
            result = max(results)
        elif typeId == 5:
            if results[0] > results[1]:
                result = 1
            else:
                result = 0
        elif typeId == 6:
            if results[0] < results[1]:
                result = 1
            else:
                result = 0
        elif typeId == 7:
            if results[0] == results[1]:
                result = 1
            else:
                result = 0
    return pointer, result

while True:
    pointer, result = analysePacket(binString, pointer)
    print("Main loop, pointer is now:", pointer)
    print("Remainder is now:", binString[pointer:])
    if pointer == False or len(binString[pointer:]) == 0 or int(binString[pointer:], 2) == 0:
        print("Result:", result)
        print("End of transmission!")
        break
