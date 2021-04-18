import random
import time
import operator
board = "??????????" + "?........?"*3 + "?...o@...?" + "?...@o...?" +"?........?"*3 + "??????????"

"GOOD DEFAULT WEIGHTING"
# SQUARE_WEIGHTS1 = [
#     0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#     0, 120, -20,  20,  10,  10,  20, -20, 120,   0,
#     0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
#     0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
#     0,  10,  -5,   3,   3,   3,   3,  -5,  10,   0,
#     0,  10,  -5,   3,   3,   3,   3,  -5,  10,   0,
#     0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
#     0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
#     0, 120, -20,  20,  10,  10,  20, -20, 120,   0,
#     0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
# ]
SQUARE_WEIGHTS1 = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   10, - 4,   3,   3,   3,   3, - 4,   10,   0,
    0, - 4, - 6,  -0,  -1,  -1,  -0, - 6, - 4,   0,
    0,   3,  -0,   2,   1,   1,   2,  -0,   3,   0,
    0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
    0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
    0,   3,  -0,   2,   1,   1,   2,  -0,   3,   0,
    0, - 4, - 6,  -0,  -1,  -1,  -0, - 6, - 4,   0,
    0,   10, - 4,   3,   3,   3,   3, - 4,   10,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]
# SQUARE_WEIGHTS1=[
# 0,0,0,0,0,0,0,0,0,0,
# 0,4, -3, 2, 2, 2, 2, -3, 4,0,
# 0,-3, -4, -1, -1, -1, -1 ,-4 ,-3,0,
# 0,2, -1, 1, 0, 0, 1 ,-1, 2,0,
# 0,2, -1, 0 ,1, 1, 0 ,-1,2,0,
# 0,2 ,-1, 0, 1, 1, 0, -1, 2,0,
# 0,2, -1, 1, 0, 0, 1, -1, 2,0,
# 0,-3, -4, -1, -1 ,-1, -1, -4, -3,0,
# 0,4 ,-3 ,2, 2, 2, 2, -3, 4,0,
# 0,0,0,0,0,0,0,0,0,0,
# ]

SQUARE_WEIGHTS2 =  [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   10, - 4,   3,   3,   3,   3, - 4,   10,   0,
    0, - 4, - 6,  -0,  -1,  -1,  -0, - 6, - 4,   0,
    0,   3,  -0,   2,   1,   1,   2,  -0,   3,   0,
    0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
    0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
    0,   3,  -0,   2,   1,   1,   2,  -0,   3,   0,
    0, - 4, - 6,  -0,  -1,  -1,  -0, - 6, - 4,   0,
    0,   10, - 4,   3,   3,   3,   3, - 4,   10,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]
SQUARE_WEIGHTSblack =  [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   10, - 4,   3,   3,   3,   3, - 4,   10,   0,
    0, - 4, - 6,  -0,  -1,  -1,  -0, - 6, - 4,   0,
    0,   3,  -0,   2,   1,   1,   2,  -0,   3,   0,
    0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
    0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
    0,   3,  -0,   2,   1,   1,   2,  -0,   3,   0,
    0, - 4, - 6,  -0,  -1,  -1,  -0, - 6, - 4,   0,
    0,   10, - 4,   3,   3,   3,   3, - 4,   10,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]
SQUARE_WEIGHTSwhite =  [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   10, - 4,   3,   3,   3,   3, - 4,   10,   0,
    0, - 4, - 6,  -0,  -1,  -1,  -0, - 6, - 4,   0,
    0,   3,  -0,   2,   1,   1,   2,  -0,   3,   0,
    0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
    0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
    0,   3,  -0,   2,   1,   1,   2,  -0,   3,   0,
    0, - 4, - 6,  -0,  -1,  -1,  -0, - 6, - 4,   0,
    0,   10, - 4,   3,   3,   3,   3, - 4,   10,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]

