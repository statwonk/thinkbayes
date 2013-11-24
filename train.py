# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:08:52 2013

@author: chris
"""
import imp
tb = imp.load_source('thinkbayes', '/home/chris/installations/python/ThinkBayes/thinkbayes.py')
from thinkbayes import Pmf
from thinkbayes import Suite

class Dice(Suite):
    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0/hypo

class Train(Dice):
    def __init__(self, hypos, alpha = 1.0):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, hypo**(-alpha))
        self.Normalize()
            
hypos = xrange(1, 1001)
suite = Train(hypos)
suite.Update(30)
suite.Update(60)
suite.Update(90)
# suite.Print()

def Mean(suite):
    total = 0
    for hypo, prob in suite.Items():
        total += hypo * prob
    return total
    
print Mean(suite)

def Percentile(pmf, percentage):
    p = percentage / 100.0
    total = 0
    for val, prob in pmf.Items():
        total += prob
        if total >= p:
            return val

interval = Percentile(suite, 5), Percentile(suite, 95)
print interval