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
versionSum = 0

def analysePacket(binString, pointer):
    version = int(binString[pointer:pointer+3], 2)
    pointer += 3

    global versionSum
    versionSum += version

    typeId = int(binString[pointer:pointer+3], 2)
    pointer += 3

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
        literal = int(literal, 2)
        print(" => Literal type, value:", literal)
        # I think it will be zeroes after this, until the next 1 which is the start of another version (they begin with 1)
        print("remainder:", binString[pointer:])
        print("pointer is now:", pointer)
        print("length of string:", len(binString))
        #while binString[pointer] == "0":
        #    pointer += 1
        #    print("remainder:", binString[pointer:])
        #    print("pointer is now:", pointer)
        #    if pointer == len(binString):
        #        print("End of file!")
        #        return False
    else:
        # operator types
        # contain other packets
        lengthTypeId = binString[pointer]
        pointer += 1
        print(" => Operator type, lengthTypeId:", lengthTypeId)
        if lengthTypeId == "0":
            # next 15 bits are a number
            # that represents the total length in bits of all the sub-packets in this packet
            subPacketLength = int(binString[pointer:pointer+15], 2)
            pointer += 15
            print(" ==> subPacketLength:", subPacketLength)
            print("current pointer:", pointer)
            limit = pointer + subPacketLength
            while pointer < limit:
                print("--- Sub Packet ---")
                pointer = analysePacket(binString, pointer)
                print("Pointer is now:", pointer)
        elif lengthTypeId == "1":
            # next 11 bits are a number
            # that represents the number of sub-packets contained by this packet
            numSubPackets = int(binString[pointer:pointer+11], 2)
            pointer += 11
            print(" ==> numSubPackets:", numSubPackets)
            for _ in range(numSubPackets):
                print("--- Sub Packet ---")
                pointer = analysePacket(binString, pointer)
                print("doing subpackets, pointer is now:", pointer)
        # is there padding here?
    return pointer

while True:
    pointer = analysePacket(binString, pointer)
    print("Main loop, pointer is now:", pointer)
    print("Remainder is now:", binString[pointer:])
    #if pointer == False or len(binString[pointer:]) < 7:
    if pointer == False or int(binString[pointer:], 2) == 0:
        print("End of transmission!")
        break

print("versionSum:", versionSum)