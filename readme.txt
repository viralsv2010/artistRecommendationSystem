Dataset :: https://drive.google.com/open?id=1z2OVLnKbeGAXrdhVHWYFuyopnK3YpBMi


Tasks Completed so far:

Folder :: Checkpoint 1 \


1) We have collected 1500 tweets for location Albany, New York using Twitter Rest API.

2) Merged generated dataset files and converted into a single data file(api-data.txt) file.

3) After that, we removed duplicate tweets using Python script removeDuplicatetweets.py, which will 
generate file having no duplicate tweets named "removeDuplicates.txt".

4) Then, just for our knowledge we created sentiment_analysis.py file to generate the positive and negative tweets in postive.txt and negative.txt file.

5) Next, to remove excess data, we did data processing on the tweets using preprocessor.py and generated the fruitful data file named preprocessed.txt.

6) We created one script file named scriptfromTweetstoCSV.py can convert any text file to csv and output as output.csv.

7) There is one report file in the folder with the name Report.pdf which has all the task details.


Folder :: Checkpoint 2 \


7) We have labeled the tweets collected as positive and negative and stored them in ‘Checkpoint 2 \Svm\labeled_tweets.txt’. There is also one file named "Checkpoint 2 \Svm\unlabeled_tweets.txt" which will be testing dataset and svm.py is the script file for classification.

8) Then, we found the top 10 features after removing the trivial words, spaces, alpha-numeric characters, etc.

9) After applying SVM classifier and 10-fold cross validation on the labeled dataset, we got ‘Checkpoint 2 \Svm\predicted_tweets.txt’, which has predicted class labels for the tweets which had not been labeled manually using script svm.py.

10) For finding association rules, we have used "Checkpoint 2 \Association_Rule\alternate.py" script to get the tweets in the proper format.

11) Script_to_get_dataInList.py is used to get data from the dataset file as a list and stores it into Music_Words.txt

12) Python script "Checkpoint 2 \Association_Rule\association_rule.py" produces association rules of the dataset and stores the association rules to the file named “Checkpoint 2 \Association_Rule\result.txt”

13) There is one report file in the folder with the name Report-2.pdf which has all the task details.

14) Converted the "Checkpoint 2 \Association_Rule\result.txt" file to csv file named "script\result.csv".

15) Made a python script "script\script.py" in the folder named "Checkpoint 2 \script.py" which will sort the "script\result.csv" file and generate the final output file named "finaloutput.csv" without any duplicate data.