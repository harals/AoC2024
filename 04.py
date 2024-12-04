
data = []

def findHorizontalRight():
    num = 0
    for row in range(len(data)):
        for char in range(len(data[row])-3):
            if(data[row][char] == "X"):
                if(data[row][char+1] == "M"):
                    if(data[row][char+2] == "A"):
                        if(data[row][char+3] == "S"):
                            num += 1
    return num                            

def findHorizontalLeft():
    num = 0
    for row in range(len(data)):
        for char in range(3,len(data[row])):
            if(data[row][char] == "X"):
                if(data[row][char-1] == "M"):
                    if(data[row][char-2] == "A"):
                        if(data[row][char-3] == "S"):
                            num += 1
    return num

def findVerticalDown():
    num = 0
    for row in range(len(data)-3):
        for char in range(len(data[row])):
            if(data[row][char] == "X"):
                if(data[row+1][char] == "M"):
                    if(data[row+2][char] == "A"):
                        if(data[row+3][char] == "S"):
                            num += 1
    return num

def findVerticalUp():
    num = 0
    for row in range(3,len(data)):
        for char in range(len(data[row])):
            if(data[row][char] == "X"):
                if(data[row-1][char] == "M"):
                    if(data[row-2][char] == "A"):
                        if(data[row-3][char] == "S"):
                            num += 1
    return num

def findDiagonalDownRight():
    num = 0
    for row in range(len(data)-3):
        for char in range(len(data[row])-3):
            if(data[row][char] == "X"):
                if(data[row+1][char+1] == "M"):
                    if(data[row+2][char+2] == "A"):
                        if(data[row+3][char+3] == "S"):
                            num += 1
    return num

def findDiagonalDownLeft():
    num = 0
    for row in range(len(data)-3):
        for char in range(3,len(data[row])):
            if(data[row][char] == "X"):
                if(data[row+1][char-1] == "M"):
                    if(data[row+2][char-2] == "A"):
                        if(data[row+3][char-3] == "S"):
                            num += 1
    return num

def findDiagonalUpRight():
    num = 0
    for row in range(3,len(data)):
        for char in range(len(data[row])-3):
            if(data[row][char] == "X"):
                if(data[row-1][char+1] == "M"):
                    if(data[row-2][char+2] == "A"):
                        if(data[row-3][char+3] == "S"):
                            num += 1
    return num

def findDiagonalUpLeft():
    num = 0
    for row in range(3,len(data)):
        for char in range(3,len(data[row])):
            if(data[row][char] == "X"):
                if(data[row-1][char-1] == "M"):
                    if(data[row-2][char-2] == "A"):
                        if(data[row-3][char-3] == "S"):
                            num += 1
    return num

def countX():
    num = 0
    for row in range(1,len(data)-1):
        for char in range(1,len(data[row])-1):
            if(isMasOrSamRD(row, char) and isMasOrSamLD(row, char)):
                num += 1
    return num

def isMasOrSamRD(row, char):
    if(data[row][char] == "A" and
       data[row-1][char-1] == "M" and
       data[row+1][char+1] == 'S'):
        return True
    if(data[row][char] == "A" and
       data[row-1][char-1] == "S" and
       data[row+1][char+1] == 'M'):
        return True
    else:
        return False
    
def isMasOrSamLD(row, char):
    if(data[row][char] == "A" and
       data[row-1][char+1] == "M" and
       data[row+1][char-1] == 'S'):
        return True
    if(data[row][char] == "A" and
        data[row-1][char+1] == "S" and
        data[row+1][char-1] == 'M'):
        return True
    else:
        return False
    

with open('input-04.txt', 'r') as file:
    for line in file:
        data.append(list(line.rstrip()))
        
    found = 0
    found += findHorizontalRight()
    found += findHorizontalLeft()
    found += findVerticalDown()
    found += findVerticalUp()
    found += findDiagonalDownRight()
    found += findDiagonalDownLeft()
    found += findDiagonalUpRight()
    found += findDiagonalUpLeft()
    
    print(found)
    print(countX())
    