import copy

map = []
current_x = 0
current_y = 0
move_counter = 1
loop_counter = 0

with open('input-06.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        map.append(list(line))
        
    originalmap = copy.deepcopy(map)
        
# find cursor
def find():
    global current_x
    global current_y
    for x in range(len(map)):
        for y in range(len(map)):
            if (map[x][y] == "^" or
                map[x][y] == ">" or
                map[x][y] == "v" or
                map[x][y] == "<"):
                current_x = x
                current_y = y
                return x,y
        

def walk():
    global map, current_x, current_y, move_counter, loop_counter
    
    
    if(current_x >= len(map) or current_y >= len(map[0])):
       print("cannot move outside edge" , current_x, current_y, " > ", len(map), len(map[0]))
       return
    
    cursor_type = map[current_x][current_y]    
    if(cursor_type == "^"):
        if(map[current_x-1][current_y] == '#'):
            # is blocked
            turn()
        else:
            map[current_x][current_y] = "X"
            current_x -= 1
            if(map[current_x][current_y] == "."):
                move_counter += 1
            if(map[current_x][current_y] == "X"):
                loop_counter += 1
            map[current_x][current_y] = cursor_type
    elif(cursor_type == ">"):
        if(map[current_x][current_y+1] == '#'):
            # is blocked
            turn()
        else:
            map[current_x][current_y] = "X"
            current_y += 1
            if(map[current_x][current_y] == "."):
                move_counter += 1
            if(map[current_x][current_y] == "X"):
                loop_counter += 1
            map[current_x][current_y] = cursor_type
            
    elif(cursor_type == "v"):
        if(map[current_x+1][current_y] == '#'):
            # is blocked
            turn()
        else:
            map[current_x][current_y] = "X"
            current_x += 1
            if(map[current_x][current_y] == "."):
                move_counter += 1
            if(map[current_x][current_y] == "X"):
                loop_counter += 1
            map[current_x][current_y] = cursor_type
    elif(cursor_type == "<"):
        if(map[current_x][current_y-1] == '#'):
            # is blocked
            turn()
        else:
            map[current_x][current_y] = "X"
            current_y -= 1
            if(map[current_x][current_y] == "."):
                move_counter += 1
            if(map[current_x][current_y] == "X"):
                loop_counter += 1
            map[current_x][current_y] = cursor_type    
        
def isOutside():
    if(current_x >= len(map)-1 or current_x == 0):
        return True
    elif(current_y >= len(map[0])-1 or current_y == 0): # assuming all lines are of equal length
        return True
    else:
        return False
    
def printGFX():
    print("pos now: ", current_x, current_y)
    print(map[current_x-1][current_y-1:current_y+2])
    print(map[current_x][current_y-1:current_y+2])
    print(map[current_x+1][current_y-1:current_y+2])
    
def turn():
    global map
    global current_x
    global current_y
    if(map[current_x][current_y] == "^"):
        map[current_x][current_y] = ">"
    elif(map[current_x][current_y] == ">"):
        map[current_x][current_y] = "v"
    elif(map[current_x][current_y] == "v"):
        map[current_x][current_y] = "<"
    elif(map[current_x][current_y] == "<"):
        map[current_x][current_y] = "^"

# main
def escape():
    global loop_counter, move_counter
    move_counter = 1
    loop_counter = 0
    
    find() # to initialize variables
    while not isOutside():
        walk()
        # printGFX() # print 3x3 proximal to cursor
        if(loop_counter > 1000): # brute force threshold
            return False
    return True
       
def part1():
    escape()
    print(move_counter)

def part2():
    global map, current_x, current_y, move_counter
    current_x = 0
    current_y = 0
    move_counter = 1
    loops = 0
    init_x, init_y = find()
    
    # do not place at (49, 47)

    for i in range(len(map)):
        print("i = ", i, " of ", len(map)) # progress
        for j in range(len(map[0])):
            map = copy.deepcopy(originalmap)
            if(i == init_x and j == init_y):
                continue
            else:
                map[i][j] = "#"
                if(not escape()):
                    loops += 1
    print(loops)
        
    
    

### part 1
#part1()

### part 2
part2()
