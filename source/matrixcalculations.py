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
    gamma = 0.2
    tau = 0.02
    enter_loop(numRounds, P_his, W, N, gamma, tau)

def create_c(startingWealth, agentCount):
    temp = []
    for _ in range(agentCount):
        temp.append(startingWealth)
    return temp

def enter_loop(numRounds, P_his,W, N, gamma, tau):
    return ''

def new_matrix():
    return ''

def new_A():
    return ''

def new_B():
    return ''

main()