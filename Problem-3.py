def getOddNumbers(count):
    result = []
    if count%2 == 0 : count = count-1
    for i in range(1, count*2):
        if i%2 != 0 : result.append(i)
    return result 

count = int(input("Enter a integer coint"))
print(getOddNumbers(count))

# alternate solution
# count = int(input("enter a integer"))
# if count%2 == 0 : count = count-1
# for i in range(1, count*2, 2):
#     print(i, " ")