oldr = 1
bindex = set()
windex = set()
directions = [-1, 1, 10, -10, 11, -11, 9, -9]
def count_board(board):
    bindex = board.count("@")
    windex = board.count("o")
    return bindex, windex
def index(board):
    global bindex
    bindex.clear()
    global windex
    windex.clear()
    for x in range(10,89):
         if board[x] == "@":
             bindex.add(x)
         elif board[x] == "o":
             windex.add(x)
    return bindex,windex
def othertkn(tkn):
    return "@" if tkn == "o" else "o"


def possible_moves(board, tkn):
    next = set()
    otkn = othertkn(tkn)
    for x in range(10,89):#bindex if tkn == "@" else windex:
        temp = x
        if board[temp]==tkn:
            for y in directions:
                temp += y
                while (10 < temp + y < 89) and (10 < temp < 89) and (board[temp + y] != "?") and (
                        board[temp] == otkn):
                    temp += y
                if (temp != x + y) and (board[temp] == "."):
                    next.add(temp)
                temp = x
    next = list(next)
    next.sort()
    return next

def make_move(board, tkn, pos):
    flip = []
    intermediate = []
    next = list(board)
    otkn = othertkn(tkn)
    temp = pos
    for y in directions:
        temp += y
        while ((board[temp] != "?") and (0 < temp < 100) and (board[temp] == otkn)):
            if (temp != temp + y) and (board[temp] != tkn):
                intermediate.append(temp)
            temp += y
        if board[temp] != tkn:
            intermediate.clear()
        else:
            flip.extend(intermediate)
            intermediate.clear()
        temp = pos
    if len(flip) != 0:
        next[pos] = tkn
        for x in flip:
            next[x] = tkn
        #bindex.update(flip)
        next = "".join(next)
    return next


