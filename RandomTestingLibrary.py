import RandGenRule30 as R30
import RandGenLehmer as RLCG
import time
import numpy as np
import scipy.stats as stats
from pylab import show,hist,subplot,figure
import matplotlib.pyplot as plt


#Returns rng objects with that seed
def setSeed(seed=0):
    if(seed):
        np.random.seed(seed)
    r3 = R30.randGen30(seed)
    le = RLCG.randGenLehmer()
    return r3, le

#Box-Muller Transformation from http://glowingpython.blogspot.com/2013/01/box-muller-transformation.html
def makeGaussian(u1,u2):
    z1 = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
    z2 = np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)
    return z1,z2

#Statistics for the uniform distribution
def UniformStats(u):
    print("Expected mean for a perfectly uniform distribution: ")
    mu1 = (len(u))/2000
    print(mu1)
    print("Actual mean: ")
    print(np.mean(u))
    print()
    
    kurt = -6/5
    print("Expected kurtosis for a perfectly uniform distribution: ")
    #mu1 = (len(u))/2
    print(kurt)
    print("Actual kurtosis: ")
    print(stats.kurtosis(u,0,True))
    print()
    print(stats.kstest(u,'uniform'))
    print()

    xax = np.arange(len(u))
    
    figure()
    f,a1 = plt.subplots()
    a1.scatter(xax,u)
    a1.set_title('Scatter')
    show()
    figure()
    f,a1 = plt.subplots()
    a1.plot(xax,np.sort(u),'b')
    a1.set_title('CDF')
    show()
    figure()
    hist(u)
    show()

#Statistics for gaussian distribution
def GaussianStats(u1,u2):
    z1,z2 = makeGaussian(u1,u2)
    
    kurt = 3
    print("Expected kurtosis for a perfectly uniform distribution: ")
    #mu1 = (len(u))/2
    print(kurt)
    print("Actual kurtosis: ")
    print(stats.kurtosis(z1,0,False))
    print(stats.kurtosis(z2,0,False))
    print()
    print(stats.kstest(z1,'norm'))
    print(stats.kstest(z2,'norm'))
    print()
    xax = np.arange(len(z1))
    
    figure()
    subplot(221) # the first row of graphs
    plt.scatter(xax,z1)     # contains the histograms of u1 and u2 
    subplot(222)
    plt.scatter(xax,z2)
    show()
    figure()
    subplot(221) # the first row of graphs
    plt.plot(xax,np.sort(z1),'b')     # contains the histograms of u1 and u2 
    subplot(222)
    plt.plot(xax,np.sort(z1),'b')
    show()
    figure()
    subplot(221) # the first row of graphs
    hist(z1)    # contains the histograms of u1 and u2 
    subplot(222)
    hist(z2)
    show()
def initialize(size, seed, doprint = True):
    r3, le = setSeed(seed)
    r3a = np.zeros(size)
    lea = np.zeros(size)
    start1 = time.time()
    
    for i in range(size):
        r3a[i] = r3.nextRand()
    end1 = time.time() - start1
    if doprint:print("Time taken in seconds to create Rule 30 random numbers: "+str(end1) )
    
    start2 = time.time()
    for i in range(size):
        lea[i] = le.nextRand()
    end2 = time.time() - start2
    if doprint:print("Time taken in seconds to create Lehmer random numbers: "+str(end2) )
    
    start3 = time.time()
    pyr = np.random.rand(size)
    end3 = time.time() - start3
    if doprint:print("Time taken in seconds to create NumPy random numbers: "+str(end3) )
    
    if doprint: print("Numpy is "+str(end2/end3)+" times faster than lehmer")
    if doprint: print("Lehmer is "+str(end1/end2)+" times faster than Rule30")
    if doprint: print("Numpy is "+str(end1/end3)+" times faster than Rule30")
    return r3a, lea, pyr  