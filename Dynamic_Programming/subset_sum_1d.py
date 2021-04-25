#Subset_sum 1D space

def subset_sum(arr, k, n):
    t = [ 0 for i in range(k+1)]
    t[0] = 1
    for i in range(n):
        for j in range(k-arr[i],-1,-1):
            if t[j]:
                t[j+arr[i]] = 1
    return t[k]
    
# wt = [2, 5, 3, 1, 10, 7] 
# w = 11
# n = 6
# t = [[0 for i in range(w+1)] for j in range(n+1)]
# print("Possible" if subset_sum(wt, w, n) else "Not Possible") 
