import numpy as np

if __name__ == "__main__":
    
    use_init = False
    degree = 3
    if use_init:
        S, K, r, s, T, n, N = 101, 105, 5/100, 50/100, 3, 3, 8
    else:
        s = input()
        ts = s.strip().split(' ')
        S, K, r, s, T, n, N = float(ts[0]), float(ts[1]), float(ts[2])/100, float(ts[3])/100, float(ts[4]), int(ts[5]), int(ts[6])


    deltaT = T/n
    discount = np.exp(-r*deltaT)
    n_path = N

    if use_init:
        random_walk = np.array(
            [
                [101, 97.6424, 92.5815, 107.5178],
                [101, 101.2103, 105.1763, 102.4524],
                [101, 105.7802, 103.6010, 124.5115],
                [101, 96.4411, 98.7120, 108.3600],
                [101, 124.2345, 101.0564, 104.5315],
                [101, 95.8375, 93.7270, 99.3788],
                [101, 108.9554, 102.4177, 100.9225],
                [101, 104.1475, 113.2516, 115.0994]
            ]
        )
    else:
        ## 1. Make Random_Walk
        random_walk = np.zeros((n_path, n+1))
        ### a. Initialize price
        random_walk[:, 0] = S

        ### b. Random Walk for n steps
        for i in range(1, n+1):
            factor = np.exp((r-0.5*s*s)*deltaT + s*np.sqrt(deltaT)*np.random.normal(size=(n_path)))
            random_walk[:, i] = random_walk[:, i-1]*factor
        

    ## 2. Generate Payoff as y and t-1 price as x, then do linear regression. For n times.
    payoff = np.maximum(0, K - random_walk)
    Y = payoff[:, -1]
    for i in range(n-1, -1, -1):
        Y*=discount
        if i == 0:
            break
        hold = np.where(payoff[:, i] > 0)
        x = random_walk[hold, i][0]
        y = Y[hold]
        reg = np.polyfit(x, y, degree)
        cv = np.polyval(reg, x)
        Y[hold] = np.where(payoff[hold, i][0] >= cv, payoff[hold, i][0], Y[hold])
    
    price = np.mean(Y) if np.mean(Y) > K-S else K-S
    std = np.std(Y)/np.sqrt(n_path)
    print("Price: %.4f" % price)
    print("STD Err: %.4f" % std)
