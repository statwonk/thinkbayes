# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:57:59 2013

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
            
suite = Dice([4, 6, 8, 12, 20])
suite.Update(6)

for roll in [6, 8, 7, 7, 5, 4]:
    suite.Update(roll)    

suite.Print()