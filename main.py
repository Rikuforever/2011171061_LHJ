from DB import MasterDB

db = MasterDB()
db.readFile()
h = db.TweetDB.getHash("내가")
d = db.TweetDB.list.search(h)
print(d.userList.start.v.userName)
db.UserDB.updateFollowRank()
db.UserDB.updateTweetRank()
for x in range(300):
    print(db.UserDB.tweetRank[x].userName)
    print(db.UserDB.tweetRank[x].tweetCount)
