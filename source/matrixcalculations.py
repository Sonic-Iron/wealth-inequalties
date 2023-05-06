from GameInstance import generate_gini_coefficient
from decimal import Decimal

def main():
    N = agentCount = 32
    numRounds = 100000
    startingWealth = 3
    W = agentCount*startingWealth
    K = int((W-1))
    h = W/(K+1)
    P_his = []
    c = create_c(startingWealth, agentCount, K)
    beta = 0.2
    tau = 0.0
    P_his, G_his = enter_loop(startingWealth, numRounds, P_his, h, c, K, W, N, beta, tau)

def create_c(startingWealth,agentCount, K):
    temp = [0]*(K+2)
    temp[startingWealth] = agentCount
    return temp
def enter_loop(startingWealth, numRounds, P_his, h, c, K, W, N, beta, tau):
    G_his = ''
    P_his = ''
    for num in range(numRounds):
        G_his += '('+str(num)+','+str(gen_gini_matrix(W, c, h))+')'
        P_his += '('+str(num)+','+str(c)+')'
        c = next_c(h, c, K, W, N, beta, tau)
    return P_his, G_his
def next_c(h, c, K, W, N, beta, tau):
    new_c = [0] * len(c)
    for i in range(1, K+1):
        new_c[i] = new_P(i, h, N, c, K, W, beta, tau)
    for a in range(len(new_c)):
        new_c[a] = N * new_c[a]/sum(new_c)
    print(sum(new_c), sum([p*c[p] for p in range(len(new_c))]), new_c)
    return new_c
def new_P(i, h, N, c, K, W, beta, tau):
    constant_hb = (2/(h**2))*(beta**2)
    term1a = new_A(i, h, N, c, K)
    term1b = new_B(h, N, i, c)
    ih_squ_div2 = ((i*h)**2)/2
    term1 = (1 - (constant_hb*((ih_squ_div2*term1a)+term1b)))*c[i]
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
    h_constant = (h**3)/(24*N)
    term1 = 6*(i**2) - 4*i + 1
    term1 *= c[i]

    term2 = 0
    for n in range(1, i):
        term2 += (6*(n**2) + 1)*c[n]
    return (term1 + term2)*h_constant

def gen_gini_matrix(W, c, h):
    area = 0
    total_wealth = sum([p*c[p] for p in range(len(c))])

    prop_pop_pre = 0
    prop_wealth = 0
    for popnum in range(len(c)):
        popnum_pop = c[popnum]/sum(c) - prop_pop_pre
        prop_pop_pre += c[popnum]/sum(c)






    return area


main()
