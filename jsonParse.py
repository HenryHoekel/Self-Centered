import tweepy
import json

from pprint import pprint

def parse_json(user):

    ## direct file path to .json file ##
    filepath = 'C:\\Users'
    user = user.lower()
    filepath = filepath + user + '.json'

    with open(filepath) as data_file:
        data = json.load(data_file)

    ####  debug data if you wish #####
    #print data
    #pprint(data)

    #one_user = data['user'][0]['text']

    tweets = []

    for user in data:
        ### more debug ####
        #print(user["text"])
        tweets.append(user["text"])

    selfish_tweets = []

    count=0
    # Todo: Parse this better
    for x in tweets:
        if "I " in x:
            count+=1
            selfish_tweets.append(x)
        elif "Me " in x:
            count+=1
            selfish_tweets.append(x)
        elif "me " in x:
            count+=1
            selfish_tweets.append(x)
        elif "Myself " in x:
            count+=1
            selfish_tweets.append(x)
        elif "myself " in x:
            count+=1
            selfish_tweets.append(x)
        elif "My " in x:
            count+=1
            selfish_tweets.append(x)
        elif "my " in x:
            count+=1
            selfish_tweets.append(x)

    # Print the Results :)
    print('Selfish Tweets: ' + str(count) + '/' + str(len(tweets)))
    total = count / len(tweets)
    print('Percentage: ' + str(total))
    pprint(selfish_tweets)
    print('\n')

    #### print all tweets (showoff) ###
    #pprint(tweets)

# end parse_json
