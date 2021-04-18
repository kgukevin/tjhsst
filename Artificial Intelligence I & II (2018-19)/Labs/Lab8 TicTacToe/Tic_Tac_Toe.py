import collections
import time
import sys
import operator

sys.setrecursionlimit(50000)
board = "....O...."

edges = dict()
rowcons = []
colcons = []
for x in range(0, 3):
    rowindex = set()
    row = int(x / 3)
    for r in range(3):
        rowindex.add(row * 3 + r)
    rowcons.append(rowindex)
    colindex = {ind for ind in range(int(x % 3), int((3 * 3) - x % 3), 3)}
    if x % 3 == 2:
        colindex.add(8)
    colcons.append(colindex)

for x in range(0, 9):
    edges[x] = rowcons[int(x / 3)] | colcons[int(x % 3)]
    if x == 0 or x == 8:
        edges[x].add(0)
        edges[x].add(4)
        edges[x].add(8)
    if x == 0 or x == 8:
        edges[x].add(0)
        edges[x].add(4)
        edges[x].add(8)


def assess_board(board, letter):
    result = ((board[0] == board[1] == board[2] == letter) or
              (board[3] == board[4] == board[5] == letter) or
              (board[6] == board[7] == board[8] == letter) or
              (board[0] == board[3] == board[6] == letter) or
              (board[1] == board[4] == board[7] == letter) or
              (board[2] == board[5] == board[8] == letter) or
              (board[0] == board[4] == board[8] == letter) or
              (board[2] == board[4] == board[6] == letter))
    if result == True:
        return True
    elif (board.count(".") == 0):
        return "draw"
    return False


def goal_test(board):
    x = assess_board(board, "X")
    o = assess_board(board, "O")
    if x == o == "draw":
        return True
    if ((x == True) or (o == True)):
        return True
    return False


def get_children(board):
    children = []
    state = list(board[-1])
    moves = board[0]
    open = [x for x in range(9) if board[-1][x] == "."]
    X = board[-1].count("X")
    O = board[-1].count("O")
    if X > O:
        for x in open:
            temp = state.copy()
            temp[x] = "O"
            children.append((moves + 1, "".join(temp)))
    else:
        for x in open:
            temp = state.copy()
            temp[x] = "X"
            children.append((moves + 1, "".join(temp)))
    return children


def BFS(startstate):
    next = collections.deque([(0, startstate)])  # BFS algorithm from class of a list of states
    visited = {startstate}
    start = time.process_time()
    while len(next) != 0:
        v = next.popleft()
        if goal_test(v[-1]):
            end = time.process_time()
            print("path length: " + str(v[0]) + ". seconds to run: %s" % (end - start) + ".")
            return True, visited, v[0], end - start
        for child in get_children(v):
            if not child[-1] in visited:
                visited.add(child[-1])  # add just new state, not whole child
                next.append(child)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start


def BFS3(startstate):
    next = collections.deque([(0, startstate)])  # BFS algorithm from class of a list of states
    visited = {startstate}
    start = time.process_time()
    distinct = set()
    total = []
    while len(next) != 0:
        v = next.popleft()
        if goal_test(v[-1]):
            end = time.process_time()
            print("path length: " + str(v[0]) + ". seconds to run: %s" % (end - start) + ".")
            # return True, visited, v[0], end - start
            distinct.add(v[-1])
            total.append(v[-1])
        else:
            for child in get_children(v):
                if not child[-1] in visited:
                    visited.add(child[-1])  # add just new state, not whole child
                    next.append(child)
    end = time.process_time()
    # print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    print(str(len(total)) + " " + str(len(distinct)))
    return False, visited, 0, end - start


def evaluate(state):
    x = assess_board(state, "X")
    o = assess_board(state, "O")
    if x == True:
        return 5
    elif x == o == "draw":
        return 0
    elif o == True:
        return -5


def mini_children(state):
    board = state[:]
    children = []
    state = list(board)
    open = [x for x in range(9) if board[x] == "."]
    X = board.count("X")
    O = board.count("O")
    if X > O:
        for x in open:
            temp = state.copy()
            temp[x] = "O"
            children.append("".join(temp))
    else:
        for x in open:
            temp = state.copy()
            temp[x] = "X"
            children.append("".join(temp))
    return children


