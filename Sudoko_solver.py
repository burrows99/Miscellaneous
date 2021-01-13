board=[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end="    ")
            if((j+1)%3==0 and j<8):
                print("|",end=" ")
        print("\n")
        if((i+1)%3==0 and i<8):
            print('- - - - - - - - - - - - - - - - - - - - - - -')
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j]==0):
                return([i,j])
    return(None)
def valid(board,position,num):
    row=position[0]
    coloumn=position[1]
    #check coloumn
    ans=True
    for i in range(len(board)):
        if(board[i][coloumn]==num):
            return(False)
    #check row
    for i in range(len(board[0])):
        if(board[row][i]==num):
            return(False)
    #check grid
    box_r=int(row/3)
    box_c=int(coloumn/3)
    for i in range(box_r*3,box_r*3 + 3):
        for j in range(box_c*3,box_c*3 + 3):
            if(board[i][j]==num and [i,j]!=position):
                return(False)
    return(ans)
def solve(board):
    position=find_empty(board)
    if(not position):
        return(True)
    else:
        row=position[0]
        coloumn=position[1]
    for i in range(1,10):
        if(valid(board,position,i)):
            board[row][coloumn]=i
            if(solve(board)):
                return(True)
            board[row][coloumn]=0
    return(False)
print_board(board)
print('\n')
print('After solving:')
solve(board)
print_board(board)
