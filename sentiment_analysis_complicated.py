#Trung "Jason" Nguyen
import os
import glob
import nltk
from nltk.tokenize import  RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random
nltk.download('stopwords')

#Open input.txt file
with open("input.txt", "r") as test_file:
    content = test_file.read()

#Remove line break and period after Mr, Dr to split into sentences
content = content.replace('\n', ' ')
content = content.replace("Mr. ", "Mr ")
content = content.replace("Dr. ", "Dr ")    
#split the text into sentences
test_data = content.split('.')
#put all sentences into a list
test_data = list(map(str.strip, test_data))
  
#Get positive data from folder 'pos'
positive_data = []
path = 'pos'
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(os.path.join(os.getcwd(), filename), 'r', encoding="utf8") as f:
       positive_content = f.read()
       positive_data.append(positive_content)

#Get negative data from folder 'neg'
negative_data = []
path = 'neg'
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(os.path.join(os.getcwd(), filename), 'r', encoding="utf8") as f:
       negative_content = f.read()
       negative_data.append(negative_content)

#create objects used to clean data
tokenizer = RegexpTokenizer(r'\w+')
eng_stopwords = set(stopwords.words('english'))
porter_stemmer = PorterStemmer()

def clean_data(text):
    text = text.lower()
    tokens = tokenizer.tokenize(text) 
    new_words = [token for token in tokens if token not in eng_stopwords]
    stemmed_words = [porter_stemmer.stem(word) for word in new_words]
    clean_text = " ".join(stemmed_words)
    return clean_text

#Clean positive and negative data sets
positive_data_cleaned = [clean_data(i) for i in positive_data]
negative_data_cleaned = [clean_data(i) for i in negative_data]

#2 arrays in which 1 indicates positive and 0 indicates negative
y_positive = []
y_negative = []
for token in positive_data_cleaned:
    y_positive.append('1')
for token in negative_data_cleaned:
    y_negative.append('0')

#Merge array -> 2 big data sets content and positive/negative
data_list = positive_data_cleaned + negative_data_cleaned
y = y_positive + y_negative

#shuffle 2 list in unison
c = list(zip(data_list, y))
random.shuffle(c)
data_list, y = zip(*c)

#training data
X_train = data_list[:13000]
y_train = y[:13000]

#test data taken from input.txt
X_test =  [clean_data(i) for i in test_data if i != '']                   

#Vectorization
cv = CountVectorizer(ngram_range=(1,2))
data_vec = cv.fit_transform(X_train).toarray()
test_vec = cv.transform(X_test).toarray()

#Training and predict
mn = MultinomialNB()
mn.fit(data_vec, y_train)
pred = mn.predict(test_vec) #prediction of sentiment for each sentence

print(pred) #print the prediction

#Calculate overall score of the entire text
total_score = 0
for pr in pred:
    total_score += int(pr)
overall_score = float(total_score/len(X_test))
print("The overall sentiment score of the text is: " + str(overall_score))

#OUTPUT example
#['0' '0' '1' '1' '1' '0' '1' '1' '0' '0' '1' '0' '0' '1' '1' '1' '1' '1'
#'1' '1' '1' '1']
#0.681818181

#['1' '0' '0' '0' '0' '0' '1' '1' '0' '0' '1' '0' '0' '0' '1' '1' '1' '1'
#'1' '1' '1' '1']
#0.5454545454545454