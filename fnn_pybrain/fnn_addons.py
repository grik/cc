#! /usr/bin/env python2.7
from __future__ import print_function

__author__ = "Mikolaj Buchwald"
# Based on:
# * Example script for feed-forward network usage in PyBrain Martin Felder
# * http://stackoverflow.com/a/8143012 by c0m4

from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import ClassificationDataSet
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# ds = SupervisedDataSet(3, 2)
trndata = ClassificationDataSet(3, 1, nb_classes=2)
tstdata = ClassificationDataSet(3, 1, nb_classes=2)

color = [
    [214, 0, 0], [210, 62, 90], [147, 10, 36], [212, 52, 52],
    [229, 76, 98], [204, 0, 67], [188, 62, 109], [235, 0, 51],
    [16, 39, 213], [18, 157, 159], [53, 198, 153], [23, 119, 150],
    [0, 95, 255], [37, 74, 136], [4, 45, 196], [10, 143, 255]
    ]

# 0 is red, 1 is blue
color_class = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    1, 1, 1, 1,
    1, 1, 1, 1
    ]

# add samples to dataset
for i in range(len(color)):
    indata = color[i]
    outdata = color_class[i]
    trndata.addSample(indata, [outdata])
    print('[%d, %d, %d], [%d]' % (indata[0], indata[1], indata[2], outdata))
trndata.assignClasses()

net = buildNetwork(trndata.indim, 6, trndata.outdim)
# net = buildNetwork(
#    trndata.indim, 6, trndata.outdim, recurrent=False, bias=False
#    )
trainer = BackpropTrainer(
    net, dataset=trndata, learningrate=0.01, momentum=0.5, verbose=True
    )

# # train on dataset with X epochs
# t.trainOnDataset(ds, 50)
# t.testOnData(verbose=True)

print('')

errors = []

plt.axis([0, 50, 0, 1])
plt.ion()
plt.show()
before_first = True


for i in range(50):
    # train the network for 1 epoch
    trainer.trainEpochs(1)

    # evaluate the result on the training and test data
    trnresult = percentError(
        trainer.testOnClassData(dataset=trndata),
        trndata['class']
        )
#     tstresult = percentError( trainer.testOnClassData(
#         dataset=tstdata ), tstdata['class'] )

    # print the result
    print(
        'epoch: %4d' % trainer.totalepochs,
        '  train error: %5.2f%%' % trnresult,
        # "  test error: %5.2f%%" % tstresult
        )

    err = trainer.testOnData()
    errors.append(err)

 
'''

Additional utilities

'''
data_vis_all = np.array(color)
data_vis = [data_vis_all[0:8].T, data_vis_all[8:16].T]

def plot(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    cm = [['r', 'o'], ['b', '^'], ['g', 'x']]
    
    for i in range(len(data)):
        print(len(data))
        xs = data[i][0]
        ys = data[i][1]
        zs = data[i][2]
        ax.scatter(xs, ys, zs, c=cm[i][0], marker=cm[i][1], s=100)

    ax.scatter(90, 231, 90, c='k', marker='x', s=180)

    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')

    ax.set_xlim(0,255)
    ax.set_xlim(0,255)
    ax.set_xlim(0,255)

    plt.show()

plot(data_vis)
