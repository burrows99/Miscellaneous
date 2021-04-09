def display(board):
    total=list()
    for i in board:
        s=list()
        for j in i:
            s.append(str(j))
        s=' | '.join(s)
        total.append(s)
    var='\n'+('-'*len(s))+'\n'
    ans=var.join(total)
    print(ans)
def isValid(board,row,col,n):
    for i in range(n):
        if(board[row][i]=='Q'):
            return(False)
    for i in range(n):
        if(board[i][col]=='Q'):
            return(False)
    r=row
    c=col
    while((r>=0 and c>=0) and (r<n and c<n)):
        if(board[r][c]=='Q'):
            return(False)
        r=r-1
        c=c-1
    r=row
    c=col
    while((r>=0 and c>=0) and (r<n and c<n)):
        if(board[r][c]=='Q'):
            return(False)
        r=r+1
        c=c-1
    r=row
    c=col
    while((r>=0 and c>=0) and (r<n and c<n)):
        if(board[r][c]=='Q'):
            return(False)
        r=r-1
        c=c+1
    r=row
    c=col
    while((r>=0 and c>=0) and (r<n and c<n)):
        if(board[r][c]=='Q'):
            return(False)
        r=r+1
        c=c+1
    return(True)
def solve(board,row,n,N):
    if(N==0 or row>=n):
        return(True)
    else:
        for i in range(n):
            if(isValid(board,row,i,n)):
                board[row][i]='Q'
                if(solve(board,row+1,n,N-1)):
                    return(True)
                board[row][i]=' '
        return(False)
n=25
board=[[' ']*n for i in range(n)]
solve(board,0,n,n)
display(board)
