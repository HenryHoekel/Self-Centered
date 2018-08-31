import tweepy
import json

from pprint import pprint

## direct file path to .json file ##
filepath = ''

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
for x in tweets:
    if "I " in x:
        count+=1
        selfish_tweets.append(x)
    elif "Me " in x:
        count+=1
        selfish_tweets.append(x)
    elif "Myself " in x:
        count+=1
        selfish_tweets.append(x)
    elif "me " in x:
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

    
print("COUNT ")
print(count)
print("/")
print(len(tweets))

total = count / len(tweets)

print("TOTAL")
print(total)

pprint(selfish_tweets)

#### print all tweets (showoff) ###
#pprint(tweets)

"""
test = "HI"
if "I " in test:
    print("YES")
else:
    print("no")
"""
    
print("COUNT ")
print(count)
print("/")
print(len(tweets))

total = count / len(tweets)

print("TOTAL")
print(total)