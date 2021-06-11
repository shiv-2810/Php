from textblob import TextBlob
import tweepy
import sys


def percentage(part, whole):
    return 100 * float(part) / float(whole)


API_key = "uRChDJ7xtVmnCNLNYHyBDyzAx"
API_Key_Secret = "wOoDemNfzMhgSxy123VUxVxmRySd1iAA8IdCQ29fNFEh02K8Yq"
Access_Token = "1386950375475802112-rSN24fzEZqSY4lATllmrKN0DLIfPgk"
Access_Token_Secret = "SnGwQ9d7FnOZzxBbWtN4lxjcU3GPyoPUEsjNJZroBPfmb"

Auth_Handler = tweepy.OAuthHandler(consumer_key=API_key, consumer_secret=API_Key_Secret)
Auth_Handler.set_access_token(Access_Token, Access_Token_Secret)

API = tweepy.API(Auth_Handler)

search_terms = "happiness"
tweet_amount = 100

tweets = tweepy.Cursor(API.search, q=search_terms, lang="en").items(tweet_amount)

polarity = 0
positive = 0
strongly_positive = 0
weakly_positive = 0
negative = 0
strongly_negative = 0
weakly_negative = 0
neutral = 0

for tweet in tweets:
    # print(tweet.text)
    final_text = tweet.text.replace("RT", "")
    if final_text.startswith(" @"):
        position = final_text.index(":")
        final_text = final_text[position + 2 :]
    if final_text.startswith("@"):
        position = final_text.index(" ")
        final_text = final_text[position + 2 :]
    if final_text.startswith(" @"):
        position = final_text.index(" ")
        final_text = final_text[position + 2 :]

    # print(final_text)
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0.00 and tweet_polarity <= 0.3:
        weakly_positive += 1
    elif tweet_polarity > 0.3 and tweet_polarity <= 0.6:
        positive += 1
    elif tweet_polarity > 0.6 and tweet_polarity <= 1:
        strongly_positive += 1
    elif tweet_polarity > -0.3 and tweet_polarity <= 0.00:
        weakly_negative += 1
    elif tweet_polarity > -0.6 and tweet_polarity <= -0.3:
        negative += 1
    elif tweet_polarity > -1 and tweet_polarity <= -0.6:
        strongly_negative += 1
    elif tweet_polarity == 0.00:
        neutral += 1
    polarity += tweet_polarity
    print(final_text)
print()
print()
print()
print("polarity of the given tweets is:")
print(polarity)
print()
print("Amount of tweets:")
print(f"Amount of weakly_positive tweets: {weakly_positive}")
print(f"Amount of positive tweets: {positive}")
print(f"Amount of strongly_positive tweets: {strongly_positive}")
print(f"Amount of weakly_negative tweets: {weakly_negative}")
print(f"Amount of negative tweets: {negative}")
print(f"Amount of strongly_negative tweets: {strongly_negative}")
print(f"Amount of neutral tweets: {neutral}")

positive = strongly_positive + weakly_positive + positive
negative = strongly_negative + weakly_negative + negative

positive = percentage(positive, tweet_amount)
negative = percentage(negative, tweet_amount)
neutral = percentage(neutral, tweet_amount)
polarity = percentage(polarity, tweet_amount)

print()
print()
print("Detailed Report: ")
print(str(positive) + "% people thought it was positive")
print(str(negative) + "% people thought it was negative")
print(str(neutral) + "% people thought it was neutral")
