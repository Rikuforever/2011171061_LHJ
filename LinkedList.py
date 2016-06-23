class LinkedList:
    def __init__(self):
        self.start = LNode()

    def add(self, key, v):
        node = LNode()
        node.key = key
        node.v =v
        if self.start.v:
            node.next = self.start
            self.start = node
        else:
            self.start.key = key
            self.start.v = v

    def search(self, key):
        n = self.start
        while n:
            if n.key is key:
                return n.v
            else:
                n = n.next
        return None


class LNode:
    def __init__(self):
        self.next = None
        self.key = None     # Search Key
        self.v = None       # Value
