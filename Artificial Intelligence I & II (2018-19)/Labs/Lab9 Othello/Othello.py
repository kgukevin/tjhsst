import random
import sys
import operator
sys.setrecursionlimit(50000)
board = "??????????" + "?........?"*3 + "?...o@...?" + "?...@o...?" +"?........?"*3 + "??????????"
'''board = list(board)
board[35]="@"
board[36]="o"
board[78]="@"
board[35]="@"
board[36]="o"
board[34]="@"
board[54]="@"
board[34]="o"
board[76]="@"
board = "".join(board)
#board = "??????????" + "?........?"*8 + "??????????"'''

'''SQUARE_WEIGHTS = [
    0,   0,    0,    0,    0,    0,    0,    0,   0,   0,
    0, 220,  -20,   30,    5,    5,   30,  -20,  50,   0,
    0, -20,  -40,  -10,  -10,  -10,  -10,  -40, -20,   0,
    0,  30,  -10,   15,    3,    3,   15,  -10,  30,   0,
    0,   5,  -10,    3,    3,    3,    3,  -10,   5,   0,
    0,   5,  -10,    3,    3,    3,    3,  -10,   5,   0,
    0,  30,  -10,   15,    3,    3,   15,  -10,  30,   0,
    0, -20,  -40,  -10,  -10,  -10,   10,  -40, -20,   0,
    0,  50,  -20,   30,    5,    5,   30,  -20, 220,   0,
    0,   0,    0,    0,    0,    0,    0,    0,   0,   0,
]'''
SQUARE_WEIGHTS = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 220, -20,  45,   5,   5,  45, -20, 220,   0,
    0, -20, -80,  -5,  -5,  -5,  -5, -80, -20,   0,
    0,  45,  -5,  45,   3,   3,  45,  -5,  45,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,  45,  -5,  45,   3,   3,  45,  -5,  45,   0,
    0, -20, -80,  -5,  -5,  -5,  -5, -80, -20,   0,
    0, 220, -20,  45,   5,   5,  45, -20, 220,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]

bindex=set()
windex=set()
directions = [-1,1,10,-10,11,-11,9,-9]
def display_board(board):
    for x in range(10):
        if x == 0:
            numers = " "+"  ".join(str(x) for x in range(x*10,x*10+10))
        else:
            numers = " ".join(str(x) for x in range(x*10,x*10+10))
        temp = board[x*10:x*10+10].replace("."," ")
        print("  ".join(temp)+"    " + "  ".join(board[x*10:x*10+10]) + "   " + numers)

def count_board(board):
    global bindex
    bindex.clear()
    global windex
    windex.clear()
    for x in range(len(board)):
        if board[x]=="@":
            bindex.add(x)
        elif board[x]=="o":
            windex.add(x)
    return bindex,windex
count_board(board)
def possible_moves(board,tkn):
    '''next = set()
    #for x in (bindex if tkn == "@") else: windex:
    if tkn == "@":
        othertkn = "o"
        for x in bindex:
            temp = x
            for y in directions:
                temp+=y
                while (0 < temp+y < 100) and (0 < temp < 100) and (board[temp+y] != "?") and (board[temp]==othertkn):
                    temp+=y
                if (temp!= x+y) and (board[temp]=="."):
                    next.add(temp)
                temp = x
    if tkn == "o":
        othertkn = "@"
        for x in windex:
            temp = x
            for y in directions:
                temp+=y
                while (0 < temp+y < 100) and (0 < temp < 100) and (board[temp+y] != "?") and (board[temp]==othertkn):
                    temp+=y
                if (temp!= x+y) and (board[temp]=="."):
                    next.add(temp)
                temp = x
    next = list(next)
    next.sort()
    return next'''
    next=set()
    otkn = othertkn(tkn)
    for x in range(100):
        temp = x
        if board[temp] == tkn:
            for y in directions:
                temp += y
                while (0 < temp + y < 100) and (0 < temp < 100) and (board[temp + y] != "?") and (
                        board[temp] == otkn):
                    temp += y
                if (temp != x + y) and (board[temp] == "."):
                    next.add(temp)
                temp = x
    next = list(next)
    next.sort()
    return next

