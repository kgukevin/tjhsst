import math
import time
import sys

sys.setrecursionlimit(50000)
N = 9
subblock_height = 3
subblock_width = 3
symbol_set = {x for x in range(N)}
edges = {}
available = {}
subs = []


def createboard(puzzle):
    global N
    global subblock_width
    global subblock_height
    global symbol_set
    global edges

    N = int(math.sqrt(len(puzzle)))
    subblock_height = int(math.sqrt(N))
    subblock_width = int(N / subblock_height)
    stringslist = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbol_set = [stringslist[x] for x in range(N)]

    for chars in range(int(N * N)):
        rowindex = set()
        row = int(chars / N)
        for r in range(N):
            rowindex.add(row * N + r)
        colindex = {ind for ind in range(int(chars % N), int(N * N), N)}
        #if chars%N == (N-1):
            #colindex.add(N*N-1)
        subcol = chars % N - chars % N % subblock_width
        subrow = row - row % subblock_height
        firstindex = subcol + N * subrow
        subindex = set()
        for ind in range(firstindex, firstindex + subblock_width):
            for inde in range(subblock_height):
                subindex.add(ind + N * inde)
        # if chars == 49:
        # print(rowindex, colindex, subindex)
        edges[chars] = rowindex | colindex | subindex
        if rowindex not in subs:
            subs.append(rowindex)
        if colindex not in subs:
            subs.append(colindex)
        if subindex not in subs:
            subs.append(subindex)
def initiate_puzzle(puzzle):
    global N
    global available
    for chars in range(int(N*N)):
        if puzzle[chars] == ".":
            available[chars] = "".join(get_initial_values(puzzle, chars))
            #available[chars]="".join(symbol_set)
        else:
            available[chars] = str(puzzle[chars])
    inds = 0

    #available = propagate(available,inds)
    changes = True
    #available = propagatep3(available,changes)
    available = propagate2(available)

    #return available
    #return propagatep3(available)
    for x in range(20):
        available = propagatep3(available)
    #return propagatep3(propagate2(available))
    return available

def printboard(puzzle):
    global N
    for x in range(N):
        row = []
        for y in range(x * N, (x + 1) * N):
            if (y % subblock_width == 0) & (y != x * N):
                row.append("|")
            if puzzle[y] == '.':
                row.append(" ")
            else:
                row.append(puzzle[y])
            row.append(" ")
        divide = ""
        for size in range(N * 2 + subblock_width):
            divide += "-"
        if (x % subblock_height == 0) & (x > 0):
            print(divide)
        print("".join(row))

    print()
    print()
def output(puzzle):
    global N
    str = ""
    for x in puzzle.keys():
        str+=puzzle[x]
    print(N)
    print(str)

def goal_test(state):
    for x in state:
        if len(state[x]) != 1:
            return False
    return True


def get_next_unassigned_var(state):
    shortest = N
    next = 0
    for x in range(N * N):
        if (len(state[x]) > 1) & (len(state[x]) < shortest):
            shortest = len(state[x])
            next = x
    return next


def get_sorted_values(state, var):
    return state[var]


def get_initial_values(state, var):
    valid = []
    invalid = set()
    for x in edges[var]:
        invalid.add(state[x])
    for y in symbol_set:
        if y not in invalid:
            valid.append(y)
    # print(valid)
    return valid


def propagate(state, var):
    global edges
    original = state.copy()
    solved = [var]
    while len(solved) != 0:
        next = solved.pop()
        val = original[next]
        for x in edges[next]:
            if x != next:
                if val in original[x]:
                    original[x] = original[x].replace(val, "")
                    if len(original[x]) == 0:
                        return False
                    if len(original[x]) == 1:
                        solved.append(x)
    return original
