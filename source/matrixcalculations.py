import numpy as np
from scipy import linalg




def main():
    N = 32
    agentCount = 32
    numRounds = 100
    K = 1000
    startingWealth = 1000
    W = agentCount*startingWealth
    maxWealth = agentCount*startingWealth
    h = W/K+1
    P_his = []
    P_his.append(create_c(startingWealth,agentCount))

def create_c(startingWealth, agentCount):
    temp = []
    for _ in range(agentCount):
        temp.append(startingWealth)
    return temp

def new_matrix():
    return ''

def new_A():
    return ''

def new_B():
    return ''

main()