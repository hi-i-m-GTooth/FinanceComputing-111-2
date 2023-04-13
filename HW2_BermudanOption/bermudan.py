from math import e, sqrt
if __name__ == "__main__":
    s = input()
    ts = s.strip().split(' ')
    S, K, r, s, T, n = int(ts[0]), int(ts[1]), int(ts[2])/100, int(ts[3])/100, float(ts[4]), int(ts[5])

    deltaT = T/n
    u = e**(s*sqrt(deltaT))
    d = u**(-1)
    p = (e**(r*deltaT)-d)/(u-d)
    leafs = []
    # init leafs
    for i in range(n+1):
        val = K - S * u**(2*i-n) + 1
        leafs.append(val if val>=0 else 0)
    
    # move
    for j in range(n-1, 0-1, -1):
        for i in range(j+1):
            leafs[i] = (p*leafs[i+1] + (1-p)*leafs[i])*(e**(-r*deltaT))
            exercise = max(K - S*u**(2*i-j) + 1, 0)
            if (j == int(n*(1/4)) or j == int(n*(3/4))) and (leafs[i] < exercise): leafs[i] = exercise

    print(leafs[0])

