import numpy as np

def getaround(row,col):
    res = []
    x = np.arange(max(col -1, 0),min(col + 2, 8))
    y = np.arange(max(row -1, 0),min(row + 2, 8))
    for i in x:
        for j in y:
            res.append((j,i))
    try:
        res.remove((row,col))
    except:
        pass
    return res


def getunknow(board,check_num):
    result = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    for row in range(len(board)):
        for col in range(len(board[0])):
            num = 0
            around = getaround(row,col)
            for place in around:
                if board[place[0]][place[1]] in check_num:
                    num += 1
            result[row][col] = num
    
    return result