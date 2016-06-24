from DB import MasterDB

db = MasterDB()
status = -1

while status != 99:
    if status == -1:
        print("0. Read data files")
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
        status = int(input())
    elif status == 0:
        print()
        print("Loading")
        db.readFile()
        print()
        print("=====")
        print("Finished reading.")
        print("=====")
        print()
        status = -1
    elif status == 1:
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
    elif status == 2:
        db.TweetDB.updateWordRank()
        l = db.TweetDB.wordRank
        print()
        print("=====")
        print("Most Tweeted Words")
        for x in range(5):
            print(str(x+1)+" : "+l[x].word+" ( "+str(l[x].tweetCount)+" times )")
        print("=====")
        print()
        status = -1
    elif status == 3:
        db.UserDB.updateTweetRank()
        l = db.UserDB.tweetRank
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
        t = db.TweetDB.searchTweet(w)
        print()
        print("=====")
        if t:   # Valid word
            l = t.getUserList()
            user = l[0]
            count = l[1]
            for x in range(len(user)):
                print(user[x].userName+" ( "+str(count[x])+" times )")
        else:   # Valid word
            print("Invalid word, please try again")
        print("=====")
        print()
        status = -1
    else:
        print("Invalid input.")
        status = -1