def propagate2(state):
    global edges
    original = state.copy()
    solved = []
    for x in available:
        if len(original[x]) == 1:
            solved.append(x)
    while len(solved) != 0:
        next = solved.pop()
        val = original[next]
        for x in edges[next]:
            if x != next:
                if val in original[x]:
                    original[x] = original[x].replace(val, "")
                    if len(original[x]) == 0:
                        return False
                    if len(original[x]) == 1:
                        solved.append(x)
    return original
    '''store = True
    while len(solution)!=0 and store:
        index = solution.pop()
        val = original[index]
        for i in edges[index]:
            if val in original[i]:
                original[i]= original[i].replace(val,'')
                if len(original[i])==0:
                    #Going down wrong path? returns none
                    return False
                if len(original[i])==1:
                    solution.append(i)
        store = not goal_test(original)
    #checkSets(state) #ADDED LINE
    return original'''


def csp(state):
    global callcount
    callcount += 1
    global totalcall
    totalcall +=1
    if goal_test(state): return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = state.copy()
        new_state[var] = val
        next_state = propagate(new_state, var)
        if next_state is not False:
            if goal_test(next_state): return next_state
            result = csp(next_state)
            if result is not None:
                return result

    # return None


def propagatep3(state):
    global subs
    #subs = [{0,1,2,3,4,5,6,7,8}]
    #original = {0:'234',1:'1345234',2:'2356',3:'4',4:'789',5:'8',6:'45',7:'67',8:'34'}
    original = state.copy()
    #temp = state.copy()
    #printboard(original)
    count = 0
    index = None
    for sets in subs:
        for sym in symbol_set:
            for x in sets:
                if (sym in original[x]):
                    count += 1
                    if count == 1:
                        index = x
                    else:
                        index = None
            if index != None:
                original[index] = sym
            index = None
            count = 0
    #printboard(original)
    #original = state.copy()
    original = propagate2(original)
    '''if original == False:
        return temp'''
    return original

    '''original = state.copy()
    count = 0
    index = 0
    for sets in subs:
        for sym in symbol_set:
            for x in sets:
                if sym in original[x]:
                    count += 1
                    index = x
            if (count==1):
                for temp in original:
                    if sym in original[temp]:
                        index = temp

                original[index] = sym
                count = 0
    ind = 0
    for x in original:
        if len(original[x]) == 1:
            ind = x
    original = propagate(original, ind)
    original = propagate2(original)
    return original'''

