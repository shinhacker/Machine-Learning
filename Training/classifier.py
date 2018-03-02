# Author : Shin McCold 
# Reference Siraj Weekly Challenge Accepted 1 
# About : Machine Learning & Neural Networks classifiers using various Models in Sklearn

from sklearn import tree
from sklearn import neural_network
from sklearn import neighbors
clf = tree.DecisionTreeClassifier()  # Decision Tree Classifier 1 

clf2 =neural_network.MLPClassifier()  #Neural Classifier 2


clf3 =neighbors.KNeighborsClassifier()  #Neighbors Classifier 3


X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
'female', 'male', 'male']   

 

clf = clf.fit(X,Y)
clf2 = clf2.fit(X,Y)
clf3 = clf3.fit(X,Y)


prediciton = clf.predict([[170,70,43]])
prediciton2 = clf2.predict([[170,70,43]])
prediciton3 = clf3.predict([[170,70,43]])

print (prediciton)
print (prediciton2)  # Seems neural network is little fishy
print (prediciton3)
