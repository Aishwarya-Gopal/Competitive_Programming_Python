#number of ways of finding change for n coins with {x, y, z} denominations

def num_ways_coin_change(wt, w, n):
    t = [[0 for i in range(w+1)] for j in range(n)]
    for i in range(n):
        for j in range(w+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
            elif wt[i-1]<=j:
                t[i][j] = t[i][j-wt[i-1]] + t[i-1][j]
            elif wt[i-1]>j:
                t[i][j] = t[i-1][j]
    return t[n-1][w]
