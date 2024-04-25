import re

import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOP_WORDS = set(stopwords.words('english'))

def stop_words(text: str):
    word_tokens = word_tokenize(text)
    filtered_sentence = [w.lower() for w in word_tokens if not w.lower() in STOP_WORDS]
    a_to_z = re.compile('^[a-z0-9]*$')
    filtered_words = [w for w in filtered_sentence if a_to_z.match(w)]
    return filtered_words