def make_move(board,tkn,pos):
    flip = []
    intermediate = []
    next = list(board)
    if tkn == "@":
        othertkn = "o"
        temp = pos
        for y in directions:
            temp+=y
            while((board[temp]!="?") and (0 < temp < 100) and (board[temp]==othertkn)):
                if (temp!=temp+y) and (board[temp]!=tkn):
                    intermediate.append(temp)
                temp += y
            if board[temp]!=tkn:
                intermediate.clear()
            else:
                flip.extend(intermediate)
                intermediate.clear()
            temp = pos
        if len(flip)!=0:
            next[pos]=tkn
            for x in flip:
                next[x]=tkn
            next = "".join(next)
    if tkn == "o":
        othertkn = "@"
        temp = pos
        for y in directions:
            temp+=y
            while((board[temp]!="?") and (0 < temp < 100) and (board[temp]==othertkn)):
                if (temp!=temp+y) and (board[temp]!=tkn):
                    intermediate.append(temp)
                temp += y
            if board[temp]!=tkn:
                intermediate.clear()
            else:
                flip.extend(intermediate)
                intermediate.clear()
            temp = pos
        if len(flip)!=0:
            next[pos]=tkn
            for x in flip:
                next[x]=tkn
            next = "".join(next)
    count_board(next)
    return next

def random_play(board):
    path = []
    count = 0
    state = board[:]
    display_board(state)
    b,w = count_board(state)
    print("black score: "+ str(len(b))+ " white score: "+str(len(w)))
    print()
    tkn1 = "@"
    tkn2 = "o"
    next1 = possible_moves(state, tkn1)
    print("possible black moves: " + str(next1))
    next2 = possible_moves(state, tkn2)
    print("possible white moves: " + str(next2))
    while (len(next1)>0) or (len(next2)>0):
        next1 = possible_moves(state, tkn1)
        if len(next1)>0:
            index = random.randint(0,len(next1)-1)
            path.append(next1[index])
            state = make_move(state,tkn1,next1[index])
            count+=1
            print("move: "+str(count)+" black move")
            print(next1)
            display_board(state)
            b, w = count_board(state)
            print("black score: " + str(len(b)) + " white score: " + str(len(w)))
        else:
            if len(next2)==0:
                break
            path.append(-1)
            print("black pass")
        print()
        print()
        next2 = possible_moves(state, tkn2)
        if len(next2)>0:
            index = random.randint(0, len(next2) - 1)
            path.append(next2[index])
            state = make_move(state,tkn2,next2[index])
            count+=1
            print("move: " + str(count) + " white move")
            print(next2)
            display_board(state)
            b, w = count_board(state)
            print("black score: " + str(len(b)) + " white score: " + str(len(w)))
        else:
            if len(next1)==0:
                break
            path.append(-1)
            print("white pass")
        print()
        print()
        #b, w = count_board(state)
    print("black: " + str(100 * len(b) / (len(b) + len(w))) + "% white: " + str(
        100 * len(w) / (len(b) + len(w))) + "%")
    print("total path: "+ str(path[:len(path)-1]))

def evaluate(board,depth):
    #display_board(board)
    b,w = count_board(board)
    temp = sum(SQUARE_WEIGHTS[x] for x in b)-sum(SQUARE_WEIGHTS[x] for x in w)
    temp+=(len(b)-len(w))*70
    '''if len(b)+len(w) <30:
        m = 30
    else:
        m=10
    temp += (len(possible_moves(board,"@"))-len(possible_moves(board,"o")))*m'''
    return temp

