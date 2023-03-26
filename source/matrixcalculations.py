import numpy as np
from scipy import linalg


def new_matrix(C,i,j,h,g,W,N,T):
    A = new_A(C,i,h,N,t,k)
    B = new_B(C,i,h,N,t,k)


def new_A(C, i,h,N,t,k):
    coeffSum = 0
    for j in range(i+1, k):
        coeffSum += C[t][j-1] + (h/2*N)*C[t][i-1]
    return (h/N)*coeffSum

def new_B(C,i,h,N,t,k):
    return ''