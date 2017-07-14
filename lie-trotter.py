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

def trotter2nd(X,Y,Z,h,n):
    eZ = calc_exp(Z,h)
    eX = calc_exp(X,h/n*0.5)
    eY = calc_exp(Y,h/n)
    S = np.diag(np.ones(d))
    eXeYeX = eX.dot(eY.dot(eX))
    for i in range(n):
        S = S.dot(eXeYeX)
    return linalg.norm(eZ - S)/linalg.norm(eZ)


def n_dependence(X,Y,Z,h,order):
    filename = "n_%x.dat" % order
    t = trotter if order == 1 else trotter2nd
    print filename
    f = open(filename,'w')
    for i in range(100):
        n = i+1
        f.write(str(n) + " " +  str(t(X,Y,Z,h,n)))
        f.write("\n")
    f.close()

def h_dependence(X,Y,Z,n, order):
    t = trotter if order == 1 else trotter2nd
    filename = "h%x_%x.dat" %(n, order)
    print filename
    f = open(filename,'w')
    for i in range(100):
        h = (i+1)/100.0
        f.write(str(h) + " " +  str(t(X,Y,Z,h,n)))
        f.write("\n")
    f.close()

np.random.seed(1)
x1 = np.random.rand(d,d)
x2 = np.random.rand(d,d)
X = x1.dot(x1.T)
Y = x2.dot(x2.T)
Z = X + Y

n_dependence(X,Y,Z,1.0,1)
n_dependence(X,Y,Z,1.0,2)

h_dependence(X,Y,Z,1,1)
h_dependence(X,Y,Z,2,1)
h_dependence(X,Y,Z,4,1)

h_dependence(X,Y,Z,1,2)
h_dependence(X,Y,Z,2,2)
h_dependence(X,Y,Z,4,2)
