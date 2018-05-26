

from sklearn.linear_model import LogisticRegression
from sklearn import svm
import pylab as pl
import numpy as np
from sklearn import cross_validation
from sklearn.model_selection import cross_val_score
from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import train_test_split
import re

stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

tweets = []
for line in open('labeled_tweets.txt').readlines():
    items = line.split(',')
    tweets.append([int(items[0]), items[1].lower().strip()])

# Extract the vocabulary of keywords
vocab = dict()
for class_label, text in tweets:
    for term in text.split():
        term = term.lower()
        term= re.sub('[\n]+', ' ', term)
        # Remove not alphanumeric symbols white spaces
        term = re.sub(r'[^\w]', ' ', term)
        # Replace #word with word
        term = re.sub(r'#([^\s]+)', r'\1', term)
        # Remove :( or :)
        term = term.replace(':)', '')
        term = term.replace(':(', '')
        # trim
        term = term.strip('\'"')
        if len(term) > 2 and term not in stopwords:
            if vocab.has_key(term):
                vocab[term] = vocab[term] + 1
            else:
                vocab[term] = 1
#print vocab
# Remove terms whose frequencies are less than a threshold (e.g., 15)
vocab = {term: freq for term, freq in vocab.items() if freq > 83}
print '********Question:2********'
print 'List of Top 10 Features:'
print vocab
# Generate an id (starting from 0) for each term in vocab
vocab = {term: idx for idx, (term, freq) in enumerate(vocab.items())}
print 'Total Number of features selected:'
print len(vocab)

print '*********Question-3********'
# Generate X and y Arrays
X = []
y = []
for class_label, text in tweets:
    x = [0] * len(vocab)
    terms = [term for term in text.split() if len(term) > 2]
    for term in terms:
        if vocab.has_key(term):
            x[vocab[term]] += 1
    y.append(class_label)
    X.append(x)
print 'X-Array:'
#print len(X)
print X
print 'Y-Array:'
print y
#print len(y)


print '********Question-4********'
# 10 folder cross validation to estimate the best w and b

X_train, X_test, y_train, y_test, = train_test_split(X, y, test_size=0.1, random_state = 0)
#print X_train.shape, y_train.shape
#print X_test.shape, y_test.shape

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print clf.score(X_test, y_test)

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, X, y, cv=10)
print scores

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2 ))

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],'C': [1, 10, 100, 1000]},{'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
scores = ['precision', 'recall']
svr = svm.SVC(C=1)
for score in scores:
    print("# Tuning hyper-parameters for %s"% score)
    clf =GridSearchCV(svr, tuned_parameters, cv=10,scoring='%s_macro'% score)
    clf.fit(X_train, y_train)
    print("best parameters %s" % clf.best_params_)
   # means = clf.cv_results_['mean_test_score']
    #stds = clf.cv_results_['std_test_score']
    #for mean, std, params in zip(means, stds, clf.cv_results_['params']):
     #   print("%0.3f (+/-%0.03f) for %r"% (mean, std *2, params))
    #_true, y_pred = y_test, clf.predict(X_test)



# predict the class labels of new tweets
#print clf.predict(X)
tweets = []
for line in open('unlabeled_tweets.txt').readlines():
    tweets.append(line)

# Generate X for testing tweets
print '********Question-5********'
X = []
for text in tweets:
    x = [0] * len(vocab)
    terms = [term for term in text.split() if len(term) > 2]
    for term in terms:
        if vocab.has_key(term):
            x[vocab[term]] += 1
    X.append(x)
y = clf.predict(X)

# print unlabeled tweets and their class labels
myfile = open('predicted_tweets.txt', 'w')
for idx in range(1,438):
    print 'Sentiment Class (1 means positive; 0 means negative): ', y[idx]
    print 'TEXT: ', idx, tweets[idx]
    myfile.write('%d,%s\n'%(y[idx],tweets[idx]))
myfile.close()



print sum(y), len(y)
