from GameInstance import generate_gini_coefficient
from decimal import Decimal

def main():
    N = agentCount = 4
    numRounds = 1000
    startingWealth = 10
    W = agentCount*startingWealth
    K = 10
    h = W/(K+1)
    P_his = []
    c = create_c(startingWealth, agentCount, K)
    P_his.append(c)
    beta = 0.2
    tau = 0.0
    P_his, G_his = enter_loop(startingWealth, numRounds, P_his, h, c, K, W, N, beta, tau)

def create_c(startingWealth,agentCount, K):
    temp = [0]*(K+2)
    temp[startingWealth] = agentCount
    print(temp)
    return temp
def enter_loop(startingWealth, numRounds, P_his, h, c, K, W, N, beta, tau):
    G_his = ''
    for num in range(numRounds):
        G_his += '('+str(num)+','+str(generate_gini_coefficient(startingWealth, c))+')'
        P_his.append(c)
        c = next_c(h, c, K, W, N, beta, tau)
    return P_his, G_his
def next_c(h, c, K, W, N, beta, tau):
    new_c = [0] * len(c)
    for i in range(1, K+1):
        new_c[i] = new_P(i, h, N, c, K, W, beta, tau)
    print(sum(new_c), new_c)
    return new_c
def new_P(i, h, N, c, K, W, beta, tau):
    constant_hb = (2/(h**2))*(beta**2)
    term1a = new_A(i, h, N, c, K)
    term1b = new_B(h, N, i, c)
    ih_squ_div2 = ((i*h)**2)/2
    term1 = (1 - (constant_hb*((ih_squ_div2*term1a)+term1b)))*c[i]
    assert term1 >= 0
    term2newa = new_A((i+1), h, N, c, K)
    term2newb = new_B(h, N, (i-1), c)
    term2 = (1/(2*(h**2)))*((2*(beta**2)*((((((i+1)*h)**2)/2)*term2newa)+term2newb)) - (h*tau*((W/N)-((i+1)*h))))*c[i+1]
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
    h_over_2N = h/(2*N)

    term1 = (4*((i*h)**3)) - (4*(((i-1)*h)**3))
    term1 *= term1*((i-1)*h)
    term1 -= 3 * ((i * h) ** 4)
    term1 += 3 * (((i-1) * h) ** 4)
    term1 *= 1/(24*h)
    term2 = 0
    for n in range(1, i):
        term2 += 0
    term2 = term2
    return (term1 + term2)*h_over_2N

main()
