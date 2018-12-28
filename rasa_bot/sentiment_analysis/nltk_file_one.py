from nltk

from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.corpus import state_union

example_text = 'Hello Mr. Sherlock Homes, how are you doing today? The weather is great and python is awesome. The sky is pinkish-blue. You should not eat cartboard.'

# print(sent_tokenize(example_text))
# print(word_tokenize(example_text))

# for word in word_tokenize(example_text):
#     print(word)

example_sentence = 'This is an example showing off stop word filteration.'

stop_words = set(stopwords.words("english"))
# print(stop_words)

words = word_tokenize(example_sentence)
filtered_sentence = []

# for word in words:
#     if word not in stop_words:
#         filtered_sentence.append(word)
#
# print(filtered_sentence)

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

# for word in example_words:
#     print(ps.stem(word))

new_words = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly atleast once."

words = word_tokenize(new_words)

# for word in words:
#     print(ps.stem(word))

