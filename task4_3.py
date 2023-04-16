#tokenization
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
text="this is an examle to apply tokenization.I am new here."
token=word_tokenize(text)
print(token)
token2=sent_tokenize(text)
print(token2)