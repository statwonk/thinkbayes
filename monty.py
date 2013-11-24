"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

tb = imp.load_source('thinkbayes', '/home/chris/installations/python/ThinkBayes/thinkbayes.py')
from thinkbayes import Pmf
from thinkbayes import Suite

class Monty(Suite):
    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1

suite = Monty('ABC')
suite.Update('A')
suite.Print()
