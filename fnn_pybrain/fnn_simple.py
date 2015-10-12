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

# training and test dataset creation
trndata = ClassificationDataSet(3, 1, nb_classes=2)
tstdata = ClassificationDataSet(3, 1, nb_classes=2)

# color information (RGB values)
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

print('')


for i in range(50):
    # train the network for 1 epoch
    trainer.trainEpochs(1)

    # evaluate the result on the training and test data
    trnresult = percentError(
        trainer.testOnClassData(dataset=trndata),
        trndata['class']
        )

    # print the result
    print(
        'epoch: %4d' % trainer.totalepochs,
        '  train error: %5.2f%%' % trnresult
        )

# single sample test
test_input = [27, 12, 225]
# activate the network (feedforward) using this one sample
test_output = net.activate(test_input)
# print output
print(
    '\ninput values: %d, %d, %d\noutput value: %f' %
    (test_input[0], test_input[1], test_input[2], test_output)
    )

# prepare explicit answer
answer = \
    '-----------------\n' \
    'So the color is: \n'
if test_output < 0.5:
    answer += 'red'
else:
    answer += 'blue'
# print answer
print(answer+'\n')
