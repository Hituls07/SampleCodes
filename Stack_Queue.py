"""
Stacks, like the name suggests, follow the Last-in-First-Out (LIFO) principle.
As if stacking coins one on top of the other,
the last coin we put on the top is the one that is the first to be removed from the stack later
"""
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack


'''
One of the example of stack is undo feature in word files. 
We can record every action the user takes by pushing it to the stack. 
When the user wants to undo an action they'll pop it from the stack. 
We can quickly simulate the feature like this:
'''
document_actions = Stack()
document_actions.push('action: enter; text-id: 1, text: This is my favourite document')
print(document_actions.display())
document_actions.push('action; format; text_id: 1, alignment: center')
print(document_actions.display())
document_actions.pop()
print(document_actions.display())

"""
Queues, like the name suggests, follow the First-in-First-Out (FIFO) principle. 
As if waiting in a queue for the movie tickets, 
the first one to stand in line is the first one to buy a ticket and enjoy the movie.
"""


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def display(self):
        return self.queue


'''
Queues have widespread uses in programming as well. 
Think of games like Street Fighter or Super Smash Brothers.
Players in those games can perform special moves by pressing a combination of buttons. 
These button combinations can be stored in a queue.
We can enqueue all input events as they come in. This way it doesn't matter if input events come with little time between them, 
they'll all be stored and available for processing. 
When we're processing the moves we can dequeue them. 
'''

input_queue = Queue()
input_queue.enqueue('DOWN')
input_queue.enqueue('UP')
input_queue.enqueue('RIGHT')
print(input_queue.display())
print(input_queue.dequeue())
print(input_queue.dequeue())
print(input_queue.dequeue())


