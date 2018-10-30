# Doubly linked list are composed of nodes and refernces or pointers linked to the next nodes
# The last and first nodes point to node
# A single node can contain primitive data or a custom object, a reference point to the next node, another reference to the previous node
# a doubly linked list can be traversed in both directions: forward and backward
# with a doubly linked list the remove operation is more efficient if the node is given 


""" The first is another implementation of a singly linked list """
class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.nextNode = next


class SingleList(object):
    head = None
    tail = None

    def show(self):
        print("Showing list data")

        # set the current node equal to the head 
        current_node = self.head

        while current_node is not None:
            print(current_node.data, " -> ")
            current_node = current_node.next
        print( None)


    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node 
        self.tail = node

    def remove(self,node_value):
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.data == node_value:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next




