# Bitwise subsequence
# You have an array A of N integers A1 A2 .. An. Find the longest increasing subsequence Ai1 Ai2 .. Ak (1 <= k
# <= N) that satisfies the following condition:
# • For every adjacent pair of numbers of the chosen subsequence Ai[x] and Ai[x+1] (1 < x < k), the expression(
# Ai[x] & Ai[x+1] ) * 2 < ( Ai[x] | Ai[x+1] ) is true

# Note: '&' is the bitwise AND operation, ' | ' is the bit-wise OR operation
# Input:
# The first line contains an integer, N, denoting the number of elements in A.
# Each line i of the N subsequent lines (where 0 ≤ i < N) contains an integer describing Ai.

# Sample Cases:
# Input Output Output Description
# 5     2      One possible subsequence is: 5 12
# 15
# 6
# 5
# 12
# 1
# -----------------------------------------------------------------------------------------------------------------
# 6     2      One possible subsequence is: 2 15
# 9
# 17
# 2
# 15
# 5
# 2
# -----------------------------------------------------------------------------------------------------------------
# 7     3     One possible subsequence is: 2 8 17 
# 17
# 16
# 12
# 2
# 8
# 17
# 17

def f(array,index,n,memo):
    if(memo[index]!=-1):
        return(memo[index])
    elif(index>=n-1):
        memo[index]=[array[n-1]]
        return([array[n-1]])
    else:
        p=list()
        a=array[index]
        for i in range(index+1,n):
            b=array[i]
            if(a<b and ((a and b)*2<a or b)):
                p.append([array[index]]+f(array,i,n,memo))
        try:
            memo[index]=max(p,key=len)
        except:
            memo[index]=[array[index]]
        return(memo[index])
def F(array):
    n=len(array)
    global_max=list()
    memo=[-1]*n
    for i in range(n):
        global_max.append(f(array,i,n,memo))
    return(max(global_max,key=len))
a=[15,6,5,12,1]
b=[9,17,2,15,5,2]
c=[17,16,12,2,8,17,17]
print(F(a))
print(F(b))
print(F(c))
# time complexity : n**2
