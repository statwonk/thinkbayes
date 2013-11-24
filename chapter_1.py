# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:13:35 2013

@author: chris
"""

import imp

tb = imp.load_source('thinkbayes', '/home/chris/installations/python/ThinkBayes/thinkbayes.py')
from thinkbayes import Pmf

pmf = Pmf()
pmf.Set('Bowl 1', 0.5)
pmf.Set('Bowl 2', 0.5)
pmf.Mult('Bowl 1', 0.75)
pmf.Mult('Bowl 2', 0.5)
pmf.Normalize()
print pmf.Prob('Bowl 1')
print pmf.Prob('Bowl 2')

class Cookie(Pmf):
    
    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()
        
        
hypos = ['Bowl 1', 'Bowl 2']
pmf = Cookie(hypos)


