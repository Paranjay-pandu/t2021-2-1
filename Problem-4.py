count = int(input("Enter the number of numbers in the list:"))
inputList = []
for i in range(count):
    num = int(input(f"Enter a number {i+1}:"))
    inputList.append(num)

def countMultiples(inputList):
    countDict = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0}
    for num in countDict:
        for i in inputList:
            if i%int(num) == 0:
                countDict[num] += 1
    return countDict

print(countMultiples(inputList))