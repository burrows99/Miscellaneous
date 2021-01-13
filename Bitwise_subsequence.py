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

def condition(x,y):
    if((x&y)*2<(x|y) and x<=y):
        return(True)
    else:
        return(False)
def subsequence(a,i):
    start=a[i]
    j=i+1
    A=list()
    while(j<len(a)):
        if(condition(a[i],a[j])):
            A.append(a[j])
            i=j
            j=i+1
        else:
            j=j+1
    A.insert(0,start)
    return(A)
def F(a):
    ans=0
    for i in range(len(a)):
        s=subsequence(a,i)
        if(ans<len(s)):
            ans=len(s)
    return(ans)

a=[15,6,5,12,1]
b=[9,17,2,15,5,2]
c=[17,16,12,2,8,17,17]
print(F(a))
print(F(b))
print(F(c))
# time complexity : n**2
