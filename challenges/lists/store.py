
"""

Write a program that inputs five integers from the user
and stores them in a list. It then displays all the value in the
list using a loop


"""

i = 0
listy = []
while(i < 5):
    num = int(input("Please enter a natural number? "))
    listy.append(num)
    i+=1

for x in listy:
    print(listy[x])