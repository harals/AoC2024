# [ x, [ y1, y2, y3 ]]
 
rules = {}
updates = []
invalids = []
 
def checkUpdate(update):
    for pagenum in update:
        rule = rules.get(pagenum)
        index = update.index(pagenum)
        if index == 0:
            continue
        sublist = update[0:index]
        for sub in sublist:
            if sub in rule:
                return False
    return True
 

def fixUpdate(update):
    if(checkUpdate(update)):
        return update
    for pagenum in update:
        rule = rules.get(pagenum)
        index = update.index(pagenum)
        if index == 0:
            continue
        sublist = update[0:index]
        for sub in sublist:
            if sub in rule:
                sub_index = update.index(sub)
                update[index], update[sub_index] = update[sub_index], update[index]
    return fixUpdate(update)
 
 
def findMiddle(update):
    middleIndex = int((len(update) - 1)/2)
    return update[middleIndex]
 
with open('input-05-1.txt', 'r') as file:
    for item in file:
            x,y = item.split("|")
            x = int(x)
            y = int(y)
            rule = rules.get(x)
            if rule is None:
                rules[x] = [y]
            else:
                rules[x].append(y)

 
with open('input-05-2.txt', 'r') as file:
    sum = 0
    for line in file:
        update = line.rstrip().split(",")
        for i in range(len(update)):
            update[i] = int(update[i])
        updates.append(update)
        valid = checkUpdate(update)
 
        if(valid):
            sum += findMiddle(update)
        else:
            invalids.append(update)
    print(sum)
    
    sum = 0
    for update in invalids:
        fixUpdate(update)
        sum += findMiddle(update)
    print(sum)