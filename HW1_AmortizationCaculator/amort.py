if __name__ == "__main__":
    s = input()
    ts = s.strip().split(' ')
    assert len(ts) == 6, "[Error] Wrong input size. Please try again with a correct size."
    # vars
    L = int(ts[0].replace(',', ''))
    r1 = float(int(ts[1])/100)
    r2 = float(int(ts[2])/100)
    n1 = int(ts[3])
    n_year = int(ts[4])
    m = int(ts[5])

    total_t = n_year*m
    assert total_t >= n1, "[Error] n1 > n*m."
    
    # cal for const pay
    deno, total_r, r = 1, 0, 1+r1/m
    for i in range(1, n1+1):
        deno /= r
        total_r += deno
    r = 1+r2/m
    for i in range(1, total_t-n1+1):
        deno /= r
        total_r += deno
    pay = L/(total_r)

    # output amort
    print("Start writing!")
    path = "./amort.csv"
    f = open(path, 'w')
    remain, r = L, r1
    f.write(f"Time,Payment,Interest,Principal,Remaining principal\n")
    f.write(f"{0},{0},{0},{0},{remain}\n")
    for t in range(1, total_t+1):
        if t == n1+1:
            r = r2
        interest = remain*(r/12)
        prin = pay-interest
        remain -= prin
        f.write(f"{t},{round(pay, 2):.2f},{round(interest, 2):.2f},{round(prin, 2):.2f},{round(remain, 2):.2f}\n")
    f.close()