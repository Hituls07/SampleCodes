
class Node:

    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None
        
        
class SLinkedList:

    def __init__(self):
        self.headval = None

    def listprint(self):
        prival = self.headval

        while prival is not None:
            print(prival.dataval)
            prival = prival.nextval

        return

    def AtBegining(self, dataval):
        new_node = Node(dataval)
        new_node.nextval = self.headval
        self.headval = new_node


    def AtEndining(self, dataval):
        new_node = Node(dataval)
        prival = self.headval
        if prival is None:
            self.headval = new_node
            return

        while(prival.nextval):
            prival = prival.nextval

        prival.nextval = new_node

    def InsertBetween(self, middle_node, dataval):

        new_node = Node(dataval)
        prival = self.headval

        if self.headval is None:
            self.headval = new_node

        while prival.dataval != middle_node:
            prival = prival.nextval
            if prival is None:
                return 'Node does not exist'

        new_node.nextval = prival.nextval
        prival.nextval = new_node

    def RemoveNode(self, removekey):

        prival = self.headval
        while prival.nextval.dataval != removekey:
            prival = prival.nextval
            if prival is None:
                return 'Node does not exist'

        prival.nextval = prival.nextval.nextval







e1 = SLinkedList()
e1.headval = Node('Mon')
e2 = Node('Tue')
e1.headval.nextval = e2
e3 = Node('Wed')
e2.nextval = e3
e1.AtBegining('Sun')
e1.AtEndining('Thur')
e1.InsertBetween('Wed', 'holiday')
e1.RemoveNode('Tue')
print(e1.listprint())
