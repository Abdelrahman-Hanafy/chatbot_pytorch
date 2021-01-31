import nltk
from nltk import PorterStemmer

#nltk.download('punkt')
stemmer = PorterStemmer()

# make tokenization for the sentence 
def tokenize(sent):
    return nltk.word_tokenize(sent)
# stem and lower the tokenized words
def stem(wrd):
    return stemmer.stem(wrd.lower())
# create the word bag for the sentence
def bagging(tok_sent, all_wrds):
    pass

