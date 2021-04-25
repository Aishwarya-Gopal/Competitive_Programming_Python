#minimum_subset_diff

def subset_sum(wt, w, n):
    t = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
            elif wt[i-1]<=j:
                t[i][j] = t[i-1][j-wt[i-1]] or t[i-1][j]
            elif wt[i-1]>j:
                t[i][j] = t[i-1][j]
    return t[-1]

def minimum_subset_diff(arr):
    rAnge = sum(arr); n = len(arr)
    t = subset_sum(arr, rAnge, n)
    v = [i for i in range(rAnge//2+1) if t[i]==1]
    mn = 90000
    for x in v:
        mn = min(mn, rAnge-(2*x))
    return mn
    
# wt = [2, 5, 3, 1] 
# print(minimum_subset_diff(wt)) 
