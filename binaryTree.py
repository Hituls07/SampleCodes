class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if self.data is None:
            return self.data == value
        elif value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)


    def printTree(self):
        if self.left is not None:
            self.left.printTree()

        print(self.data)

        if self.right is not None:
           self.right.printTree()


    def contains(self, value):

        if value == self.data:
            return True
        elif value <= self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)


    def getHeight(self, value):

        if value == self.data or self.data is None:
            return 0
        elif value < self.data:
            return 1 + self.left.getHeight(value)
        else:
            return 1 + self.right.getHeight(value)
        
        
    def highestHeight(self, root):

        l = 0 if root.left is None else 1 + self.getHeight(root.left)
        r = 0 if root.right is None else 1 + self.getHeight(root.right)

        if l > r:
            return l
        else:
            return r


r = Node(50)
r.insert(30)
r.insert(20)
r.insert(40)
r.insert(70)
r.insert(60)
r.insert(80)
r.insert(90)
print(r.contains(80))
print(r.getHeight(40))
print(r.highestHeight())
r.printTree()





