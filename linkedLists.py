# Linked lists are composed nodes and references / pointers pointing from one node to other
# The last reference points to null
# Iterate through the nodes until I hit null
# a single node contains data(integer, float or custom object) & and reference to the next object
# Linked lists can be used to implement common data types like stacks and queues
# Simple linked lists should by themselves not allow random access to data
# I have to iterate through all nodes to find data in a linked list
# linked list are dynamic and allocate memory at run time
# Linked list waste memory becuase of references
# Linked list updating require ordinal (1) time complexity at the beginning
# Singly linked lists are hard to traverse backwards
# Linked list updating at the end O(N) time complexity


class Node(object):

    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.size = 0 

    # this is very fast and has ordinal(1) time complexity
    def insertStart(self, data):
        self.size = self.size + 1 
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            print("Data successfully inserted at front of list")
        else:
            newNode.nextNode = self.head
            self.head = newNode
            print("Data successfully inserted at front of list")
           

    def size1(self):
        return self.size
    
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
            return size

    # inseting at the end is very slow and has linear time complexity
    def insertEnd(self,data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode =self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode
        
        print("Successfully added to end the list")
        

    def traverseList(self,data):
        actualNode = self.head

        while actualNode is not None:
            print("#d" % actualNode.data)
            actualNode = actualNode.nextNode

    def remove(self,data):

        if self.head is None:
            return

        self.size = self.size - 1 

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

linkedList = LinkedList()

print("The size output ", linkedList.size1)

linkedList.insertStart(8)
linkedList.insertEnd(27)
