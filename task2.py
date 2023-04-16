#choice 1
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
text = "NLTK is a leading platform for building Python programs to work with human language data . NLTK is available for Windows , Mac OS X, and Linux . Best of all,NLTK is a free,open source,community-driven project."
print("output :",word_tokenize(text))
#==========================================
#choice 2
from nltk import sent_tokenize
text = "NLTK is a leading platform for building Python programs to work with human language data . NLTK is available for Windows , Mac OS X, and Linux . Best of all,NLTK is a free,open source,community-driven project."
print("output :",sent_tokenize(text))
#==========================================
#choice 3
text = "NLTK is a leading platform for building Python programs to work with human language data . NLTK is available for Windows , Mac OS X, and Linux . Best of all,NLTK is a free,open source,community-driven project."
print("output :",(text))
#==========================================
from nltk.tokenize import word_tokenize,sent_tokenize
text=input('enter your text :')
print('1:tokenize words / 2:tokenize sent / 3:original text')
choice=input('choose a number:')
if choice=='1':
    print(word_tokenize(text))
elif choice=='2':
    print(sent_tokenize(text))
else:
    print(text)
#===========================================