def minimax(board):
    if goal_test(board):
        return {board: evaluate(board)}
    result = dict()
    for moves in mini_children(board):
        next_board = moves
        X = board.count("X")
        O = board.count("O")
        if X > O:
            res = max(minimax(next_board).values())
        else:
            res = min(minimax(next_board).values())
        result[moves] = res
    return result


def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()
    print()


def display_moves(nexts, tkn):
    tkn = tkn.upper()
    for moves in nexts:
        res = ""
        if nexts[moves] == 0:
            res = "T"
        if tkn == "X":
            if nexts[moves] == 5:
                res = "W"
            if nexts[moves] == -5:
                res = "L"
        if tkn == "O":
            if nexts[moves] == 5:
                res = "L"
            if nexts[moves] == -5:
                res = "W"
        print(moves + " results in " + res)


def computer_turn(board, tkn):
    tkn = tkn.upper()
    next = minimax("".join(board))
    display_moves(next, tkn)
    if tkn == "O":
        board = list(min(next.items(), key=operator.itemgetter(1))[0])
    else:
        board = list(max(next.items(), key=operator.itemgetter(1))[0])
    display_board(board)
    return board


def player_turn(board, tkn):
    move = input("What move? ")
    board[int(move)] = tkn
    display_board(board)
    return board


def play(board):
    if board == ".........":
        display_board(board)
        state = list(board)
        tkn = input("X or O? ")
        if tkn == "o" or tkn == "O":
            while not goal_test(state):
                state = player_turn(state, "X")  # token opposite of computer piece
                if goal_test(state):
                    sol = evaluate(state)
                    if sol == 0:
                        print("TIE")
                        return
                    elif sol == 5:
                        print("YOU LOSE")
                        return
                    else:
                        print("YOU WIN")
                        return
                state = computer_turn(state, tkn)  # token same as if statement
                if goal_test(state):
                    sol = evaluate(state)
                    if sol == 0:
                        print("TIE")
                        return
                    elif sol == -5:
                        print("YOU LOSE")
                        return
                    else:
                        print("YOU WIN")
                        return
        if tkn == "x" or tkn == "X":
            while not goal_test(state):
                state = computer_turn(state, tkn)
                if goal_test(state):
                    sol = evaluate(state)
                    if sol == 0:
                        print("TIE")
                        return
                    elif sol == -5:
                        print("YOU WIN")
                        return
                    else:
                        print("YOU LOSE")
                        return
                state = player_turn(state, "O")
                if goal_test(state):
                    sol = evaluate(state)
                    if sol == 0:
                        print("TIE")
                        return
                    elif sol == 5:
                        print("YOU WIN")
                        return
                    else:
                        print("YOU LOSE")
                        return
    else:
        display_board(board)
        state = list(board)
        X = board.count("X")
        O = board.count("O")
        if X > O:
            tkn = "O"
            ptkn = "X"
        else:
            ptkn = "O"
            tkn = "X"
        while not goal_test(state):
            state = computer_turn(state, tkn)
            if goal_test(state):
                sol = evaluate(state)
                if tkn == "O":
                    if sol == 0:
                        print("TIE")
                        return
                    elif sol == 5:
                        print("YOU WIN")
                        return
                    else:
                        print("YOU LOSE")
                        return
                else:
                    if sol == 0:
                        print("TIE")
                        return
                    elif sol == -5:
                        print("YOU WIN")
                        return
                    else:
                        print("YOU LOSE")
                        return
            state = player_turn(state, ptkn)
            if goal_test(state):
                sol = evaluate(state)
                if tkn == "O":
                    if sol == 0:
                        print("TIE")
                        return
                    elif sol == -5:
                        print("YOU WIN")
                        return
                    else:
                        print("YOU LOSE")
                        return
                else:
                    if sol == 0:
                        print("TIE")
                        return
                    elif sol == 5:
                        print("YOU WIN")
                        return
                    else:
                        print("YOU LOSE")
                        return

board = sys.argv[1]
play(board)
