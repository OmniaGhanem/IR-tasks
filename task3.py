# choice 4.1
from nltk.stem import PorterStemmer
word = "programming"
print("output :", PorterStemmer().stem(word))
# ==========================================
# choice 4.2
from nltk.stem.snowball import SnowballStemmer
word = 'programming'
print("output :", SnowballStemmer("english").stem(word))
#============================================
from nltk.stem.snowball import PorterStemmer,SnowballStemmer
word=input('Enter the word/sentenceb :')
print('1:porterstemmer 2: snowballstemmer')
choice=input('choose a number :')
if choice =='1':
        print("output :", PorterStemmer().stem(word))
elif choice=='2':
        print("output :", SnowballStemmer("english").stem(word))
else:
    print('output : unavailable choice')
#============================================
from nltk.stem import PorterStemmer
words= ["programming"]
for w in words:
    print("output :", PorterStemmer().stem(w))
#============================================
from nltk.stem.snowball import SnowballStemmer
word = ['programming']
for w in word:
    print("output :", SnowballStemmer("english").stem(w))
# ============================================
