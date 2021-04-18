import math
import time

N=9
subblock_height = 3
subblock_width = 3
symbol_set = {x for x in range(N)}
edges = {}

def createboard(puzzle):
    global N
    global subblock_width
    global subblock_height
    global symbol_set
    global edges

    N = int(math.sqrt(len(puzzle)))
    subblock_height = int(math.sqrt(N))
    subblock_width = int(N/subblock_height)
    stringslist = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbol_set = stringslist[0:N]

    for chars in range(int(N*N)):
        rowindex = set()
        row = int(chars / N)
        for r in range(N):
            rowindex.add(row * N + r)
        colindex = {ind for ind in range(int(chars%N),int(N*N-chars%N),N)}
        subcol = chars%N-chars%N%subblock_width
        subrow = row-row%subblock_height
        firstindex = subcol+N*subrow
        subindex = set()
        for ind in range(firstindex, firstindex+subblock_width):
            for inde in range(subblock_height):
                subindex.add(ind+N*inde)
        #if chars == 49:
            #print(rowindex, colindex, subindex)
        edges[chars]=rowindex|colindex|subindex

def printboard(puzzle):
    global N
    for x in range(N):
        row = []
        for y in range(x*N,(x+1)*N):
            if (y % subblock_width == 0) & (y!= x*N):
                row.append("|")
            if puzzle[y]=='.':
                row.append(" ")
            else:
                row.append(puzzle[y])
            row.append(" ")
        divide = ""
        for size in range(N*2+subblock_width):
            divide+="-"
        if (x % subblock_height == 0) & (x>0):
            print(divide)
        print("".join(row))

    print()
    print()


def csp(state):
    global callcount
    callcount+=1
    if goal_test(state): return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        # create new_state by assigning val to var
        '''new_state = list(state)
        new_state[var] = val
        result = csp("".join(new_state))'''
        new_state = state[0:var]+val+state[var+1:len(state)]
        result = csp(new_state)
        if result is not None:
            return result
    return None
def goal_test(state):
    for x in state:
        if x=='.':
            return False
    return True
def get_next_unassigned_var(state):
    for x in range(N*N):
        if state[x]=='.':
            return x
    return None
def get_sorted_values(state,var):
    valid = []
    invalid = set()
    for x in edges[var]:
        invalid.add(state[x])
    for y in symbol_set:
        if y not in invalid:
            valid.append(y)
    #print(valid)
    return valid


    



filename = "sudoku_puzzles_1.txt"
file = open(filename)
lists = file.readlines()
totaltime = 0
callcount = 0
for x in range(len(lists)):
    lists[x] = lists[x].rstrip()
    print(x)
    createboard(lists[x])
    start = time.perf_counter()
    solution = csp(lists[x])
    end = time.perf_counter()
    totaltime += (end-start)
    print("runtime: "+str(end-start)+ " totaltime: "+str(totaltime))
    printboard(solution)
    print("total calls: "+str(callcount))

