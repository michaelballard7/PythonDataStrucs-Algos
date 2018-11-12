"""

Write a program that inputs he current day and month

It then calculates and displays the number of days

in the current uear till the date entered. 

"""

days = [31,28,31,30,31,30,31,31,30,31,30,31]


month = int(input("Please enter the month: "))

day = int(input("Please enter the day: "))

total = day


for i in range(month - 1):
    total = total + days[i]


print("The total days till the entered day/month is ", total)