def minimax(board,tkn,depth):
    tkn1 = tkn
    tkn2 = othertkn(tkn)
    if (depth==0) or (len(possible_moves(board,tkn1))==len(possible_moves(board,tkn2))==0):
        return {board: evaluate(board,depth)}
    if (len(possible_moves(board, tkn1)) == 0) & (len(possible_moves(board, tkn2)) != 0):
        tkn1 = tkn2
        tkn2 = tkn
    result = dict()
    for moves in possible_moves(board,tkn1):
        next_board = make_move(board,tkn1,moves)
        #display_board(next_board)
        if tkn1 == "o":
            res = max(minimax(next_board,tkn2,depth-1).values())
        else:
            res = min(minimax(next_board,tkn2,depth-1).values())
        result[moves] = res
    return result

def alphabeta(board,tkn,depth,alpha,beta):
    tkn1 = tkn
    tkn2 = othertkn(tkn)
    if (depth==0) or (len(possible_moves(board,tkn1))==len(possible_moves(board,tkn2))==0):
        return {board: evaluate(board,depth)}
    if (len(possible_moves(board, tkn1)) == 0) & (len(possible_moves(board, tkn2)) != 0):
        tkn1 = tkn2
        tkn2 = tkn
    result = dict()
    for moves in possible_moves(board,tkn1):
        next_board = make_move(board,tkn1,moves)
        #display_board(next_board)
        if alpha>beta:
            break
        if tkn1 == "o":
            res = max(alphabeta(next_board,tkn2,depth-1,-beta,-alpha).values())
        else:
            res = min(alphabeta(next_board,tkn2,depth-1,-beta,-alpha).values())
        if res>alpha:
            alpha = res
        result[moves] = res
    return result


def othertkn(tkn):
    return "@" if tkn=="o" else "o"

def computer_turn(board, tkn,depth):
    next = alphabeta("".join(board),tkn,depth,-2000,2000)
    if tkn == "o":
        move = min(next.items(), key=operator.itemgetter(1))[0]
    else:
        move = max(next.items(), key=operator.itemgetter(1))[0]
    #display_board(board)
    return move

def random_mini_play(board,depth):
    path = []
    count = 0
    state = board[:]
    display_board(state)
    b,w = count_board(state)
    print("black score: "+ str(len(b))+ " white score: "+str(len(w)))
    print()
    tkn1 = "@"
    tkn2 = "o"
    next1 = possible_moves(state, tkn1)
    print("possible black moves: " + str(next1))
    next2 = possible_moves(state, tkn2)
    print("possible white moves: " + str(next2))
    while (len(next1)>0) or (len(next2)>0):
        next1 = possible_moves(state, tkn1)
        if len(next1)>0:
            index = random.randint(0,len(next1)-1)
            path.append(next1[index])
            state = make_move(state,tkn1,next1[index])
            count+=1
            print("move: "+str(count)+" black move")
            print(next1)
            display_board(state)
            b, w = count_board(state)
            print("black score: " + str(len(b)) + " white score: " + str(len(w)))
        else:
            if len(next2)==0:
                break
            path.append(-1)
            print("black pass")
        print()
        print()
        next2 = possible_moves(state, tkn2)
        if len(next2)>0:
            index = random.randint(0, len(next2) - 1)
            path.append(next2[index])
            state = make_move(state,tkn2,computer_turn(state,tkn2,depth))
            count+=1
            print("move: " + str(count) + " white move")
            print(next2)
            display_board(state)
            b, w = count_board(state)
            print("black score: " + str(len(b)) + " white score: " + str(len(w)))
        else:
            if len(next1)==0:
                break
            path.append(-1)
            print("white pass")
        print()
        print()
        #b, w = count_board(state)
    print("black: " + str(100 * len(b) / (len(b) + len(w))) + "% white: " + str(
        100 * len(w) / (len(b) + len(w))) + "%")
    print("total path: "+ str(path[:len(path)-1]))
    return (100 * len(w) / (len(b) + len(w)))

y=0
for x in range(1):
    y+=random_mini_play(board,4)
print(y/1)