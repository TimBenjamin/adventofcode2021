import sys

algoString = sys.stdin.readline().strip().replace("#","1").replace(".","0")
next(sys.stdin)

image = []
while line := sys.stdin.readline():
    image.append(list(line.strip().replace("#","1").replace(".","0")))

def padImage(image, padChar):
    # add N spaces of padding all round it
    padding = 5
    newImage = []
    blank = [padChar] * (len(image[0]) + (padding*2))
    for _ in range(padding):
        newImage.append(blank)
    for row in image:
        newImage.append(([padChar]*padding) + row + ([padChar]*padding))
    for _ in range(padding):
        newImage.append(blank)
    return newImage

def printImage(image):
    for row in image:
        row = "".join(row)
        print(row.replace("1","#").replace("0","."))
    print()

def getBlank(image):
    newImage = []
    for _ in image:
        newImage.append(["0"] * len(image))
    return newImage

steps = 2
image = padImage(image, "0")
printImage(image)
for _ in range(steps):
    print("image size:", len(image))
    newImage = getBlank(image)
    for i in range(1, len(image)-1):
        for j in range(1, len(image[i])-1):
            # this is middle of the 3x3 grid we are going to update
            lookupString = ""
            lookupString += image[i-1][j-1] + image[i-1][j] + image[i-1][j+1]
            lookupString += image[i][j-1] + image[i][j] + image[i][j+1]
            lookupString += image[i+1][j-1] + image[i+1][j] + image[i+1][j+1]
            algoIndex = int(lookupString, 2)
            pixel = algoString[algoIndex]
            newImage[i][j] = pixel
    padCharLookupString = ""
    padCharLookupString += image[1][1] + image[1][2] + image[1][3]
    padCharLookupString += image[2][1] + image[2][2] + image[2][3]
    padCharLookupString += image[3][1] + image[3][2] + image[3][3]
    padCharAlgoIndex = int(padCharLookupString, 2)
    padChar = algoString[padCharAlgoIndex]
    # strip the outermost padding
    newImage = newImage[1:len(newImage)-1]
    for i, row in enumerate(newImage):
        newImage[i] = row[1:len(row)-1]
    image = newImage
    image = padImage(image, padChar)
    print("final i,j", i,j)
    print()
#newImage = padImage(newImage)
printImage(newImage)

# number of 1s?
count = 0
for row in image:
    for cell in row:
        if cell == "1":
            count += 1
print(count)
