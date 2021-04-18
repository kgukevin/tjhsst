global N
global height
global width
global indices
import time
import random
import sys
backtrack = 0
symbols = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
global symbol_set
def convert(state):
    d = dict()
    ind = []
    for index,value in enumerate(state):
        if value!='.':
            d[index]=value
            ind.append(index)
        else:
            d[index]=symbol_set
    '''
    for i in ind:
        for x in indices[i]:
            if state[i] in d[x]:
                d[x]=d[x].replace(state[i],'')
    '''
    for i in ind:
        cprop(d,i)
    #print(d)
    return d

def read(state):
    global N
    global width
    global height
    global indices
    global symbol_set
    N = int(len(state)**0.5)
    symbol_set = symbols[0:N]
    height = N**0.5
    if height.is_integer():
        height = int(height)
        width = height
    else:
        height = int(height)
        width = height +1
    sets = []
    for i in range(N):
        rowset = set()
        columnset = set()
        for x in range(N):
            rowset.add(x+i*N)
            columnset.add(i+x*N)
        sets.append(rowset)
        sets.append(columnset)
    for c in range(int(N/width)):
        for r in range(int(N/height)):
            blockset = set()
            initialr = r*height #row 0,1,2,3...
            initialc = c*width
            for x in range(width):
                for y in range(height):
                    blockset.add((initialr+y)*N+initialc+x)
            sets.append(blockset)
            #print(blockset)
    store = dict()
    #print(sets)
    for i in range(N*N):
        for s in sets:
            if i in s:
                if i in store.keys():
                    store[i] = s.union(store[i])
                else:
                    store[i]=s.copy()
                store[i].remove(i)
    indices = store


def goal_test(state):
    for i in state:
        if len(state[i])!=1:
            return False
    return True

def get_next_unassigned_variable(state):
    maxi = 0
    maxlen = N
    for i in state:
        if len(state[i])<=maxlen and len(state[i])!=1:
            maxlen = len(state[i])
            maxi = i
    return maxi



def get_sorted_values(state,var):
    return state[var]

def cprop(state,var): #THIS IS THE PROBLEM
    go = [var]
    store = True
    while len(go)!=0 and store:
        index = go.pop()
        val = state[index]
        for i in indices[index]:
            if val in state[i]:
                state[i]= state[i].replace(val,'')
                if len(state[i])==0:
                    #Going down wrong path? returns none
                    return False
                if len(state[i])==1:
                    go.append(i)
        store = not goal_test(state)
    #checkSets(state) #ADDED LINE
    return True



def csp(state): #LIMIT BACKTRACKING?
    global backtrack
    backtrack+=1
    if goal_test(state):
        return state
    var = get_next_unassigned_variable(state)
    for val in get_sorted_values(state,var):
        copy = state.copy()
        copy[var] = val
        if cprop(copy,var):
            c= csp(copy)
            if c !=None:
                return c
    #return None

def numSymbols(state):
    d = dict()
    for i in symbol_set:
        d[i]=0
    for i in state:
        d[state[i]] = d[state[i]]+1
    return d


def display(state):
    s = ''
    for i in range(N*N):
        s+=state[i]
    print(s)
    #print(state)

def checkSets(state):
    for sets in indices:
        sets = indices[sets]
        unique = symbol_set
        for index in sets:
            for i in state[index]:
                if i in unique:
                    unique.replace(i,'')
        for i in unique:
            for index in sets:
                if i in state[index]:
                    state[index]=i

def main():
    #sys.setrecursionlimit(50000)
    name = 'sudoku_puzzles_1.txt'
    #name = sys.argv[1]
    file = open(name)
    n = 0
    t=0.0
    lines = file.readlines()
    for i in range(95,127):
        state = lines[i].rstrip()
        read(state)

        state = convert(state)

        start = time.perf_counter()
        #cprop(state)

        print('puzzle: '+str(n))
        n += 1

        solution = csp(state)
        end = time.perf_counter()

        display(solution)

        print(numSymbols(solution))

        print(end-start)
        t+=end-start
        print()

    print(t)
    print(backtrack)

main()