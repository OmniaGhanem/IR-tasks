import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

document = "we try to delete stopwords from the document like in and the "

words = nltk.word_tokenize(document)

modified_words = [word for word in words if word.lower() not in stopwords.words('english')]

modified_document = ' '.join(modified_words)

print(modified_document)