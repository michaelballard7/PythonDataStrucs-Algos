# Lists and types: 
mylist = [10,20,30,40]
names = ["Tahir", "John", "Ali", "Maria"]
mixtures = [True, "1234", 40, 1.002]


# Adding and Removing elements from a list 
names.append("Michael")
last_name = names.pop()

# Retrieving elements from a list
first_name = names[0]

# find an elements index:
specific_index = names.index("Tahir")

# Insert something to a specific element in the list
names.insert(0,"Malachi")
new_first_name = names[0]

# I can remove items from a list, if duplicated items the first element is removed
removed_name = names.remove("Maria")


# extend the end of a list with a collection of elements
names.extend(["Ballard", "Dixon","Bezos"])
x = ["Columbia", "Harvard"]
names.extend(x)

# I can measure the length of my list
length = len(names)   

# lists can be nested:
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
abc = [a,b,c]
middle_item = abc[1][1]

# List building methods