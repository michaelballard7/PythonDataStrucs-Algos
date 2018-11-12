"""
 Write a program that finds the maximum value of a list

 Do not use built in helper methods

"""



import random

intList = []

for i in range(10):
    intList.append(random.randint(1,100))

# initialize the maximum value at index zero
max_value = intList[0]

for j in range(1,10):
    if intList[j] > max_value:
        max_value = intList[j]

print(intList)
print("The max value in the list is ", max_value)