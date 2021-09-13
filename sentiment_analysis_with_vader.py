#Trung "Jason" Nguyen
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

with open("input.txt", "r") as test_file:
    content = test_file.read()

#remove line break
content = content.replace('\n', ' ') 
#remove period before Mr, Dr to use split()
content = content.replace("Mr. ", "Mr ")
content = content.replace("Dr. ", "Dr ")    
#split the text into sentences
test_data = content.split(".")
#put all sentences into a list
test_data = list(map(str.strip, test_data))
#change to lower for consistency
clean_data = [i.lower() for i in test_data]

#analize sentiment score function
def sentiment_scores(sentence):
     
    # Create a SentimentIntensityAnalyzer object to use analyze function
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(sentence)
     
    ## OPTIONAL: PRINT SCORES FOR EACH SENTENCE
    #print("Overall sentiment score is : ", sentiment_score)
    #print("Sentence Overall Rated As", end = " ")
    #if sentiment_score['compound'] >= 0.05 :          ## decide sentiment as positive, negative and neutral
    #    print("Positive")
    #elif sentiment_score['compound'] <= - 0.05 :
    #    print("Negative")
    #else :
    #    print("Neutral")

    return sentiment_score['compound'] #overall sentiment score of sentence
 
total_score = 0
#find sentiment score of all sentences and add them to total score
for sentence in clean_data:
    if sentence != '':
        a = sentiment_scores(sentence)
        total_score += a

#overall sentiment score of the text
input_sentiment_score = float("{:.2f}".format(float(total_score/len(clean_data))))
print(input_sentiment_score)
print("Text Overall Rated As", end = " ")
 
#decide sentiment of the entire text file as positive, negative and neutral
if input_sentiment_score >= 0.05 :
    print("Positive")

elif input_sentiment_score <= - 0.05 :
    print("Negative")

else :
    print("Neutral")

#Output:
#0.15
#Text Overall Rated As Positive

