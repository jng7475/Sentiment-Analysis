#Sources:
- [NTLK Documentation](https://www.nltk.org/) 
- [sklearn Naive Bayes MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) 
- [Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/) 
- [Sentiment analysis Tutorial using NLTK](https://www.youtube.com/watch?v=U8m5ug9Q54M&t=4258s)
- [Vader Documentation](https://github.com/cjhutto/vaderSentiment#introduction) 
- [Vader Sentiment Analysis Article](https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/) 


#Details:
At first, without previous knowledge about Sentiment Analysis or Machine Learning in general, I had to watch a youtube tutorial in order to understand the basis of Sentiment Analysis. After watching the youtube video (link provided above), I learned about NLTK and how I can use the tools provided to manipulate and clean the text in the input.txt file. I also learned about Naive Bayes classification, how it works and how it can be used to figure out the sentiment score of a simple string.

After that I read through the NLTK and sklearn Naive Bayes MultinomialNB documentations to understand more how they work and began my project. I used the "Large Movie Review Dataset" to train my model; however, my laptop encountered some issues with memory, so I could only use 13000 out of 25000 data values after shuffling them. This raises a problem because the data set used for training is not always the same after shuffling. Then I used the model to predict the sentiment scores for each sentence from the 'input.txt' file (which have been processed). The result is either '0' which indicates that the sentence is negative or '1' which indicates that the sentence is positive. Finally, I use the mean of all the results to represent the overall sentiment score of the text file. The scores consistenly ranges from over 0.5 to over 0.6 which indicates that the text is slightly positive. This matches my prediction as the first paragraph contains some negativity while the second paragraph, which is longer, is slightly more positive. One problem is it takes more than 10 minutes everytime I compile and run the project, which I still don't have an answer for.

After finishing my project, I saw an article about Sentiment Analysis using Vader, which is a pre-trained model for Sentiment Analysis. I was fascinated as I had been spending days trying to train my own model and work with it without knowing there is a pre-trained model available. Therefore, I tried out another approach using Vader. The result I got was 0.15 (with -1 being very negative and 1 being very positive). This result is, in a certain extent, similar to the result I got from the other approach mentioned above as it indicates that the text is slightly positive. 

In general, I was able to learn something completely new to me and was able to use it. I'm still inexperienced with Machine Learning, so I know my coding might not be optimized and can be improved. I'm always willing to learn new knowlege and practice to improve technical skills, which is why I hope to be a part of ACM.