def evaluate(board,old,tkn1,tkn2):
    global alltemp
    global SQUARE_WEIGHTS1
    global SQUARE_WEIGHTS2
    global SQUARE_WEIGHTSblack
    global SQUARE_WEIGHTSwhite
    #display_board(board)
    b,w = index(board)
    temp = 0
    next1 = possible_moves(board,tkn1)
    for moves in next1:
        tempboard = make_move(board,tkn1,moves)

        #Q2 This one place where my code changes strategies. The weighting of the board changes based on the stability
        #of the board. More stable pieces are weighted higher.

        # if moves not in [11,12,13,14,15,16,17,18,21,31,41,51,61,71,81,82,83,84,85,86,87,88,28,38,48,58,68,78]:
        #     tempe = moves
        #     for y in directions:
        #         tempe += y
        #         while (10 < tempe + y < 89) and (10 < tempe < 89) and (tempboard[tempe + y] != "?") and (
        #                 tempboard[tempe] == tkn1):
        #             tempe+=y
        #             if tempboard[tempe]=="." or tempboard[tempe+y]=="?":
        #                 SQUARE_WEIGHTS1[moves] += 1
        #             else:
        #                 SQUARE_WEIGHTS1[moves] -= 1
        if moves in [11, 12, 13, 14, 15, 16, 17, 18]:
            step = 1
            count = 0
            st = False
            en = False
            start = 11
            end = 18
            for x in [11, 12, 13, 14, 15, 16, 17, 18]:
                if tempboard[x]==tkn1:
                    if count == 0:
                        start = x
                        st = True
                    count+=1
                else:
                    if count > 0:
                        end = x-step
                        en = True
                if st == en == True:
                    if tempboard[start - step] == tempboard[end + step] == "?":
                        SQUARE_WEIGHTS1[moves] += count + 4
                    elif tempboard[start-step]==tempboard[end+step]==tkn2:
                        SQUARE_WEIGHTS1[moves] += count+3
                    elif tempboard[start-step]==tempboard[end+step]==".":
                        SQUARE_WEIGHTS1[moves] += count+3
                    else:
                        SQUARE_WEIGHTS1[moves] -= (count+3)
                    st = en = False
                    count = 0

        if moves in [81,82,83,84,85,86,87,88]:
            step = 1
            count = 0
            st = False
            en = False
            start = 81
            end = 88
            for x in [81,82,83,84,85,86,87,88]:
                if tempboard[x]==tkn1:
                    if count == 0:
                        start = x
                        st = True
                    count+=1
                else:
                    if count > 0:
                        end = x-step
                        en = True
                if st == en == True:
                    if tempboard[start - step] == tempboard[end + step] == "?":
                        SQUARE_WEIGHTS1[moves] += count + 4
                    elif tempboard[start-step]==tempboard[end+step]==tkn2:
                        SQUARE_WEIGHTS1[moves] += count+3
                    elif tempboard[start-step]==tempboard[end+step]==".":
                        SQUARE_WEIGHTS1[moves] += count+3
                    else:
                        SQUARE_WEIGHTS1[moves] -= (count+3)
                    st = en = False
                    count = 0
        if moves in [11,21,31,41,51,61,71,81]:
            step = 10
            count = 0
            st = False
            en = False
            start = 11
            end = 81
            for x in [11,21,31,41,51,61,71,81]:
                if tempboard[x]==tkn1:
                    if count == 0:
                        start = x
                        st = True
                    count+=1
                else:
                    if count > 0:
                        end = x-step
                        en = True
                if st == en == True:
                    if tempboard[start - step] == tempboard[end + step] == "?":
                        SQUARE_WEIGHTS1[moves] += count + 4
                    elif tempboard[start-step]==tempboard[end+step]==tkn2:
                        SQUARE_WEIGHTS1[moves] += count+3
                    elif tempboard[start-step]==tempboard[end+step]==".":
                        SQUARE_WEIGHTS1[moves] += count+3
                    else:
                        SQUARE_WEIGHTS1[moves] -= (count+3)
                    st = en = False
                    count = 0
        if moves in [18,28,38,48,58,68,78,88]:
            step = 10
            count = 0
            st = False
            en = False
            start=end=18
            for x in [18,28,38,48,58,68,78,88]:
                if tempboard[x]==tkn1:
                    if count == 0:
                        start = x
                        st = True
                    count+=1
                else:
                    if count > 0:
                        end = x-step
                        en = True
                if st == en == True:
                    if tempboard[start - step] == tempboard[end + step] == "?":
                        SQUARE_WEIGHTS1[moves] += count + 4
                    elif tempboard[start-step]==tempboard[end+step]==tkn2:
                        SQUARE_WEIGHTS1[moves] += count+3
                    elif tempboard[start-step]==tempboard[end+step]==".":
                        SQUARE_WEIGHTS1[moves] += count+3
                    else:
                        SQUARE_WEIGHTS1[moves] -= (count+3)
                    st = en = False
                    count = 0
        if moves in [18,27,36,45,54,63,72,81]:
            step = 9
            count = 0
            st = False
            en = False
            start = 18
            end = 81
            for x in [18,27,36,45,54,63,72,81]:
                if tempboard[x]==tkn1:
                    if count == 0:
                        start = x
                        st = True
                    count+=1
                else:
                    if count > 0:
                        end = x-step
                        en = True
                if st == en == True:
                    if tempboard[start - step] == tempboard[end + step] == "?":
                        SQUARE_WEIGHTS1[moves] += count + 4
                    elif tempboard[start-step]==tempboard[end+step]==tkn2:
                        SQUARE_WEIGHTS1[moves] += count+3
                    elif tempboard[start-step]==tempboard[end+step]==".":
                        SQUARE_WEIGHTS1[moves] += count+3
                    else:
                        SQUARE_WEIGHTS1[moves] -= (count+3)
                    st = en = False
                    count = 0
        if moves in [11,22,33,44,55,66,77,88]:
            step = 11
            count = 0
            st = False
            en = False
            start = 11
            end = 88
            for x in [11,22,33,44,55,66,77,88]:
                if tempboard[x]==tkn1:
                    if count == 0:
                        start = x
                        st = True
                    count+=1
                else:
                    if count > 0:
                        end = x-step
                        en = True
                if st == en == True:
                    if tempboard[start - step] == tempboard[end + step] == "?":
                        SQUARE_WEIGHTS1[moves] += count + 4
                    elif tempboard[start-step]==tempboard[end+step]==tkn2:
                        SQUARE_WEIGHTS1[moves] += count+3
                    elif tempboard[start-step]==tempboard[end+step]==".":
                        SQUARE_WEIGHTS1[moves] += count+3
                    else:
                        SQUARE_WEIGHTS1[moves] -= (count+3)
                    st = en = False
                    count = 0

        # if tempboard[11] == tkn1 or tempboard[18] == tkn1 or tempboard[81] == tkn1 or tempboard[88] == tkn1:
        #     SQUARE_WEIGHTS1[moves]+=500

    #next2 = possible_moves(board,tkn2)
    '''if board[11]==tkn2 or board[18]==tkn2 or board[81]==tkn2 or board[88]==tkn2:
        SQUARE_WEIGHTS1[12]=SQUARE_WEIGHTS1[21]=SQUARE_WEIGHTS1[17]=SQUARE_WEIGHTS1[28]=SQUARE_WEIGHTS1[71]=SQUARE_WEIGHTS1[82]=SQUARE_WEIGHTS1[78]=SQUARE_WEIGHTS1[87]=-6
        SQUARE_WEIGHTS1[22] =SQUARE_WEIGHTS1[27]=SQUARE_WEIGHTS1[72]=SQUARE_WEIGHTS1[77]=-8'''
    if tkn1=="@":
        SQUARE_WEIGHTSblack=SQUARE_WEIGHTS1
        temp = sum(SQUARE_WEIGHTSblack[x] for x in b) - sum(SQUARE_WEIGHTSblack[x] for x in w)
    else:
        SQUARE_WEIGHTSwhite = SQUARE_WEIGHTS1
        temp = sum(SQUARE_WEIGHTSwhite[x] for x in b) - sum(SQUARE_WEIGHTSwhite[x] for x in w)
    # if (len(b) + len(w)) <= 5:
    #temp = (sum(SQUARE_WEIGHTS1[x] for x in b) - sum(SQUARE_WEIGHTS1[x] for x in w))*2
    SQUARE_WEIGHTS1=SQUARE_WEIGHTS2


    temp += (len(possible_moves(board, "@")) - len(possible_moves(board, "o")))*.5


    #SQUARE_WEIGHTS1 = [SQUARE_WEIGHTS1[x]+(SQUARE_WEIGHTS1[x]*(.05) * (300-old)) for x in range(len(SQUARE_WEIGHTS1))]
    #SQUARE_WEIGHTS = list(SQUARE_WEIGHTS)

    #Q2 this is the second place where the strategy changes. Towards the end, my code begins to play for the most tokens
    #to maximize the amount of tokens taken.
    m=.7
    if len(b) + len(w) >= 59:
        m = 40
    temp += (len(b)-len(w))*m



    return temp


