import time


def main():
    N = agentCount = 2

    numRounds = 10000

    startingWealth = 5


    W = agentCount*startingWealth
    K = W - 1

    h = W/(K+1)

    P_his = []
    c = create_c(startingWealth, agentCount, K)
    P_his.append(c)
    beta = 0.2
    tau = 0.0
    P_his = enter_loop(numRounds, P_his, h, c, K, W, N, beta, tau)
def create_c(startingWealth,agentCount, K):
    temp = []
    for _ in range(K+2):
        temp.append(0)
    temp[startingWealth] = agentCount
    print(temp)
    return temp
def enter_loop(numRounds, P_his, h, c, K, W, N, beta, tau):
    for _ in range(numRounds):
        P_his.append(c)
        c = next_c(h, c, K, W, N, beta, tau)
    return P_his
def next_c(h, c, K, W, N, beta, tau):
    new_c = [0] * len(c)
    for i in range(1, K+1):
        new_c[i] = new_P(i, h, N, c, K, W, beta, tau)
    print(new_c)
    return new_c
def new_P(i, h, N, c, K, W, beta, tau):
    term1 = (1 - ((2/(h**2))*(beta**2)*(((((i*h)**2)/2)*new_A(i, h, N, c, K))+new_B(h, N, i, c))))*c[i]
    term2 = (1/(2*(h**2)))*((2*(beta**2)*((((((i+1)*h)**2)/2)*new_A((i+1), h, N, c, K))+new_B(h, N, (i+1), c))) - (h*tau*((W/N)-((i+1)*h))))*c[i+1]
    term3 = (1/(2*(h**2)))*((2*(beta**2)*((((((i-1)*h)**2)/2)*new_A((i-1), h, N, c, K))+new_B(h, N, (i-1), c))) + (h*tau*((W/N)-((i-1)*h))))*c[i-1]
    return term1 + term2 + term3
def new_A(i, h, N, c, K):
    term1 = (h*c[i])/(2*N)
    term2 = 0
    for n in range(i+1, K+1):
        term2 += c[n]
    term2 = term2*(h/N)
    return term1 + term2
def new_B(h, N, i, c):
    term1 = ((h/(2*N))*(((h**2)*((2*i)-1))-h))*c[i]
    term2 = 0
    for n in range(1, i):
        term2 += ((4*(h**2))-(2*h))*c[n]
    term2 = term2*(h/(2*N))
    return term1 + term2
main()
