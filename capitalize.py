import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# text="delhi is the capital of india.and it is one of the most beautiful city in india." #-->if you are fetching the input from the DB
def capitalize():
    text=input("Enter the  meaningfull sentence")
    # tokenize the text into words
    words = nltk.word_tokenize(text)
    # apply POS-tagging on words
    tagged_words = nltk.pos_tag([word.lower() for word in words])
    # apply capitalization based on POS tags
    capitalized_words = [w.capitalize() if t in ["PROPN","NNS","NN"] else w for (w,t) in tagged_words]
    # capitalize first word in sentence
    capitalized_words[0] = capitalized_words[0].capitalize()
    # join capitalized words
    capital_lized = re.sub(" (?=[\.,'!?:;])", "", ' '.join(capitalized_words))
    return capital_lized
capitalize()
