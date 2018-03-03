#Tutorial how to use python textblob for sentimental analysis
#Author : Shin McCold


from textblob import TextBlob

wiki = TextBlob("I am happy")
print wiki.tags  # the tags assosicated with it
print wiki.words # words associated with it
print wiki.sentiment.polarity # sentiment associated with it
