def f(array,o,n):
    if(n==0):
        print(o)
        return
    else:
        o1=o
        o2=str(array[n-1])+o
        f(array,o1,n-1)
        f(array,o2,n-1)
array=[1,2,3]
o=''
n=len(array)
f(array,o,n)
        
#            ''
#         /      \
#       3        ''
#     /  \      /  \
#   23   3     2   ''
#  /  |  | \  / |  | \
# 123 23 13 3 12 2 1 ''