def minimax(board,tkn,depth):
    #count_board(board)
    tkn1 = tkn
    tkn2 = othertkn(tkn)
    if (depth==0) or (len(possible_moves(board,tkn1))==len(possible_moves(board,tkn2))==0):
        return {board: evaluate(board,0)} #0 is a temp moves
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


#Q1 This is just regular alpha-beta pruning. The code traverses through the tree of possible moves like minimax, but it
# "prunes" certain branches when it establishes that there cannot be a better move. The method determines which values
# are pruned by passing alpha and beta values for maximizing nodes and minimizing nodes respectively. Alpha is the best
# move for maximizing and beta the best node if minimizing. If alpha is greater than beta, then the code stops.
def alphabeta(board,tkn,depth,alpha,beta,old):
    #count_board(board)
    global oldr
    tkn1 = tkn
    tkn2 = othertkn(tkn)
    next1 = possible_moves(board,tkn1)
    next2 = possible_moves(board,tkn2)
    if (depth==0) or (len(next1)==len(next2)==0):
        oldr = evaluate(board,old,tkn1,tkn2)
        return {board: oldr}
    if (len(next1) == 0) & (len(next2) != 0):
        tkn1 = tkn2
        tkn2 = tkn
        next1 = next2
        #next2 = possible_moves(board, tkn2)
    result = dict()
    for moves in next1:
        next_board = make_move(board,tkn1,moves)
        #display_board(next_board)
        if alpha>=beta:
            break
        if tkn1 == "o":
            res = max(alphabeta(next_board,tkn2,depth-1,alpha,beta,oldr).values())
            if res>=alpha:
                alpha = res
        else:
            res = min(alphabeta(next_board,tkn2,depth-1,alpha,beta,oldr).values())
            if res<=beta:
                beta = res
        result[moves] = res
    return result


