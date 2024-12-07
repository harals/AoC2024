import itertools,copy,re

def calc(factors):
    factors = re.split(r"(\+|\*|\|\|)",factors)
    result = 0
    for i in range(len(factors)):
        if(i == 0):
            result = int(factors[i])
            continue
    
        if(factors[i] == '+'):
            result += int(factors[i+1])
        elif(factors[i] == '*'):
            result *= int(factors[i+1])
        elif(factors[i] == "||"):
            result = int(str(result) + factors[i+1])
            
        i += 1 # skip to next operator
    return result



def seed(factors):
    # 1 2 3 4
    expressions = []
    numOps = factors.count(" ")
    permutations = list(itertools.product(['+','*','||'], repeat=numOps)) # remove || for part 1

    for opList in permutations:
        expr = copy.copy(factors)
        for i in opList:
            expr = expr.replace(" ", i, 1)
        expressions.append(expr)
    return expressions
            

with open('input-07.txt', 'r') as file:
    
    sumValid = 0
    for line in file:
        line = line.rstrip()

        result, factors = line.split(':')
        result = int(result)
        factors = factors.strip()
        
        expressions = seed(factors)
        
        for exp in expressions:
            val = calc(exp)
            if (result == val):
                print("true: ",result, val, exp)
                sumValid += val
                break
    print(sumValid)
        
    