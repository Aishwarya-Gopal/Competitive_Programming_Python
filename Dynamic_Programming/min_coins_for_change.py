#min_coins_for_change

import sys
def min_coins_for_change(wt, w, n):
    t = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if j==0:
                t[i][j] = 0
            if i==0:
                t[i][j] = sys.maxsize - 1
            elif i==1:
                if j%wt[i-1]==0:
                    t[i][j] = j//wt[i-1]
                else:
                    t[i][j] = sys.maxsize - 1
            elif wt[i-1]<=j:
                t[i][j] = min(1 + t[i][j-wt[i-1]], t[i-1][j])
            elif wt[i-1]>j:
                t[i][j] = t[i-1][j]
    return t[n][w]  
    
    
# wt = [1, 2, 3] 
# w = 5
# n = 3 
# print(min_coins_for_change(wt,w, n)) 
