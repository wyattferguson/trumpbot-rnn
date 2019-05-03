
cleaned = open('tweets.txt', 'w')

with open('./raw_tweets.txt') as tweets:
    for tweet in tweets:
        if len(tweet) > 40:
            if tweet[0:2] != '" ' and tweet[0:3] != 'via' and tweet[0:2] != '"@':
                cleaned.write(tweet)
                print(tweet)

cleaned.close()