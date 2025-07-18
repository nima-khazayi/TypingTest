import random
import nltk
from nltk.corpus import words

# Check if the words corpus is already downloaded
try:
    words.words()
except LookupError:
    nltk.download("words")  # Download the words corpus if not already present

word_list = words.words()  # Get the list of English words

def dict(num):
    """Generate a list of words of the specified number"""
    dictionary = generate(num)
    return dictionary

def generate(num_words):
    """Used choice instead of random.sample to allow duplicate words"""
    return [random.choice(word_list) for _ in range(num_words)]