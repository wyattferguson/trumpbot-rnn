# Trumpbot v1.0
Trumpbot was my attempt at creating a RNN trained on Donald Trumps(DT) tweets. I used this as a sort of practice project for learning a bit about RNN's and Tensorflow 2. The result was a chaos and a learning experience so lets dive in.

## Run with Containers

### Docker

If you don't want to install dependencies to your host, you can build a Docker container
with the included Dockerfile:

```bash
$ docker build -t trumpbot .
```

The entrypoint is the script to generate the tweets:

```bash
$ docker run trumpbot
...
 obamas Top and France at 900 PM on FoxNews. Anderson Congratulations to the House vote for MittRomney o

 hillary Clinton has been a total disaster. I have an idea for her great speech on CNN in the world  a great honor for me and his partisan hotel and every spor

 friends support Trump International Golf Club on the Paris About that Right School is started by the DNC and Clinton and the DNC that will be a great show with t
```

If you want to interact with the container (perhaps training first) you can shell inside instead:

```bash
$ docker run -it --entrypoint bash trumpbot
root@b53b98f12c34:/code# ls
Dockerfile  README.md  __init__.py  learn.py  raw_tweets.txt  requirements.txt	training_checkpoints  trumpbot.py  tweets.txt
```

You'll be in the `/code` directory that contains the source code. 

### Singularity

For users that want to perhaps use GPU (or better leverage the host) the recommendation is to
use a [Singularity](https://www.sylabs.io/guides/3.2/user-guide/) container, and a recipe file [Singularity](Singularity) is provided
to build the container.

```bash
$ sudo singularity build trumpbot.sif Singularity
```

And then to run (add the --nv flag if you want to leverage any host libraries).

```bash
$ singularity run trumpbot.sif
```

If you need to change the way that tensorflow or numpy are installed, you can edit the Singularity or Docker recipes.

## Setup
Setup is pretty straightforward. It only needs numpy and tensorflow 2 alpha just run the start pip install:

    pip3 install -r requirements.txt


## Dataset

The entire dataset was just tweets scraped from the DT twitter account. I used Jefferson Henrique's library [GetOldTweets-python](https://github.com/Jefferson-Henrique/GetOldTweets-python) that I modified a little bit. All the raw tweets can be found in the raw_tweets.txt file FYI all the links in any tweet have been removed.

The first thing about using Tweets as a dataset for training is that they are filled with garbage that wreaks havoc when training. Heres what I did:

- Removed any links or urls to photos
- Simplified all the puncuation, with Trump this is a big thing, hes tweets are a clown fiesta of periods and exclemation marks.
- Cleaned out any invisible or non-english characters, any foreign characters just casuases trouble.
- Removed the '@' symbol, I'll explaid why later.
- Removed the first couple of months of tweets, they were mostly about the celebrity apprentice and not really core to what I was trying to capture.
- Removed any retweets or super short @replys

The final training text is in tweets.txt which altogether is about 20,000 tweets.

## Training
I trained the model twice, the first time for 30 epochs which took around 6 hours. The result was absolute garbage, at the time I hadnt removed hidden or foreign characters so it took 6 hours to spit out complete nonsense. So after I cleaned out the tweets again, I ran the training over night for 50 epochs this time.

Just run the learn file to train it again if you want, the model check points are store in the 'training_checkpoints' folder

    python3 learn.py


## Generating Tweets
So now the fun part, you can run the command:

    python3 trumpbot.py

This will generate 10 tweets from a random group of topics. If you open the trumpbot.py file theres a few things you can play with:

    tweets - Number of messsages you want generated

    temperature - This controls how predictable the tweet will be, by 
    default its random from 0.1 -> 0.4, anything above about 0.7 generates
     garbage.

    talking_points - Is a list of inputs to feed the network, try out 
    differnt words and see what works.

    num_generate - This controls the length of the message you want to
     get generated.

## Result
For my first crack at text generation Im happy with the results. Here are some sample tweets:

    hillary Clinton has been a total disaster. If you cant admit that 
    the U.S. more than has been treated big baster I am a g

    Donald Trump is 45% Iran

    healthe lobbyist now wants to raise taxes for our country in the 
    first place! If only one thing is clea

    friends support Trump Rally Anger Golf Club of Caporate legislation 
    at the WhiteHouse today! #MakeAmericaGreatAgain Thank you for your
     support! #Trump2016 

    koreau like you it was great being in the last election then will be
     a great show. I have a fan o

    koreau lies and losers and losers will be a great show with the U.S.
     The President has a various past c


## What I learned

- Tweets make for a tough training set. Things like @ mentions just polute the hell out of the text so unless you want your bot to be constantly @ing everything I need to find a better way to deal with that.

- Things I thought the bot would love talking about stuff like #MAGA, russia, china, collusion just generate garbage strings.

- Text generation is really hard, and takes a ton of training time. 

- I could probably get a bit better results if I let it train a bit longer but for any drastic improvements I probably need to try another method or spend alot more time tuning the training set.

- Pick a subject that doesnt tweet like hes a dad yelling at a little league game. I think because his tweets are short little outbursts its hard to generate a predictable pattern across them.

- The words it groups together for differnt topics is probably worth looking at, like whenever you use 'hillary' as a input it usually has the words 'liar' or 'disaster' in the sentence. or how it loves telling you when its gonna be on @Foxandfriends

- With the method I used spelling its like to add random 'u' infront of words.

I feel like this is good starting point, and with some work we might have a digital orange man bot in our future.


## Credit and Contact

Created by Wyatt Ferguson 

For any comments or questions your can reach me on Twitter [@wyattferguson](https://twitter.com/wyattferguson) or visit my little portfolio at [wyattf.dev](https://wyattf.dev)
