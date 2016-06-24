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
            hData = self.TweetDB.getHash(word)
            t = self.TweetDB.list.search(hData)
            if t:                           # If already existing Tweet, add User
                t.userList.add(id, u)
                t.userCount += 1
            else:                           # If no matching Tweet, make new Tweet
                new = Tweet()
                new.word = word
                new.userList.add(id, u)
                new.userCount += 1
                self.TweetDB.addTweet(hData, new)
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
        self.TweetDB.updateWordRank()
        return self.TweetDB.wordRank

    def getFollowRank(self):
        self.UserDB.updateFollowRank()
        return self.UserDB.followRank

    def getTweetRank(self):
        self.UserDB.updateTweetRank()
        return self.UserDB.tweetRank

    def searchUserByWord(self, word):
        user = []
        self.TweetDB.list.search

class UserDB:
    def __init__(self):
        self.list = Hash(USER_HASH_SIZE)
        self.followRank = []
        self.tweetRank = []
        self.totalUser = 0

    def addUser(self, id, n):
        if self.list.add(id, n):   # If successfully added
            self.totalUser += 1
        else:
            return None

    def deleteUser(self, id):
        if self.list.delete(id):   # If successfully deleted
            self.totalUser -= 1
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

    def updateTweetRank(self):
        self.tweetRank.clear()
        for x in range(len(self.list.hTable)):  # Through Hash List
            n = self.list.hTable[x].start
            while n:                            # Through Linked List
                if n.v:
                    self.tweetRank.append(n.v)
                n = n.next
        self.tweetRank = sorted(self.tweetRank, key=self.getTweet, reverse=True)   # Sort by TweetCount

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

    def addTweet(self, key, n):
        if self.list.add(key, n):   # If successfully added
            self.totalTweet += 1
        else:
            return None

    def deleteTweet(self, key):
        if self.list.delete(key):
            self.totalTweet -= 1
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
        self.tweetRank = sorted(self.wordRank, key=self.getWord, reverse=True)  # Sort by TweetCount

    def getWord(self, t):
        return t.userCount


class EdgeDB:
    def __init__(self):
        self.list = LinkedList()

    def addEdge(self, n):
        self.list.add(None, n)

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
