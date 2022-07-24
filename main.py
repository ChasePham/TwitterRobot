import tweepy
import time


all_keys = open('Keys', 'r').read().splitlines()
CONSUMER_KEY = all_keys[0]
CONSUMER_SECRET_KEY = all_keys[1]
ACCESS_TOKEN = all_keys[2]
ACCESS_SECRET_TOKEN = all_keys[3]
BEARER_TOKEN = all_keys[4]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth, wait_on_rate_limit=True)


# Bot searches for tweets containing certain keywords
# class MyStream(tweepy.StreamingClient):
#
#     # This function gets called when a tweet passes the stream
#     def on_tweet(self, tweet):
#
#         # Retweeting the tweet
#         try:
#             # Retweet
#
#             # Printing Tweet
#             print(tweet.text + "--------------------------------------" + '\n')
#             # Delay
#             time.sleep(3)
#         except Exception as error:
#             # Error
#             print(error)
#
#
# # Creating Stream object
# stream = MyStream(bearer_token=BEARER_TOKEN)
#
# # Adding terms to search rules
# rule = tweepy.StreamRule("(#UTAustin OR #Paetow) (-is:retweet -is:reply)")
# stream.add_rules(rule, dry_run=True)
#
# # Starting stream
# stream.filter()


def find_individual_info(name):
    user = api.get_user(screen_name=name)
    print("The users follower count: " + str(user.followers_count))
    print("The users username: " + user.name)
    print("The users screen name: " + user.screen_name)
    print("The users locations: " + user.location)
    print("The users description: " + user.description)
    print("The users total listed accounts: " + str(user.listed_count))
    print("The users total number of friends: " + str(user.friends_count))
    print("The date when the user created the account: " + str(user.created_at))
    print('The user\'s url:  ' + user.url)
    print('Verified? ' + str(user.verified))


def find_list_info(list_of_following):
    for individual in list_of_following:
        find_individual_info(individual.screen_name)
        print("\n")


def follow_people(person):
    friends = api.get_friends(count=200) # max
    listofusernames = []
    for individual in friends:
        listofusernames.append(individual.screen_name)
    if not(person in listofusernames):
        api.create_friendship(screen_name=person)
        listofusernames.append(person)
        total = len(listofusernames)
        print("total people you follow: " + str(total))
        file = open("followlist.txt","w")
        for names in listofusernames:
            file.write(names + "\n")
        file.close()
    else:
        print("You already follow: " + person)
    return listofusernames


#https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule
#Read this link on how streams work before moving on


def main():
    find_individual_info('UTAustin')
    # follow_people()
    # find_list_info()


main()


# Functions that we could create:
# Info about a specific user, basically the layout about the user (optional, not really needed, but nice and quick info) (CHECK)
# Additional to the first function above, create one that loops through a list or map of users, similar to first. (CHECK)
# Create a txt file of UT associated accounts, then have a function read in that list and follow those people (CHECK)
# Create a txt file associated with two functions; a retrieve name and store name. This will make sure there aren't duplicates

# Things to do with twitterBot:
# Create daily polls about stuff (Confused a lil)
# Tweet to UT accounts, something supportive everytime they post something
# Retweet UT associated events or anything in general
# Do something when someone @'s this bot, this can be like a UT happy quote or something like that
# In addition to function on top, when someone @'s and # something specific like "event",
# we can retweet the post, and say that there is an event happening

