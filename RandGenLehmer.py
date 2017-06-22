import time
import numpy as np
import matplotlib.pyplot as plt

def g (x, m, a, q, r):

    t = a * (x % q) - r * (x / q)
    if t <= 0: t+=m
    
    #print('t')
    #print (t)
    return t

def genSeed():
    t = time.time()
    #print(t)
    t=int((t-int(t))*10**6)
    #print(t)
    return t

class randGenLehmer:
    
    def __init__(self,seed=0):
        self.seed = 0
        if(seed == 0):
            seed = genSeed()
        self.i = 0
        self.ini = seed
        self.current = seed
    
    m = 2147483647
    a = 48271
    q = 44488
    r = 3399
    
    def nextRand(self, startint=0., endint=1.):
        rand = g(self.current, self.m, self.a, self.q, self.r)
        self.i+=1
        self.current = rand
        return (startint+(rand/self.m)*(endint-startint))