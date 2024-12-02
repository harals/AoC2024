safe = 0

def test_increasing(report):
    for i in range(len(report)):
        if(i == 0):
            continue
        elif(int(report[i-1]) >= int(report[i])):
            return False
    return True

def test_decreasing(report):
    for i in range(len(report)):
        if(i == 0):
            continue
        elif(int(report[i-1]) <= int(report[i])):
            return False
    return True

def test_differ(report):
    for i in range(len(report)):
        if(i == 0):
            continue
        elif(int(report[i]) > int(report[i-1]) + 3):
            return False
        elif(int(report[i]) < int(report[i-1]) - 3):
            return False
 
    return True
 
def test_report(report):
        increasing = test_increasing(report)
        decreasing =test_decreasing(report)
        difference = test_differ(report)
        return (((increasing or decreasing) and difference))
 
def test_report_with_dampener(report):
    if(test_report(report)):
        return True
    for i in range(len(report)):
        copy = report.copy()
        copy.pop(i)
        if(test_report(copy)):
           return True
 
with open("input.txt") as file:
    for line in file:
        report = line.rstrip().split(" ")
 
        if(test_report_with_dampener(report)):
            safe += 1
        #else:
        #   print(report)

print(safe)