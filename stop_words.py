import re

import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOP_WORDS = set(stopwords.words('english'))
A_TO_Z = re.compile('^[a-z0-9]*$')

def stop_words(text: str):
    word_tokens = word_tokenize(text)
    filtered_sentence = [w.lower() for w in word_tokens if not w.lower() in STOP_WORDS]
    filtered_words = [w for w in filtered_sentence if A_TO_Z.match(w)]
    return filtered_words