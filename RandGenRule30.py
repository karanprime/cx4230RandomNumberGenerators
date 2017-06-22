import time
import numpy as np
import matplotlib.pyplot as plt

def show_grid (grid):
    plt.matshow (grid)

class randGen30:
    rule30 = [0,1,1,1,1,0,0,0]
    
    def __init__(self,seed=0):
        self.seed = seed
        self.i = 0
        if(self.seed == 0):
            t = time.time()
            t = int((t-int(t))*10**6)
            s = str(bin(t))

        else:
            s = str(bin(int(self.seed)))
            if(len(s) > 33):
                s = s[0:33]
        
        s = s[2:]
        self.state = np.zeros(33)
        n = 16 - int(len(s)/2)
        for i in range(len(s)):
            self.state[n+i] = int(s[i])
        

    def nextRand(self, startint=0, endint=1):
        
        ca = self.state
        ca_next = np.zeros(33)
        
        randnum = np.zeros(16)
        randnum[0] = ca[16]

        for i in range(1,16):
            ca_next = np.zeros(33)
            n = int(ca[32]*4+ca[0]*2+ca[1]*1)
            ca_next[0] = randGen30.rule30[n]
            for j in range(1,32):
                n = ca[j-1]*4+ca[j]*2+ca[j+1]*1
                n = int(n)
                ca_next[j] = randGen30.rule30[n]
            n = int(ca[31]*4+ca[32]*2+ca[0]*1)
            ca_next[32] = randGen30.rule30[n]
            randnum[i]= ca_next[16]
            ca = ca_next
            
        self.state = ca
        rstr = ''.join(str(e) for e in randnum.astype(int))
        return(startint+(int(rstr,2)/65536.0)*(endint-startint))

#p = randGen30()
#print(p.nextRand())