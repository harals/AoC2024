antenna_map = []
antenna_locations = []
antinode_map = []
antinode_locations = []
map_height = 0
map_width = 0

def printMap():
    for line in antenna_map:
        print(line)
        
def findAntennas():
    antenna_locations = []
    for line in range(len(antenna_map)):
        for char in range(len(antenna_map[line])):
            symbol = antenna_map[line][char]
            if(symbol == '.'):
                continue
            elif(symbol == '#'):
                continue
            else:
                antenna_locations.append((symbol,line,char))
    return antenna_locations

def findAntinodes(antenna_map, antenna_locations):
    antinode_locations = []
    for antenna_1 in antenna_locations:
        char1,y1,x1 = antenna_1
    
        for antenna_2 in antenna_locations:
            if(antenna_1 == antenna_2):
                continue
            char2,y2,x2 = antenna_2
            if(char1 == char2):
                diffx = x2-x1
                diffy = y2-y1
                
                if part1:
                    
                    antix=x2+diffx
                    antiy=y2+diffy
                    
                    if(antix >= 0 and 
                       antix < map_width and 
                       antiy >= 0 and 
                       antiy < map_height and
                       #not isAnteannaAt(antix, antiy, antenna_locations) and
                       not isAntinodeAt(antix, antiy, antinode_locations)):
                            antinode_locations.append((antiy,antix))
                            #print("antinode: ", antix, antiy)

                    
                    
                else:
                
                    for i in range(1,100):
                        antix=x2+(i*diffx)
                        antiy=y2+(i*diffy)
                    
                        if(antix >= 0 and 
                           antix < map_width and 
                           antiy >= 0 and 
                           antiy < map_height and
                           #not isAnteannaAt(antix, antiy, antenna_locations) and
                           not isAntinodeAt(antix, antiy, antinode_locations)):
                                antinode_locations.append((antiy,antix))
                                #print("antinode: ", antix, antiy)

                        antix=x2-(i*diffx)
                        antiy=y2-(i*diffy)

                        if(antix >= 0 and 
                           antix < map_width and 
                           antiy >= 0 and 
                           antiy < map_height and
                           #not isAnteannaAt(antix, antiy, antenna_locations) and
                           not isAntinodeAt(antix, antiy, antinode_locations)):
                                antinode_locations.append((antiy,antix))
                                #print("antinode: ", antix, antiy)

            
    return antinode_locations

def isAnteannaAt(x,y,antenna_locations):
    c = antenna_map[y][x]
    if(c == '.' or c == '#'):
        return False
    return True

def isAntinodeAt(x,y, antinode_locations):
    for a in antinode_locations:
        (y1,x1) = a
        if( (y,x) == (y1,x1)):
            return True
    return False
        

with open('input-08.txt', 'r') as file:
    
    for line in file:
        antenna_map.append(list(line.rstrip()))
        
    map_height=len(antenna_map)
    map_width=len(antenna_map[0])
        
    
    part1 = True
    antenna_locations = findAntennas()
    antinode_locations = findAntinodes(antenna_map, antenna_locations)
    
print("antinodes: ", len(antinode_locations) )