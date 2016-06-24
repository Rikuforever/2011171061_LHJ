from DB import MasterDB

db = MasterDB()
db.readFile()
d = db.TweetDB.searchTweet("내가")
print(d.userList.start.v.userName)
db.UserDB.updateFollowRank()
db.UserDB.updateTweetRank()
for x in range(300):
    print(db.UserDB.tweetRank[x].userName)
    print(db.UserDB.tweetRank[x].tweetCount)
