def main():
    N = 4
    numrounds = 1000
    startingwealth = 5
    W = N*startingwealth
    k = W - 1
    h = W/(k+1)
    b = 0.2
    t = 0
    P_his = []
    P_his = loop_instance(startingwealth, numrounds, b, h, N, W, k, t, P_his)


def loop_instance(startingwealth, numrounds, b, h, N, W, k, t, P_his):
    c = (k+2)*[0]
    c[startingwealth] = N
    P_his.append(c)
    new_c = [0]*len(c)
    for _ in range(numrounds):
        for i in range(1, k+1):
            new_c[i] = NP(b, h, i, c, N, W, k, t)
        print(new_c)
        c = new_c
    return P_his

def NP(b, h, i, c, N, W, k, t):
    term1 = 1 - (2/(h**2))*(b**2)*(((((i*h)**2)*NA(i, c, h, N, k))/2)+NB(c, i, h, N))
    term1 *= c[i]
    term2 = c[i+1]/(2*(h**2))
    term2 *= (2*(b**2)*((((((i+1)*h)**2)*NA((i+1), c, h, N, k))/2)+NB(c, (i+1), h, N))) - (h*t*((W/N)-((i+1)*h)))
    term3 = c[i-1]/(2*(h**2))
    term3 *= (2*(b**2)*((((((i-1)*h)**2)*NA((i-1), c, h, N, k))/2)+NB(c, (i+1), h, N))) + (h*t*((W/N)-((i-1)*h)))
    return term1 + term2 + term3
def NA(i, c, h, N, k):
    term1 = (h*c[i])/(2*N)
    term2 = 0
    for n in range(i+1, k+1):
        term2 += c[n]
    term2 = term2*(h/N)
    return term1 + term2

def NB(c, i, h, N):
    term1 = h/(2*N)
    term1 *= (((h**2)*((2*i)-1))-h) * c[i]
    term2 = 0
    for n in range(1, i):
        term2 += ((4*(h**2)*n)-(2*h))*c[n]
    term2 *= (h/(2*N))
    return term1 + term2

main()