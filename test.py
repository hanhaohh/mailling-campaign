import numpy as np
import scipy as sp
import sklearn
# from sklearn.cross_validation import KFold
# from sklearn.cross_validation import ShuffleSplit
# from sklearn import tree
# from sklearn.naive_bayes import GaussianNB
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import precision_score
# from sklearn.metrics import roc_auc_score
# from sklearn.metrics import confusion_matrix
import pickle
import csv
import sys

file = open('new_data.csv')
line = file.read()
file_list = line.split('\n')
headers = file_list[0].strip().split(',')
print headers

numInstance = len(file_list)-1
numFeature = len(headers)
 
num_names = ['avggift','lastgife','pgift','ampergift']
target_names = ['response']
 
numericals = np.zeros((numInstance - 1,len(num_names)))
target = np.zeros((numInstance - 1,len(target_names)))
 
for i in range(1,numInstance):
    lines= file_list[i].rstrip().split(',')
    numCount = 0;
    for j in xrange(numFeature):
        if num_names.count(headers[j]) > 0:
            numericals[i-1][numCount]=lines[j]   
            numCount = numCount + 1
        elif target_names.count(headers[j]) > 0:
                target[i-1][0] = lines[j]
 
print numericals
 
dataMat = numericals
all_headers = num_names
  
valDict={}
for num_name in num_names:
    valDict[num_name] = 1
  
def pickleIt(pyName, outputName):
    output = open(outputName+'.pk1', 'wb')
    pickle.dump(pyName, output)
    output.close()
      
pickleIt(dataMat, 'myDataMat')
pickleIt(target, 'myTarget') 
pickleIt(all_headers, 'myHeaders')
pickleIt(valDict, 'myValues')
pickleIt(num_names, 'numericalVariables')
  
#####
  
def pickleLoad(inputName):
    pk1_file = open(inputName+'.pk1', 'rb')
    pyObj = pickle.load(pk1_file)
    return pyObj
  
dataMat = pickleLoad('myDataMat')
target = pickleLoad('myTarget')
headers = pickleLoad('myHeaders')
valDict = pickleLoad('myValues') 
num_names = pickleLoad('numericalVariables')
  
target = np.ravel(target)
  