def negascout(board,tkn,depth,alpha,beta,old):
    #count_board(board)
    global oldr
    tkn1 = tkn
    tkn2 = othertkn(tkn)
    next1 = possible_moves(board,tkn1)
    next2 = possible_moves(board,tkn2)
    if (depth==0) or (len(next1)==len(next2)==0):
        oldr = evaluate(board,old,tkn1,tkn2)
        return oldr
    if (len(next1) == 0) & (len(next2) != 0):
        tkn1 = tkn2
        tkn2 = tkn
        next1 = next2
        #next2 = possible_moves(board, tkn2)
    #result = dict()
    for x in range(len(next1)):
        if x == 0:
            next_board = make_move(board, tkn1, next1[x])
            # display_board(next_board)
            score = -(negascout(next_board,tkn2,depth-1,-beta,-alpha,1))
        else:
            next_board = make_move(board, tkn1, next1[x])
            score = -(negascout(next_board,tkn2,depth-1,-beta,-alpha,1))
            if alpha<score<beta:
                score = -(negascout(next_board,tkn2,depth-1,-beta,-alpha,1))
        alpha = max(alpha,score)
        if alpha >= beta:
            break
        #print(score)
        #result[next1[x]] = score
    return alpha

def computer_turn(board, tkn, depth):
    next = minimax("".join(board), tkn, depth)
    if tkn == "o":
        move = min(next.items(), key=operator.itemgetter(1))[0]
    else:
        move = max(next.items(), key=operator.itemgetter(1))[0]
    return move


def computer_turn2(board, tkn,depth):
    next = alphabeta(board,tkn,depth,-float('inf'),float('inf'),1)
    if tkn == "o":
        move = min(next.items(), key=operator.itemgetter(1))[0]
    else:
        move = max(next.items(), key=operator.itemgetter(1))[0]
    #display_board(board)
    return move


def computer_turn3(board, tkn,depth):
    #board="".join(board)
    best_move = -1000000
    maxpoint = -100000
    for x in possible_moves(board,tkn):
        point = negascout(board,tkn,depth,-float('inf'),float('inf'),1)
        if point>maxpoint:
            maxpoint=point
            best_move=x
    #display_board(board)
    return best_move
