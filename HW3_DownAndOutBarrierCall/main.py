from math import e, sqrt
import numpy as np

if __name__ == "__main__":
    s = input()
    ts = s.strip().split(' ')
    S0, K, r, s, H, T, n = int(ts[0]), int(ts[1]), int(ts[2])/100, int(ts[3])/100, int(ts[4]), float(ts[5]), int(ts[6])

    deltaT = T/n
    eta = np.log(S0/H)/(s*sqrt(deltaT))
    lamb = eta/int(eta)
    #print(lamb)
    mu = r - (s**2)/2

    u = e**(lamb*s*sqrt(deltaT))
    d = u**(-1)
    pu = 1/(2*lamb**2) + (mu*sqrt(deltaT))/(2*lamb*s)#((e**(r*deltaT/2)-e**(-s*sqrt(deltaT/2)))/(e**(s*sqrt(deltaT/2))-e**(-s*sqrt(deltaT/2))))**2
    pd = 1/(2*lamb**2) - (mu*sqrt(deltaT))/(2*lamb*s)#((e**(s*sqrt(deltaT/2))-e**(r*deltaT/2))/(e**(s*sqrt(deltaT/2))-e**(-s*sqrt(deltaT/2))))**2
    pm = 1-(pu+pd)
    #print(u, d, pu, pd)
    
    S = np.zeros((n+1, 2*n+1))
    S[0, n] = S0
    
    for i in range(1, n+1):
        for j in range(n-i, n+i+1):
            if j == n-i:
                S[i, j] = S[i-1, j+1] * u
            elif j == n+i:
                S[i, j] = S[i-1, j-1] * d
            else:
                S[i, j] = S[i-1, j]
    
    # set barrier nodes to 0
    for i in range(n+1):
        for j in range(2*n+1):
            if S[i, j] <= H:
                S[i, j] = 0
    #print(S[:, 77])

    # calculate option payoffs
    V = np.zeros((n+1, 2*n+1))
    for j in range(2*n+1):
        V[n, j] = max(S[n, j]-K, 0)

    # calculate option prices at earlier time steps
    for i in range(n-1, -1, -1):
        for j in range(n-i, n+i+1):
            if S[i, j] <= H:
                V[i, j] = 0
            else:
                expected_payoff = pu * V[i+1, j-1] + pm * V[i+1, j] + pd * V[i+1, j+1]
                V[i, j] = expected_payoff*(e**(-r * deltaT))

    # calculate option price at time 0
    V0 = V[0, n]
    print(V0)

