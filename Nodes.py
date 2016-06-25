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
        self.tweetCount = 0

    def getUserList(self):
        out = []
        user = []
        count = []
        n = self.userList.start
        while n:
            try:
                x = user.index(n.v)
            except ValueError:
                x = None
            if x is None:
                user.append(n.v)
                count.append(1)
            else:
                count[x] += 1
            n = n.next
        out.append(user)
        out.append(count)
        return out


class Edge:                     # From A to B
    def __init__(self):
        self.A = None
        self.B = None


