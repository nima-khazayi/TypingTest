import random
import nltk
from nltk.corpus import words

# Check if the words corpus is already downloaded
try:
    words.words()
except LookupError:
    nltk.download("words")  # Download the words corpus if not already present

word_list = words.words()  # Get the list of English words

def dict(num, n):
    """Generate a list of words of the specified number"""
    dictionary = generate(num, n)
    return dictionary

def generate(num_words, n):
    """Used choice instead of random.sample to allow duplicate words"""
    """Generate a list of words with 7 letters or less, ensuring the list length equals num_words"""
    filtered_words = [word for word in word_list if len(word) <= n]
    
    result = []
    while len(result) < num_words:
        result.append(random.choice(filtered_words))
    
    return result