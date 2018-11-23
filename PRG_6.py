import pandas as pd
msg = pd.read_csv('PRG_6.csv', names=['message','label'])              
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
X=msg.message
y=msg.labelnum

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest=train_test_split(X,y)  

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(xtrain)
xtest_dtm = count_vect.transform(xtest)
df=pd.DataFrame(xtrain_dtm.toarray(), columns=count_vect.get_feature_names())

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(xtrain_dtm,ytrain)
predicted = clf.predict(xtest_dtm)

from sklearn import metrics
print('ACCURACY: ',metrics.accuracy_score(ytest,predicted))
print('PRECISION: ',metrics.precision_score(ytest,predicted))
print('RECALL: ',metrics.recall_score(ytest,predicted))