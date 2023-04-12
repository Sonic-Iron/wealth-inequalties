def main():
    agentCount = 32

    N = 32

    numRounds = 100

    startingWealth = 1000


    W = agentCount*startingWealth
    K = agentCount*startingWealth


    h = W/K+1

    P_his = []
    P_his.append(create_c(startingWealth, agentCount, K))
    print(P_his)
    gamma = 0.2
    tau = 0.02
    #enter_loop(numRounds, P_his, W, N, gamma, tau)

def create_c(startingWealth,agentCount, K):
    temp = []
    for _ in range(K):
        temp.append(0)
    temp[startingWealth-1] = agentCount
    return temp

def enter_loop(numRounds, P_his, W, N, gamma, tau):
    return ''

def new_P():
    return ''

def new_A(i, h, N, c,):
    term1 = (h*c[i+1])
    return

def new_B():
    return ''

main()