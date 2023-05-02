from nltk.sentiment import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

def sia(s):
   return sid.polarity_scores(s)['compound']

