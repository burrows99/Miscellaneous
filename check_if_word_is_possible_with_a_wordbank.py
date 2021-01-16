def check(word1,word2):
    if(word1==word2[:len(word1)] or word1==word2[-len(word1):]):
        return(True)
    else:
        return(False)
def f(wordbank,n,word):
    if(dp[n][len(word)]!=None):
        return(dp[n][len(word)])
    if(word==''):
        dp[n][len(word)]=True
        return(dp[n][len(word)])
    if(n==0):
        dp[n][len(word)]=False
        return(dp[n][len(word)])
    else:
        if(check(wordbank[n-1],word)):
            new_word=word.replace(wordbank[n-1],'')
            p1=f(wordbank,n,new_word)
            p2=f(wordbank,n-1,word)
            dp[n][len(word)]=p1 or p2
            return(dp[n][len(word)])
        else:
            dp[n][len(word)]=f(wordbank,n-1,word)
            return(dp[n][len(word)])
word='eeeeeeeeeeeeeeeeeeeeeeeeef'
wordbank=['eeeeef','eeeeee','eeeeeee']
n=len(wordbank)
dp=[[None]*(len(word)+1) for i in range(n+1)]
print(f(wordbank,n,word))
