def main():
    agentCount = 64

    N = 32

    numRounds = 100

    startingWealth = 1000


    W = agentCount*startingWealth
    K = W - 1

    h = W/(K+1)

    P_his = []
    P_his.append(create_c(startingWealth, agentCount, K))
    gamma = 0.2
    tau = 0.02
    enter_loop(numRounds, P_his, W, N, gamma, tau, K)

def create_c(startingWealth,agentCount, K):
    temp = []
    for _ in range(K+1):
        temp.append(0)
    temp[startingWealth] = agentCount
    return temp

def enter_loop(numRounds, P_his, W, N, gamma, tau, K):
    for i in range(0, K-1):
        pass

def new_P():
    return ''

def new_A(i, h, N, c, K):
    term1 = (h*c[i])/(2*N)
    term2 = 0
    for a in range(i+1, K+1):
        term2 += c[a]
    term2 = term2*(h/N)
    return term1 + term2

def new_B(h, N, i, c):
    term1 = ((h/(2*N))*(((h^2)*((2*i)-1))-h))*c[i]
    term2 = 0


main()
