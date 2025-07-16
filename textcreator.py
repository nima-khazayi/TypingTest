import random
import nltk
from nltk.corpus import words # Import the words
word_list = words.words() # Get the list of English words

def dict(num):
    nltk.download("words") # Download the words corpus
    dictionary = generate(num)
    return dictionary

def generate(num_words):
    """Used choice instead of random.sample to allow duplicate words"""
    return [random.choice(word_list) for _ in range(num_words)]
