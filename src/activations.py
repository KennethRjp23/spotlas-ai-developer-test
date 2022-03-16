# Description: activation functions and its derivatives
import numpy as np

def f1(x):
    return np.tanh(x)

def f1_prime(x):
    return 1-np.tanh(x)**2

def f2(x):
    return 1/(1-np.exp(-x))

def f2_prime(x):
    return ( 1/(1-np.exp(-x) ) * ( 1 - (1/(1-np.exp(-x)) )))