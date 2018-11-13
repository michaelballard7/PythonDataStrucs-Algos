"""
Implement the stack data structure 

Restrict the user to enter only 5 elements in the stack

If user enters sixth element throw an error message "Sorry, stack is full"

If user tries to remove element from an empty stack display "Sorry stack is empty" 

Display the following menu for the stack:

1. Insert Element into the stack
2. Remove Element from the stack
3. Display Stack 
4. Exit 

"""
stack = []

while True:
    print(" ")
    print(" --------------------------- ")
    print("     Stack Implementer ")
    print(" --------------------------- ")
    print(" ")
    print("Please select an option")
    print("1. Insert Element into the stack ")
    print("2. Remove Element from the stack ")
    print("3. Display Stack ")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(stack) == 5:
            print("Sprry, this stack is full")
        else:
            element = int(input("Please enter the element in the stack? "))
            stack.append(element)
            print(element, "inserted successfully")
    elif choice == 2:
        if len(stack) == 0:
            print("Sorry, stack is empty")
        else:
            element = stack.pop()
            print(element, "Was successfully removed")
    elif choice == 3:
        try:
            for i in range(len(stack)-1, -1,-1):
                print(stack[i])
        except:
            print("Sorry stack is empty")
            continue
    elif choice == 4:
        print("Thnak you. See you later")
        break
    else:
        print("Invalid option")

    more = input("Do you want to continue? ")

    if more == "1" or more == 'y' or more == "Y":
        continue
    else:
        print("Thank you see you soon")
        break

