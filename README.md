# :tangerine: Trump Tweet Generator v2.0
Trumpbot was my attempt at creating a RNN trained on Donald Trumps(DT) tweets. I used this as a sort of practice project for learning a bit about RNN's and Tensorflow 2. The result was a chaos and a learning experience so let's dive in.


## :rocket: Setup
Setup is pretty straightforward. It only needs numpy and tensorflow 2 alpha just run the start pip install:

    pip3 install -r requirements.txt


## :chart_with_upwards_trend: Dataset & Training

The entire dataset was just tweets scraped from the DT twitter account. I used Jefferson Henrique's library [GetOldTweets-python](https://github.com/Jefferson-Henrique/GetOldTweets-python) that I modified a little bit. All the raw tweets can be found in the raw_tweets.txt file FYI all the links in any tweet have been removed.

The first thing about using Tweets as a dataset for training is that they are filled with garbage that wreaks havoc when training. Heres what I did:

- Removed any links or urls to photos
- Simplified all the puncuation, with Trump this is a big thing, his tweets are a clown fiesta of periods and exclemation marks.
- Cleaned out any invisible or non-english characters, any foreign characters just casuases trouble.
- Removed the '@' symbol, I'll explain why later.
- Removed the first couple of months of tweets, they were mostly about the celebrity apprentice and not really core to what I was trying to capture.
- Removed any retweets or super short @replies

The final training text is in tweets.txt which altogether is about 20,000 tweets.



## Credit and Contact

Created by Wyatt Ferguson 

For any comments or questions your can reach me on Twitter [@wyattferguson](https://twitter.com/wyattferguson) or visit my little portfolio at [wyattf.dev](https://wyattf.dev)
