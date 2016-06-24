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

    def delete(self, key):
        pre = None
        n = self.start
        while n:
            if n.key == key:            # When match found
                if pre:
                    pre.next = n.next
                    return 1
                else:                   # If first node
                    self.start = n.next
                    return 1
            else:
                pre = n
                n = n.next
        # print("Error : No Match Found")
        return None

    def search(self, key):
        n = self.start
        while n:
            if n.key == key:
                return n.v
            else:
                n = n.next
        return None


class LNode:
    def __init__(self):
        self.next = None
        self.key = None     # Search Key
        self.v = None       # Value