def propagatep4(state, changes):
    original = state.copy()
    count = 0
    index = 0
    for sets in subs:
        for sym in symbol_set:
            for x in sets:
                if sym in state[x]:
                    index = x
                    count += 1
            if (count == 1):
                '''for temp in original:
                    if sym in original[temp]:
                        index = temp'''
                original[index] = sym
                count = 0
                changes = True
    ind = 0
    for x in original:
        if len(original[x]) == 1:
            ind = x
    original = propagate(original, ind)
    return original,changes

    '''original = state.copy()
    temp = state.copy()
    count = 0
    change = None
    #print(subs)
    for sets in subs:
        for sym in symbol_set:
            for index in sets:
                if sym in state[index]:
                    count+=1
                    change=index
                    if count>1:
                        change=None
            if change is not None:
                original[change]=sym
            count = 0
    ind = 0
    for x in original.keys():
        if len(original[x])==1:
            ind = x
    original = propagate(original,ind)
    return original'''
    '''original = state.copy()
    for sets in subs:
        temp = []
        for index in sets:
            if len(state[index]) != 1:
                temp.append(list(state[index]))
        for val in symbol_set:
            if temp.count(val)==1:
                for index in sets:
                    if val in state[index]:
                        original[index]=val
                        original = propagate(original,index)
                        
        temp.clear()
    return original'''
    '''original = state.copy()
    ind = 0
    for sets in subs:
        temp = dict()
        for sym in symbol_set:
            for index in sets:
                if sym in state[index]:
                    if sym in temp.keys():
                        temp[sym].append(index)
                    else:
                        temp[sym]=[index]
        for x in temp.keys():
            if (len(temp[x])==1):
                ind = temp[x][0]
                original[temp[x][0]]=x
                changes = False
    original = propagate(original,ind)
    print(original)
    return original'''

    '''original = state.copy()
    for sets in subs:
        temp = {}
        for index in sets:
            for val in symbol_set:
                if val in state[index]:
                    if val in temp.keys():
                        temp[val]=temp[val]+1
                    else:
                        temp[val]=0
            
                    
                    
                if temp.count(val) == 1:
                    for index in sets:
                        if val in state[index]:
                            if len(state[index]) > 1:
                                original[index] = val
                                temp = propagate(original, index)
                                if temp is not False:
                                    original = temp
                                else:
                                    return False
        temp.clear()
    return original'''
  # THIS IS TE PROBLEM FIX
    '''original = state.copy()
    for sets in subs:
        temp = dict()
        for index in sets:
            v = state[index]
            if len(v) != 1:
                for i in v:
                    if i not in temp:
                        temp[i] = 1
                    else:
                        temp[i] = temp[i] + 1
        unique = ''
        for i in temp:
            if temp[i] == 1:
                unique = unique + i
        for i in unique:
            for index in sets:
                if i in original[index]:
                    original[index] = i
                    x = propagate2(original, index)
                    if x is not False:
                        original = x
                    else:
                        return False
    return original'''
    '''original = state.copy()
    count = 0
    for sets in subs:
        for val in symbol_set:
            posvals = dict()
            for index in sets:
                posvals[index]=state[index]
            for x in posvals.keys():
                if val in posvals[x]:
                    count+=1
                if count>1:
                    count=0
                    break
            if count == 1:
                for x in posvals.keys():
                    if val in posvals[x]:
                        original[x] = val
                        break
    original = propagate2(original)
    return original'''
    '''original = state.copy()
    for sets in subs:
        posvals = dict()
        for index in sets:
            posvals[index]=state[index]
        for sym in symbol_set:
            for index in posvals.keys():
                if sym in posvals[index]:
                    count+=1
                '''


def csp2(state):
    global callcount
    callcount += 1
    global totalcall
    totalcall+=1
    if goal_test(state): return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = state.copy()
        new_state[var] = val
        next_state = propagate2(new_state)
        if next_state is not False:
            next2_state = propagatep3(next_state)
            if next2_state is not False:
                result = csp2(next2_state)
                if result is not None:
                    return result

def csp3(state):
    global callcount
    callcount += 1
    if goal_test(state): return state
    var = get_next_unassigned_var(state)
    for val in list(get_sorted_values(state, var)):
        new_state = state.copy()
        new_state[var] = val
        next_state = propagate(new_state, var)
        if next_state is not False:
            changes = False
            next2_state,changes = propagatep4(next_state,changes)
            while changes:
                next2_state,changes = propagatep4(next2_state,changes)
            if next2_state is not False:
                result = csp3(next2_state)
                if result is not None:
                    return result
    return None


#filename = sys.argv[1]
filename = "sudoku_puzzles_3_harder.txt"
file = open(filename)
lists = file.readlines()
totaltime = 0
callcount = 0
totalcall = 0
for x in range(0,len(lists)):
    lists[x] = lists[x].rstrip()
    print(x)
    createboard(lists[x])
    # print(get_next_unassigned_var(available))
    start = time.perf_counter()
    solution = csp2(initiate_puzzle(lists[x]))
    end = time.perf_counter()
    totaltime += (end - start)

    printboard(solution)
    print("runtime: " + str(end - start) + " totaltime: " + str(totaltime))
    print("calls: " + str(callcount) + " totalcalls: "+ str(totalcall))
    callcount = 0
    N = 9
    subblock_height = 3
    subblock_width = 3
    symbol_set = {x for x in range(N)}
    edges = {}
    available = {}
    subs = []



"""turn in at tinyurl.com/2018EckelSudoku"""