#!/usr/bin/python3
from flask import Flask
from flask import request
from config import *
import controller.behavior as behavior_controller


import numpy as np
import matplotlib.pyplot as plt
import operator
#import scipy
#from scipy.special import expit
import matplotlib



# app = Flask(__name__)


# @app.route('/hello', methods=['GET'])
# def hello():
#     return "Hello, Group 2!"


# @app.route('/api/behavior', methods=['POST'])
# def update_data():
#     return behavior_controller.load_behavior(request.json)


# @app.route("/api/behavior", methods=['GET'])
# def get_behavior():
#     return behavior_controller.get_behavior(request.json)

# @app.route("/api/abnormal", methods=['GET'])
# def get_abnormal():
#     return behavior_controller.get_abnormal(request.json)


# calculate the distance
def euclidean_distance(vector1, vector2):
    return np.sqrt(np.sum(np.power(vector1-vector2, 2)))
def absolute_distance(vector1, vector2):
    return np.sum(np.absolute(vector1-vector2))

def get_neighbours(X_train, X_test_instance, k):
    distances = []
    neighbors = []
    for i in range(0, X_train.shape[0]):
        dist = absolute_distance(X_train[i], X_test_instance)
        distances.append((i, dist))
    distances.sort(key=operator.itemgetter(1))
    for x in range(k):
        #print distances[x]
        neighbors.append(distances[x][0])
    return neighbors

def predictkNNClass(output, y_train):
    classVotes = {}
    for i in range(len(output)):
#         print output[i], y_train[output[i]]
        if y_train[output[i]] in classVotes:
            classVotes[y_train[output[i]]] += 1
        else:
            classVotes[y_train[output[i]]] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    #print sortedVotes
    return sortedVotes[0][0]

def kNN_test(X_train, X_test, Y_train, Y_test, k):
    output_classes = []
    for i in range(0, X_test.shape[0]):
        output = get_neighbours(X_train, X_test[i], k)
        predictedClass = predictkNNClass(output, Y_train)
        output_classes.append(predictedClass)
    return output_classes

def prediction_accuracy(predicted_labels, original_labels):
    count = 0
    for i in range(len(predicted_labels)):
        if predicted_labels[i] == original_labels[i]:
            count += 1
    #print count, len(predicted_labels)
    return float(count)/len(predicted_labels)


if __name__ == '__main__':
    #app.run(debug=APP_DEBUG_MODE, host=APP_HOST)
    form = {
        "behaviorType" : "ProcessBehavior",
        "endpointID" : "DESKTOP-3LRRD6K",
        "startDate" : "2020-04-08",
        "endDate" : "2020-04-08",
        "pageSize" : "10",
        "pageIndex" : "0"
    }

    log = behavior_controller.get_behavior(form)+behavior_controller.get_abnormal(form)
    # for i in log:
    #     print(i['attckids'])

    #check the common json items
    items = []
    for i in log[0]:
        check = True
        for j in log:
            if i not in j:
                check = False
                break
        if check:
            items.append(i)
    
    #load x and y values
    x = []
    y = []
    threat_type = {"":0}
    type_count = 1

    for i in log:
        temp = []
        if i['attckids'] not in threat_type:
            threat_type[i['attckids']] = type_count
            y.append(type_count)
            type_count += 1
        else:
            y.append(threat_type[i['attckids']])
        
        for j in items:
            if i[j] == '':
                temp.append(0)
            else:
                temp.append(len(i[j].split(' ')))
        x.append(temp)

    # set up the train and test numbers
    leng = len(x)
    X_train = np.asarray(x[:int(leng*0.7)])
    y_train = np.asarray(y[:int(leng*0.7)])
    X_test = np.asarray(x[int(leng*0.7):])
    y_test = np.asarray(y[int(leng*0.7):])

    print(kNN_test(X_train, X_test, y_train, y_test, 8))
    
