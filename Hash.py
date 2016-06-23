from LinkedList import LinkedList


class Hash:
    def __init__(self, n):
        self.hTable = []
        self.size = n
        for x in range(n):
            l = LinkedList()
            self.hTable.append(l)

    def add(self, key, v):
        n = key % self.size
        if self.hTable[n].search(key):
            print("Error : Already Existing Key")
            return None
        self.hTable[n].add(key, v)

    def search(self, key):
        n = key % self.size
        v = self.hTable[n].search(key)
        if v:
            return v
        else:
            print("No Matching Key")
            return None
