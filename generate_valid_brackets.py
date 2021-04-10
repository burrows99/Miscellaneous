def f(op,cl,o):
    if(op==0 and cl==0):
        print(o)
        return
    if(op==cl):
        f(op-1,cl,o+'(')
    if(op<cl):
        if(op>0):
            f(op-1,cl,o+'(')
        f(op,cl-1,o+')')
# def f(op,cl,o):
#     if(op==0 and cl==0):
#         print(o)
#         return
#     else:
#         if(op==0):
#             f(op,cl-1,o+')')
#         elif(cl==0):
#             f(op-1,cl,o+'(')
#         else:
#             f(op,cl-1,o+')')
#             f(op-1,cl,o+'(')
n=10
f(n,n,'')
