from Hash import Hash
from LinkedList import LinkedList
from Nodes import User
from Nodes import Tweet
from Nodes import Edge

USER_HASH_SIZE = 10
TWEET_HASH_SIZE = 10

class MasterDB:
    def __init__(self):
        self.UserDB = UserDB()
        self.TweetDB = TweetDB()
        self.EdgeDB = EdgeDB()

    def addUser(self, id, username):
        new = User()
        new.id = id
        new.userName = username
        if self.UserDB.addUser(new.id,new):
            return 1
        else:
            return None

    def addTweet(self, id, word):
        u = self.UserDB.list.search(id)
        if u:                               # If Valid UserID
            t = self.TweetDB.searchTweet(word)
            if t:                           # If already existing Tweet, add User
                t.userList.add(id, u)
                t.tweetCount += 1
            else:                           # If no matching Tweet, make new Tweet
                new = Tweet()
                new.word = word
                new.userList.add(id, u)
                new.tweetCount += 1
                self.TweetDB.addTweet(word, new)
            self.UserDB.plusTweet(id)              # Update Statistics
            return 1
        else:                               # If Invalid UserID
            print("Error : Invalid UserID")
            return None

    def addEdge(self, Aid, Bid):
        a = self.UserDB.list.search(Aid)
        b = self.UserDB.list.search(Bid)
        if a and b:                         # If both UserIDs are valid
            new = Edge()
            new.A = Aid
            new.B = Bid
            self.EdgeDB.addEdge(new)
            self.UserDB.plusFollow(Aid)          # Update Statistics
        else:
            print("Error : Invalid UserID")

    def readFile(self):
        data = []
        counter = 0

        # Read User.txt
        f = open("Data\\user.txt")
        for line in f:
            if counter == 0:
                user = []
                user.append(line[0:-1])
                counter += 1
            elif counter == 3:
                data.append(user)
                counter = 0
            else:
                user.append(line[0:-1])
                counter += 1
        # Input to UserDB
        for x in range(len(data)):
            id = int(data[x][0])
            username = data[x][2]
            self.addUser(id, username)
        data.clear()

        # Read Word.txt
        f = open("Data\\word.txt")
        for line in f:
            if counter == 0:
                tweet = []
                tweet.append(line[0:-1])
                counter += 1
            elif counter == 3:
                data.append(tweet)
                counter = 0
            else:
                tweet.append(line[0:-1])
                counter += 1
        # Input to TweetDB
        for x in range(len(data)):
            id = int(data[x][0])
            word = data[x][2]
            self.addTweet(id,word)
        data.clear()

        # Read Friend.txt
        f = open("Data\\friend.txt")
        for line in f:
            if counter == 0:
                edge = []
                edge.append(line[0:-1])
                counter += 1
            elif counter == 2:
                data.append(edge)
                counter = 0
            else:
                edge.append(line[0:-1])
                counter += 1
        # Input to EdgeDB
        for x in range(len(data)):
            A = int(data[x][0])
            B = int(data[x][1])
            self.addEdge(A,B)
        data.clear()

    def getWordRank(self):
        return self.TweetDB.updateWordRank()

    def getFollowRank(self):
        return self.UserDB.updateFollowRank()

    def getTweetRank(self):
        return self.UserDB.updateTweetRank()

    def searchUserByWord(self, word):
        t = self.TweetDB.searchTweet(word)
        if t:
            return t.getUserList()
        else:
            return None

    def getFollowUser(self, id):
        l = self.EdgeDB.getFollowID(id)
        for x in range(len(l)):
            u = self.UserDB.getUser(l[x])
            if u:
                l[x] = u
        return l

class UserDB:
    def __init__(self):
        self.list = Hash(USER_HASH_SIZE)
        self.followRank = []
        self.tweetRank = []
        self.totalUser = 0

    def addUser(self, id, n):
        if self.list.add(id, n):   # If successfully added
            self.totalUser += 1
            return 1
        else:
            return None

    def deleteUser(self, id):
        if self.list.delete(id):   # If successfully deleted
            self.totalUser -= 1
        else:
            return None

    def getUser(self, id):
        u = self.list.search(id)
        if u:
            return u
        else:
            return None

    def plusFollow(self, id):
        u = self.list.search(id)
        if u:
            u.followCount += 1

    def plusTweet(self, id):
        u = self.list.search(id)
        if u:
            u.tweetCount += 1
            # In construction : need to update leaderboard

    def updateFollowRank(self):
        self.followRank.clear()
        for x in range(len(self.list.hTable)):  # Through Hash List
            n = self.list.hTable[x].start
            while n:                            # Through Linked List
                if n.v:
                    self.followRank.append(n.v)
                n = n.next
        self.followRank = sorted(self.followRank, key=self.getFollow, reverse=True) # Sort by FollowCount
        return self.followRank

    def updateTweetRank(self):
        self.tweetRank.clear()
        for x in range(len(self.list.hTable)):  # Through Hash List
            n = self.list.hTable[x].start
            while n:                            # Through Linked List
                if n.v:
                    self.tweetRank.append(n.v)
                n = n.next
        self.tweetRank = sorted(self.tweetRank, key=self.getTweet, reverse=True)   # Sort by TweetCount
        return self.tweetRank

    def getFollow(self, user):
        return user.followCount

    def getTweet(self, user):
        return user.tweetCount


class TweetDB:
    def __init__(self):
        self.list = Hash(TWEET_HASH_SIZE)
        self.wordRank = []
        self.totalTweet = 0

    def getHash(self, word):
        hData = 0
        for x in range(len(word)):
            hData += ord(word[x])  # Convert Char to Int / Hash Info
        return hData

    def addTweet(self, word, v):
        h = self.getHash(word)
        n = h % self.list.size
        t = self.list.hTable[n].search(word)
        if t:                                   # If same word already exist
            print("Error : addTweet() doesn't allow duplicate word")
            return None
        else:
            self.list.hTable[n].add(word, v)
            self.totalTweet += 1
            return 1

    def deleteTweet(self, key):
        if self.list.delete(key):
            self.totalTweet -= 1
        else:
            return None

    def searchTweet(self, word):
        h = self.getHash(word)
        n = h % self.list.size
        t = self.list.hTable[n].search(word)
        if t:
            return t
        else:
            return None

    def updateWordRank(self):
        self.wordRank.clear()
        for x in range(len(self.list.hTable)):  # Through Hash List
            n = self.list.hTable[x].start
            while n:  # Through Linked List
                if n.v:
                    self.wordRank.append(n.v)
                n = n.next
        self.wordRank = sorted(self.wordRank, key=self.getWord, reverse=True)  # Sort by TweetCount
        return self.wordRank

    def getWord(self, t):
        return t.tweetCount


class EdgeDB:
    def __init__(self):
        self.list = LinkedList()
        self.totalEdge = 0

    def addEdge(self, n):
        self.list.add(None, n)                  # Need to check for duplicates
        self.totalEdge += 1

    def deleteUser(self, id):
        pre = None
        n = self.list.start
        while n:
            if (n.v.A == id) or (n.v.B == id):  # If either A or B is the UserID
                if pre:                         # Delete it
                    pre.next = n.next
                    n = n.next
                else:
                    self.list.start = n.next
                    n = self.list.start
            else:
                pre = n
                n = n.next

    def getFollowID(self, id):
        l = []
        n = self.list.start
        while n:
            if n.v.A == id:
                l.append(n.v.B)
            n = n.next
        return l
