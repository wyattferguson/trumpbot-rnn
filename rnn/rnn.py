from textgenrnn import textgenrnn

textgen = textgenrnn()

# textgen.train_from_file('./data/raw_tweets.txt', num_epochs=1)
textgen.generate(10,temperature=0.2)