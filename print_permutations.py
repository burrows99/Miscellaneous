def permutations(array,n,o):
    if(n==0):
        print(o)
        return
    else:
        for i in array:
            permutations(array,n-1,o+str(i))
array=[1,2,3]
n=4
o=''
permutations(array,n,o)