# import multiprocessing
# from multiprocessing import Pool
# def compeuter_turnP(board, tkn, depth):
#     pool = Pool()
#     result1 = pool.apply_async(alphabeta, [board,tkn,depth,-2000,2000,1])
#
# def alphabetaP(board,tkn,depth,alpha,beta,old):
#     #count_board(board)
#     pool = Pool()
#
#     global oldr
#     tkn1 = tkn
#     tkn2 = othertkn(tkn)
#     next1 = possible_moves(board,tkn1)
#     next2 = possible_moves(board,tkn2)
#     if (depth==0) or (len(next1)==len(next2)==0):
#         olds = evaluate(board,old,tkn1,tkn2)
#         oldr = olds
#         return {board: olds}
#     if (len(next1) == 0) & (len(next2) != 0):
#         tkn1 = tkn2
#         tkn2 = tkn
#         next1 = next2
#         #next2 = possible_moves(board, tkn2)
#     result = dict()
#     for x in range(len(next1)):
#         if x == 0:
#             next_board = make_move(board,tkn1,next1[x])
#             #display_board(next_board)
#             if alpha>=beta:
#                 break
#             if tkn1 == "o":
#                 res = max(alphabetaP(next_board,tkn2,depth-1,alpha,beta,oldr).values())
#                 if res>=alpha:
#                     alpha = res
#             else:
#                 res = min(alphabetaP(next_board,tkn2,depth-1,alpha,beta,oldr).values())
#                 if res<=beta:
#                     beta = res
#             result[next1[x]] = res
#         else:
#             for y in range (1,len(next1)):
#                 result = pool.apply_async(alphabeta, [board,tkn,depth,-2000,2000,1]).get(timeout=10)
#     return result
#

def display_board(board):
    for x in range(10):
        if x == 0:
            numers = " "+"  ".join(str(x) for x in range(x*10,x*10+10))
        else:
            numers = " ".join(str(x) for x in range(x*10,x*10+10))
        #board = "".join(board)
        temp = board[x*10:x*10+10].replace("."," ")
        print("  ".join(temp)+"    " + "  ".join(board[x*10:x*10+10]) + "   " + numers)


def random_mini_play(board,depth):
    path = []
    count = 0
    state = board[:]
    display_board(state)
    b,w = count_board(state)
    print("black score: "+ str(b)+ " white score: "+str(w))
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
            print("black score: " + str(b) + " white score: " + str(w))
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
            state = make_move(state,tkn2,computer_turn2(state,tkn2,depth))
            count+=1
            print("move: " + str(count) + " white move")
            print(next2)
            display_board(state)
            b, w = count_board(state)
            print("black score: " + str(b) + " white score: " + str(w))
        else:
            if len(next1)==0:
                break
            path.append(-1)
            print("white pass")
        print()
        print()
        #b, w = count_board(state)
    display_board(state)
    print("black: " + str(100 * b / (b + w)) + "% white: " + str(
        100 * w / (b + w)) + "%")
    print("total path: "+ str(path[:len(path)-1]))
    return (100 * w / (b + w))

class Strategy():
    def best_strategy(self, board, player, best_move, running):
        global bestMOVE
        #count_board(board)
        if running.value:
            for x in range(1,100):
                best_move.value = computer_turn2(board,player,x)
                for x in possible_moves(board,player):
                    if x in [11,18,81,88]:
                        best_move.value = x
            #best_move.value = random.choice(possible_moves(board, player))
class Strategy2():
    def best_strategy(self, board, player):
        global bestMOVE
        #count_board(board)
        for x in range(1,100):
            bestMOVE = computer_turn2(board,player,x)
            for x in possible_moves(board,player):
                if x in [11,18,81,88]:
                    bestMOVE = x
            print(bestMOVE)
#alphabeta(board,"@",6,-2000,2000,1)
#random_mini_play(board,4)
'''if __name__ == '__main__':
    #multiprocessing.freeze_support()
    # start = time.perf_counter()
    # print(negascout(board,"@",10,-2000,2000,1))
    # end = time.perf_counter()
    # print(end-start)
    start = time.perf_counter()
    print(alphabeta(board, "@", 10, -2000, 2000, 1))
    end = time.perf_counter()
    print(end - start)'''
# y=0
# for x in range(10):
#     y+=random_mini_play(board,6)
# print(y/10)
import sys
s = sys.argv
x = Strategy2()
x.best_strategy(s[1],s[2])