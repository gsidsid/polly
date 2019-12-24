import twitter
import re 

api = twitter.Api(consumer_key="SuAasV1Bz4JyV6dJs3JSvmtuh",
                  consumer_secret="HaSiLPfeOmt9jJKopX9ioQ4JVgMKVdyVCnupcj0YJp3z5cyWQs",
                  access_token_key="1130029381106061312-ds9I54ZOxizb4K2GvlYMtZ3CWXr9pp",
                  access_token_secret="0dRP5ifH29CWLoibtTRzDzclIPzyR1YVgEAHaFgEL7cN9")

def get_tweets(api=None, screen_name=None):
    #print("getting tweets for:", screen_name)
    timeline = api.GetUserTimeline(screen_name=screen_name, count=200, include_rts=False, exclude_replies=True)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    #print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200, include_rts=False, exclude_replies=True
        )
        
        new_earliest = None
        if len(tweets) > 0:
            new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            #print("getting tweets before:", earliest_tweet)
            timeline += tweets

    return timeline

  
def urls_in_text(string): 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
    return url 

screen_names = ["CaucasianJames"]

for screen_name in screen_names:
    timeline = get_tweets(api=api, screen_name=screen_name)
    originals = [tweet.text for tweet in timeline if not tweet.media and len(urls_in_text(tweet.text)) == 0]

    with open("data/" + screen_name + ".txt", 'w+') as f:
        for tweet in originals:
            try:
                f.write(str(tweet))
                f.write('\n')
            except:
                continue;
