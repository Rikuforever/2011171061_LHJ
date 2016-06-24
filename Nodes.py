from LinkedList import LinkedList


class User:
    def __init__(self):
        self.N = None           # Maybe not needed
        self.id = 0
        self.userName = None
        self.tweetCount = 0
        self.followCount = 0


class Tweet:
    def __init__(self):
        self.word = None
        self.userList = LinkedList()
        self.userCount = 0


class Edge:                     # From A to B
    def __init__(self):
        self.A = None
        self.B = None


