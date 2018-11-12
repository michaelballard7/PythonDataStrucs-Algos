"""

Modify the store.py program to find the sum 

and average of all integers in a list

"""

i = 0
summed = 0
listy = []
while(i < 5):
    num = int(input("Please enter a natural number? "))
    listy.append(num)
    i+=1

for x in range(5):
    summed = listy[x] + summed

print("The sum is ", summed)
print("The average equals {}".format(summed/len(listy)))