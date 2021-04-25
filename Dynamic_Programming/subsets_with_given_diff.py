#subsets_with_given_diff

def count_subset_sum(wt, w, n):
    t = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
            elif wt[i-1]<=j:
                t[i][j] = t[i-1][j-wt[i-1]] + t[i-1][j]
            elif wt[i-1]>j:
                t[i][j] = t[i-1][j]
    return t[n][w]

def subsets_with_given_diff(arr, diff):
    rAnge = sum(arr)
    s1 = (rAnge+diff)//2
    return count_subset_sum(arr, s1, len(arr))
  
# wt = [2, 1, 1, 3] 
# diff = 1
# print(subsets_with_given_diff(wt, diff)) 
