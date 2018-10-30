
""" FIFO Strucuture """

class Queue:

    # i can use a list as the underlying datatype for my queue
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    # with dequeue I must take off the first element, due FIFO
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    # as with deueue peeks shows the first element with out removing the first element
    def peek(self):
        return self.queue[0]


    def sizeQueue(self):
        return len(self.queue)

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.sizeQueue())

print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print(queue.sizeQueue())
