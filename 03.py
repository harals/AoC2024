import re

def sumAllMuls(expressions):
    sum=0
    for expr in expressions:
        match = re.match(r"mul\((\d+),(\d+)\)", expr)
        mul = match.groups()
        sum += int(mul[0]) * int(mul[1])
    return sum
    
with open('input-03.txt', 'r') as file:
    data = file.read().rstrip()
    expressions = re.findall(r"mul\(\d+,\d+\)", data)
    print(sumAllMuls(expressions))
    
with open('input-03.txt', 'r') as file:
    data = file.read().rstrip()
    expressions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", data)
    
    muls = []
    enabled = True
    for expr in expressions:
        if(expr == 'don\'t()'):
            enabled = False
            continue
        if(expr == 'do()'):
            enabled = True
            continue
        # is a mul()
        if(enabled):
            muls.append(expr)
            
    print(sumAllMuls(muls))
   