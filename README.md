# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!


##SUBMISSION DETAILS

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
