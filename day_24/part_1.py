import sys
from math import floor

# Read an input value and write it to variable a.
def inp(a, b):
    global debug
    try:
        b = int(b)
    except ValueError:
        pass  # it was already int
    #print("  INPUT:", str(b))
    writeRegister(a, b)
    if debug: print("Result of inp("+str(a)+","+str(b)+") is: "+str(register[a])+" at register: "+str(a))
    return True

# Add the value of a to the value of b, then store the result in variable a.
def add(a,b):
    global register, debug
    try:
        b = int(b)
    except ValueError:
        b = register[b]
    writeRegister(a, register[a] + b)
    if debug: print("Result of add("+str(a)+","+str(b)+") is: "+str(register[a])+" at register: "+str(a))
    return True

# Multiply the value of a by the value of b, then store the result in variable a.
def mul(a,b):
    global register, debug
    try:
        b = int(b)
    except ValueError:
        b = register[b]
    writeRegister(a, register[a] * b)
    if debug: print("Result of mul("+str(a)+","+str(b)+") is: "+str(register[a])+" at register: "+str(a))
    return True

# Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
def div(a,b):
    global register, debug
    try:
        b = int(b)
    except ValueError:
        b = register[b]
    if b == 0:
        print("ERROR: Attempt to divide by zero!")
        return False
    writeRegister(a, floor(register[a] / b))
    if debug: print("Result of div("+str(a)+","+str(b)+") is: "+str(register[a])+" at register: "+str(a))
    return True

# Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
def mod(a,b):
    global register, debug
    try:
        b = int(b)
    except ValueError:
        b = register[b]
    if register[a] < 0:
        print("ERROR: Attempt to mod with register[a] < 0!")
        return False
    if b <= 0:
        print("ERROR: Attempt to mod with b <= 0!")
        return False
    writeRegister(a, register[a] % b)
    if debug: print("Result of mod("+str(a)+","+str(b)+") is: "+str(register[a])+" at register: "+str(a))
    return True

# If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
def eql(a,b):
    global register, debug
    try:
        b = int(b)
    except ValueError:
        b = register[b]
    if register[a] == b:
        writeRegister(a, 1)
    else:
        writeRegister(a, 0)
    if debug: print("Result of eql("+str(a)+","+str(b)+") is: "+str(register[a])+" at register: "+str(a))
    return True

# some tests:
def runTests():
    global register, debug
    # inp a - Read an input value and write it to variable a.
    register = getRegister()
    print("TEST: inp")
    inp("x", "4")
    if register["x"] == 4:
        print(" - PASS")
    else:
        print(" - FAIL")

    # add a b - Add the value of a to the value of b, then store the result in variable a.
    register = getRegister()
    print("TEST: add")
    inp("x", "1")
    add("x", "1")
    if register["x"] == 2:
        print(" - PASS")
    else:
        print(" - FAIL")

    # mul a b - Multiply the value of a by the value of b, then store the result in variable a.
    register = getRegister()
    print("TEST: mul")
    inp("x", "2")
    mul("x", "4")
    if register["x"] == 8:
        print(" - PASS")
    else:
        print(" - FAIL")

    # div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
    register = getRegister()
    print("TEST: div")
    inp("x", "8")
    div("x", "2")
    if register["x"] == 4:
        print(" - PASS (1)")
    else:
        print(" - FAIL (1)")
    inp("x", "9")
    div("x", "2")
    if register["x"] == 4:
        print(" - PASS (2)")
    else:
        print(" - FAIL (2)")

    # mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
    register = getRegister()
    print("TEST: mod")
    inp("x", "8")
    mod("x", "3")
    if register["x"] == 2:
        print(" - PASS")
    else:
        print(" - FAIL")

    # eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
    register = getRegister()
    print("TEST: eql")
    inp("x", "2")
    eql("x", "1")
    if register["x"] == 0:
        print(" - PASS (1)")
    else:
        print(" - FAIL (1)")
    inp("x", "2")
    eql("x", "2")
    if register["x"] == 1:
        print(" - PASS (2)")
    else:
        print(" - FAIL (2)")

def writeRegister(reg, value):
    global register, debug, step
    c = str(register)
    #if debug: print("Writing to register, value: " + str(value))
    register[reg] = value
    if c == str(register):
        print(str(step) + ": " + str(register) + " NO CHANGE")
        pass
    else:
        print(str(step) + ": ", register)
        pass
    step += 1
    

def getRegister():
    return {
        "x": 0,
        "y": 0,
        "z": 0,
        "w": 0
    }

