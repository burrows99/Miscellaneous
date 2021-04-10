def merge(string,space_comb,n):
    d={'0':'','1':' '}
    i=0
    new=''
    while(i<n-1):
        new+=string[i]+d[space_comb[i]]
        i=i+1
    new+=string[i]
    return(new)
def permutations(array,n,o):
    global ans
    if(n==0):
        ans.append(o)
        return
    else:
        for i in array:
            permutations(array,n-1,o+str(i))
string='abcdef'
array=[0,1]
n=len(string)-1
o=''
ans=list()
permutations(array,n,o)
for i in ans:
    print(merge(string,i,n))
