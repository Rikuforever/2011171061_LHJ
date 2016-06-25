from DB import MasterDB

def getInputInt():
    n = None
    while not n:
        try:
            n = int(input())
        except ValueError:
            print("Wrong input. Only requires number.")
            print("Please input number: ", end="")
            n = None
    return n

db = MasterDB()
status = 0

while status != 99:
    if status == -1:
        print("0. Read data files (Reset DB)")
        print("1. Display statistics")
        print("2. Top 5 most tweeted words")
        print("3. Top 5 most tweeted users")
        print("4. Find users who tweeted a word")
        print("5. Find all people who are friends of the above users")
        print("6. Delete all mentions of a word")
        print("7. Delete all users who mentioned a word")
        print("8. Find strongly connected components")
        print("9. Find shortest path from a given user")
        print("99. Quit")
        print("Select Menu:  ", end="")
        status = getInputInt()
    elif status == 0:
        print()
        print("Loading")
        print("Finished Loading")
        db.readFile()
        cUser = db.UserDB.totalUser
        cEdge = db.EdgeDB.totalEdge
        cTweet = db.TweetDB.totalTweet
        print()
        print("=====")
        print("Total users: " + str(cUser))
        print("Total friendship records: " + str(cEdge))
        print("Total tweets: " + str(cTweet))
        print("=====")
        print()
        status = -1
    elif status == 1:
        cUser = db.UserDB.totalUser
        cEdge = db.EdgeDB.totalEdge
        cTweet = db.TweetDB.totalTweet
        f = db.getFollowRank()
        t = db.getTweetRank()
        lenFollow = len(f)
        maxFollow = f[0]
        minFollow = f[lenFollow - 1]
        lenTweet = len(t)
        maxTweet = t[0]
        minTweet = t[lenTweet - 1]

        print()
        print("=====")
        print("Total users: " + str(cUser))
        print("Total friendship records: " + str(cEdge))
        print("Total tweets: " + str(cTweet))
        print()
        print("Average number of friends: "+str(db.EdgeDB.totalEdge%lenFollow))
        print("Minimum friends: "+str(minFollow.followCount))
        print("Maximum number of friends: "+str(maxFollow.followCount))
        print()
        print("Average tweets per user: "+str(db.TweetDB.totalTweet%lenTweet))
        print("Minimum tweets per user: "+str(minTweet.tweetCount))
        print("Maximum tweets per user: "+str(maxTweet.tweetCount))
        print("=====")
        print()
        status = -1
    elif status == 2:
        l = db.getWordRank()
        print()
        print("=====")
        print("Most Tweeted Words")
        for x in range(5):
            print(str(x+1)+" : "+l[x].word+" ( "+str(l[x].tweetCount)+" times )")
        print("=====")
        print()
        status = -1
    elif status == 3:
        l = db.getTweetRank()
        print()
        print("=====")
        print("Most Tweeted Users")
        for x in range(5):
            print(str(x + 1) + " : " + l[x].userName + " ( " + str(l[x].tweetCount) + " times )")
        print("=====")
        print()
        status = -1
    elif status == 4:
        print()
        print("Input one word: ", end="")
        w = input()
        l = db.searchUserByWord(w)
        print()
        print("=====")
        if l:   # Valid word
            user = l[0]
            count = l[1]
            for x in range(len(user)):
                print(user[x].userName+" ( "+str(count[x])+" times )")
            print()
            print("Total User(s): "+str(len(user)))
        else:   # Valid word
            print("Invalid word, please try again")
        print("=====")
        print()
        status = -1
    elif status == 5:
        print()
        print("Input one word: ", end="")
        w = input()
        l = db.searchUserByWord(w)
        print()
        print("=====")
        if l:
            user = l[0]
            for x in range(len(user)):  # For each found user
                print(user[x].userName+"'s Friends: ")
                u = db.getFollowUser(user[x].id)
                for y in range(len(u)):
                    print("   "+u[y].userName)  # Print follow UserNames
                print()
        else:
            print("Invalid word, please try again")
        print("=====")
        print()
        status = -1
    elif status == 6:
        print()
        print("Input one word: ", end="")
        w = input()
        result = db.deleteTweet(w)
        print()
        print("=====")
        if result:
            print("Successfully ereased "+str(result)+" tweet(s)")
        else:
            print("Invalid word, please try again")
        print("=====")
        print()
        status = -1
    elif status == 7:
        l = [0,0]
        print()
        print("Input one word: ", end="")
        w = input()
        user = db.searchUserByWord(w)[0]
        print()
        print("=====")
        if user:
            for x in range(len(user)):    # For each user
                r = db.deleteUser(user[x].id)
                l[0] += r[0]
                l[1] += r[1]
            print("Deleted user(s): "+str(len(user)))
            print("Deleted friendship record(s):" + str(l[1]))
            print("Deleted tweet(s): "+str(l[0]))
        else:
            print("Invalid word, please try again")
        print("=====")
        print()
        status = -1
    else:
        print("Invalid input.")
        status = -1
