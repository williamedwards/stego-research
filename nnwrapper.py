#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     
#
# Author:      William
#
# Created:     23/01/2014
# Copyright:   (c) William 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pybrain.tools.shortcuts import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

class ANN:
    def __init__(self, hlayers=1, hnodes=10, lrate = 10):
        self.hlayers = hlayers
        self.hnodes = hnodes
        self.lrate = lrate
        
    def get_params(self, deep=True):
        return {"hlayers":self.hlayers,"hnodes":self.hnodes,"lrate":self.lrate}
    
    def set_params(self, **params):
        for parameter, value in params.items():
            setattr(self,parameter,value)
        return self
    

    def fit(self, data, target):
        # Initialize the Network
        self.net = FeedForwardNetwork()
        layers = []
        layers.append(LinearLayer(data.shape[1]))
        for i in xrange(0, self.hlayers):
            layers.append(SigmoidLayer(self.hnodes))
        layers.append(LinearLayer(1))
        connections = []
        for i in xrange(1,len(layers)):
            connections.append(FullConnection(layers[i-1],layers[i]))
        self.net.addInputModule(layers[0])
        for i in xrange(1,len(layers)-1):
            self.net.addModule(layers[i])
        self.net.addOutputModule(layers[len(layers)-1])
        for connection in connections:
            self.net.addConnection(connection)
        self.net.sortModules()
        
        #Build data set
        self.data = SupervisedDataSet(data.shape[1],1)
        for datum, trgt in zip(data,target):
            self.data.addSample(datum, trgt)         
                
        #Begin training process
        b = BackpropTrainer(self.net, self.data, learningrate=self.lrate)
        self.train(b)
        
    def train(self, b):
        b.train()
        
    def predict(self, inp):
        return [0 if self.net.activate(i)<0.5 else 1 for i in inp]

        
    
