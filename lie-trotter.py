import numpy as np
import math
from scipy import linalg

d = 2

def calc_exp(X, h):
    rx, Ux = linalg.eigh(X)
    Ux_inv = linalg.inv(Ux)
    tx = np.diag(np.array([math.exp(h * i) for i in rx]))
    eX = Ux.dot(tx.dot(Ux_inv))
    return eX

def trotter(X,Y,Z,h,n):
    eZ = calc_exp(Z,h)
    eX = calc_exp(X,h/n)
    eY = calc_exp(Y,h/n)
    S = np.diag(np.ones(d))
    eXeY = eX.dot(eY)
    for i in range(n):
        S = S.dot(eXeY)
    return linalg.norm(eZ - S)/linalg.norm(eZ)

def n_dependence(X,Y,Z,h):
    filename = "n.dat"
    print filename
    f = open(filename,'w')
    for i in range(100):
        n = i+1
        f.write(str(n) + " " +  str(trotter(X,Y,Z,h,n)))
        f.write("\n")
    f.close()

def h_dependence(X,Y,Z,n):
    filename = "h%x.dat" %n
    print filename
    f = open(filename,'w')
    for i in range(100):
        h = (i+1)/100.0
        f.write(str(h) + " " +  str(trotter(X,Y,Z,h,n)))
        f.write("\n")
    f.close()

np.random.seed(1)
x1 = np.random.rand(d,d)
x2 = np.random.rand(d,d)
X = x1.dot(x1.T)
Y = x2.dot(x2.T)
Z = X + Y

n_dependence(X,Y,Z,1.0)
h_dependence(X,Y,Z,1)
h_dependence(X,Y,Z,2)
h_dependence(X,Y,Z,4)