def checkModelNumber(model):
    global MONAD, register
    # this is all the first section of MONAD does, so we can skip it:
    # register = {
    #     "x": 1,
    #     "y": model[0] + 3,
    #     "z": model[0] + 3,
    #     "w": model[0]
    # }
    # modelPointer = 1
    
    # # this is all the second bit does:
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 7
    # register["z"] += register["y"]
    # modelPointer = 2

    # # third bit:
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 1
    # register["z"] += register["y"]
    # modelPointer = 3

    # # 4:
    # register["z"] = floor(register["z"] / 26)
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 6
    # register["z"] += register["y"]
    # modelPointer = 4

    # # 5:
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 14
    # register["z"] += register["y"]
    # modelPointer = 5

    # # 6:
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 7
    # register["z"] += register["y"]
    # modelPointer = 6

    # # 7:
    # register["z"] = floor(register["z"] / 26)
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 9
    # register["z"] += register["y"]
    # modelPointer = 7

    # # 8:
    # register["z"] = floor(register["z"] / 26)
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 9
    # register["z"] += register["y"]
    # modelPointer = 8

    # # 9:
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 6
    # register["z"] += register["y"]
    # modelPointer = 9

    # #10:
    # register["z"] = floor(register["z"] / 26)
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 4
    # register["z"] += register["y"]
    # modelPointer = 10

    # #11:
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer]
    # register["z"] += register["y"]
    # modelPointer = 11

    # #12:
    # register["z"] = floor(register["z"] / 26)
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 7
    # register["z"] += register["y"]
    # modelPointer = 12

    # #13:
    # register["z"] = floor(register["z"] / 26)
    # register["z"] = register["z"] * 26
    # register["y"] = model[modelPointer] + 12
    # register["z"] += register["y"]
    # modelPointer = 13

    # 1
    w = model[0]
    z = w + 3
    #2 
    w = model[1]
    z = z * 26
    z += w + 7
    #3
    w = model[2]
    z = z * 26
    z += w + 1
    #4
    w = model[3]
    z = floor(z/26) * 26
    z += w + 6
    #5
    w = model[4]
    z = z * 26
    z += w + 14
    #6
    w = model[5]
    z = z * 26
    z += w + 7
    #7
    w = model[6]
    z = floor(z/26) * 26
    z += w + 9
    #8
    w = model[7]
    z = floor(z/26) * 26
    z += w + 9
    #9
    w = model[8]
    z = z * 26
    z += w + 6
    #10
    w = model[9]
    z = floor(z/26) * 26
    z += w + 4
    #11
    w = model[10]
    z = z * 26
    z += w
    #12
    w = model[11]
    z = floor(z/26) * 26
    z += w + 7
    #13
    w = model[12]
    z = floor(z/26) * 26
    z += w + 12
    
    register = {
        "x": 0,
        "y": 25,
        "z": z,
        "w": 0
    }

    w = model[13]
    x = z % 26 # x=12
    z = floor(z/26) # z=f(z/26) [this is the multiple of 26 + remainder x which is z]
    x -= 11 #x=1
    if x == w:
        x = 0 # so, say last digit is 1
    else:
        x = 1
    y = (25 * x) + 1 # y=1
    z = z * y #z=z
    y = w + 1 # y=2
    y = y * x # y=0
    z += y # z=z
    #print("  z: "+str(z))
    if z == 0: return True
    return False

    # register["z"] = z

    # #14:
    # register["x"] = 0
    # register["y"] = 25
    modelPointer = 13

    ok = True
    for instruction in MONAD:
        if instruction["cmd"] == "inp":
            inp(instruction["a"], model[modelPointer])
            modelPointer += 1
        elif instruction["cmd"] == "add":
            add(instruction["a"], instruction["b"])
        elif instruction["cmd"] == "mul":
            mul(instruction["a"], instruction["b"])
        elif instruction["cmd"] == "div":
            if div(instruction["a"], instruction["b"]) != True:
                ok = False
                break
        elif instruction["cmd"] == "mod":
            if mod(instruction["a"], instruction["b"]) != True:
                ok = False
                break
        elif instruction["cmd"] == "eql":
            eql(instruction["a"], instruction["b"])
        else:
            print("ERROR: Unexpected instruction: ", instruction)
            ok = False
            break
    
    if ok:
        if register["z"] == 0:
            return True
        else:
            return False

MONAD = []
while line := sys.stdin.readline().strip():
    # inp w
    # mul x 0
    line = line.split(" ")
    cmd = line[0]
    a = line[1]
    b = None
    if cmd != "inp":
        b = line[2]
    MONAD.append({
        "cmd": cmd,
        "a": a,
        "b": b
    })

debug = False
step = 1

# test, this is supposedly a model number

#checkModelNumber("13579246899999")
#cur = 12345678912345
#cur = 11111111676559
cur = 99997144971929
assert(len(str(cur)) == 14)
c = 1
while True:
    L = list(str(cur))
    if "0" in L:
        cur -= 1
        continue
    if c % 1000000 == 0:
        print(cur)
    step = 1
    c += 1
    model = [int(x) for x in L]
    modelString = "".join([str(x) for x in model])
    register = getRegister()
    result = checkModelNumber(model)
    if result:
        print(modelString + " is a model number! :-)")
        break
    else:
        #print(modelString + " is not a model number :-(")
        pass
    cur -= 1
    if cur < 11111111111111:
        break
    
