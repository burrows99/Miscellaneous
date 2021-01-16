import sys
sys.setrecursionlimit(10**6)
def f(a,n,s):
    if(dp[n][s]!=None):
        return(dp[n][s])
    if(s==0):
        dp[n][s]=[]
        return(dp[n][s])
    if(n==0):
        dp[n][s]=[False]
        return(dp[n][s])
    else:
        if(a[n-1]<=s):
            p1=[a[n-1]]+f(a,n,s-a[n-1])
            p2=f(a,n-1,s)
            if(False in p1):
                dp[n][s]=p2
            elif(False in p2):
                dp[n][s]=p1
            else:
                if(len(p1)<len(p2)):
                    dp[n][s]=p1
                else:
                    dp[n][s]=p2
        else:
            dp[n][s]=f(a,n-1,s)
        return(dp[n][s])
a=[3,4,5,68]
s=30
n=len(a)
dp=[[None]*(s+1) for i in range(n+1)]
print(f(a,n,s))
