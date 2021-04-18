import collections
import time
import random
import cProfile
import math
import sys
from heapq import heappop,heappush

#global variables
goal = "012345678"
size = 3

def rand_puzzle():  #finds random puzzle by generating random letters form 0-8 checking for repeats (only puzzle size 3)
    puzzle = ""
    while len(puzzle)<9:
        x = random.randint(0,8)
        if not str(x) in puzzle:
            puzzle+=str(x)
    return puzzle
def rand_solvable_puzzle():   #finds random solvable puzzle by calling rand_puzzle() and checking for parity (only puzzle size 3)
    puzzle = rand_puzzle()
    while parity_check(puzzle)==1:
        puzzle=rand_puzzle()
    return puzzle;
def goal_test(state):   #returns goal test if state is equal to goal
    if state[-1] == goal:
        return True
    return False
def print_puzzle(state):    #prints puzzle in specific format
    state = state.replace("0"," ")
    print("+-----+")
    print("|" + state[0]+" "+state[1]+" "+state[2] + "|")
    print("|" + state[3]+" "+state[4]+" "+state[5] + "|")
    print("|" + state[6]+" "+state[7]+" "+state[8] + "|")
    print("+-----+")
    print()
def get_children(states):   #returns list of children by checking both 1 and 3 indexes away from "0"
    empty = states[-1].index("0")
    state = states[-1]
    previous = states   #in order to add all previous states to the next child
    children = []
    if ((empty%size!=size-1)):
        child1 = swap_tiles(state,state[empty],state[empty+1])
        temp = previous + [child1]  #child includes all previous states as a list
        children.append(temp)
    if ((empty%size!=0)):
        child2 = swap_tiles(state,state[empty],state[empty-1])
        temp = previous + [child2]
        children.append(temp)
    if (empty < len(state)-(size)):
        child3 = swap_tiles(state,state[empty],state[empty+size])
        temp = previous + [child3]
        children.append(temp)
    if (empty > (size-1)):
        child4 = swap_tiles(state,state[empty],state[empty-size])
        temp = previous + [child4]
        children.append(temp)
    return children     #returns a list of states, which are also lists
def swap_tiles(state,char1,char2):  #used to swap the values from get_children() to make the actual new children
    state = state.replace(char2,"\"")
    state = state.replace(char1,char2)
    state = state.replace("\"",char1)
    return state
def run_100_tests(): #runs 100 tests and records data from the return of BFS.
    start = time.process_time()
    number_solved = 0
    path_lengths = 0
    longest_path = 0
    for x in range (0,101):
        print(x)
        solved, visited, path_length, times = BFS_edited(rand_puzzle(),"012345678",3)  #to make method easier, BFS returns tuple of boolean, set of visited, length of child, times of processing
        if solved:
            number_solved+=1
        path_lengths+=path_length
        if path_length>longest_path:
            longest_path = path_length
    end = time.process_time()
    print("total seconds to run: %s" %(end-start))
    print("Solvable Ratio: "+str(number_solved/100))
    print("Average Path Length: "+str(path_lengths/number_solved))
    print("Longest Path Length: "+str(longest_path))
def BFS(startstate, goals, sizes):
    global goal #edit global variables
    goal = goals
    global size
    size = sizes
    #print(startstate)
    next = collections.deque([[startstate]])    #BFS algorithm from class of a list of states
    visited = {startstate}
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return False, visited, 0, end - start
    while len(next) != 0:
        v = next.popleft()
        visited.add(v[-1])
        if(goal_test(v)):
            end = time.process_time()
            print("path length: " + str(len(v)-1) + ". seconds to run: %s" % (end - start) + ".")
            return True, visited, len(v)-1, end - start
        for child in get_children(v):
            if not child[-1] in visited:
                next.append(child)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start
def DFS(startstate, goals, sizes):    #depth first search
    global goal  # edit global variables
    goal = goals
    global size
    size = sizes
    # print(startstate)
    next = [('', startstate)]  # BFS algorithm from class of a list of states
    visited = {startstate}
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return False, visited, 0, end - start
    while len(next) != 0:
        v = next.pop()
        if (goal_test(v)):
            end = time.process_time()
            print("path length: " + str(len(v[0])) + ". seconds to run: %s" % (end - start) + ".")
            return True, visited, len(v) - 1, end - start
        for child in get_children2(v):
            if not child[-1] in visited:
                visited.add(child[-1])  # add just new state, not whole child
                next.append(child)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start
def BFS_part2(startstate): #if run on "012345678" will print 181440 as answer to question 2. if print(BFS_part2("012345678")), prints list of path length and frequency
    print(startstate)
    next = collections.deque([[startstate]])
    visited = {startstate}
    start = time.process_time()
    paths = {}
    while len(next) != 0:
        v = next.popleft()
        if(goal_test(v)):
            print("solved")
            for str in v:
                print_puzzle(str)
            #print(len(v)-1)
            end = time.process_time()   #instead of returning after goal found, BFS_part2 keeps running through all of states
            '''print("Number of Visited States: %s" %(len(visited)))
            print("seconds to run: %s" % (end - start))
            print()'''
        for child in get_children(v):
            if not child[-1] in visited:
                visited.add(child[-1])
                next.append(child)
                if(not len(child)-1 in paths.keys()):
                    paths[len(child)-1]=0
                paths[len(child)-1] = paths[len(child)-1]+1
    end = time.process_time()
    print("Number of Visited States: %s" %(len(visited)))
    print("seconds to run: %s" %(end-start))
    print()
    return paths
def parity_check(startstate):   #check if solvable for all sizes
    inversions = 0
    size = int(math.sqrt(len(startstate)))
    empty = startstate.index("0")
    if size%2==1:   #checks for parity in odd size puzzles
        startstate = startstate.replace("0", "")
        for x in range(0, len(startstate)):     #calculates # of inversions
            for y in range(0, x):
                if (startstate[x] < startstate[y]):
                    inversions += 1
        if(inversions%2==1):
            return 1
        else:
            return 0
    elif (size%2==0):   #checks for parity in even size puzzles
        startstate = startstate.replace("0", "")
        for x in range(0, len(startstate)):     #calculates # of inversions
            for y in range(0, x):
                if startstate[x] < startstate[y]:
                    inversions += 1
        if empty//size % 2 == 0:    #checks which line empty is in.
            if inversions % 2 == 1:
                return 1
            else:
                return 0
        else:
            if inversions % 2 == 0:
                return 1
            else:
                return 0
def get_children2(states):   #returns list of children by checking both 1 and 3 indexes away from "0"
    empty = states[-1].index("0")
    state = states[-1]
    previous = states[0]   #in order to add all previous states to the next child
    children = []
    if ((empty%size!=size-1)):
        child1 = swap_tiles(state,state[empty],state[empty+1])
        temp = previous + 'r'  #child includes all previous states as a list
        children.append((temp,child1))
    if ((empty%size!=0)):
        child2 = swap_tiles(state,state[empty],state[empty-1])
        temp = previous + "l"
        children.append((temp,child2))
    if (empty < len(state)-(size)):
        child3 = swap_tiles(state,state[empty],state[empty+size])
        temp = previous + 'd'
        children.append((temp,child3))
    if (empty > (size-1)):
        child4 = swap_tiles(state,state[empty],state[empty-size])
        temp = previous + 'u'
        children.append((temp,child4))
    return children
def get_children3(states):   #returns list of children by checking both 1 and 3 indexes away from "0"
    empty = states[-1].index("0")
    state = states[-1]
    previous = states[0]   #in order to add all previous states to the next child
    children = []
    if (empty < len(state)-(size)):
        child3 = swap_tiles(state,state[empty],state[empty+size])
        temp = previous + 'd'
        children.append((temp,states[1],states[2],child3))
    if (empty > (size-1)):
        child4 = swap_tiles(state,state[empty],state[empty-size])
        temp = previous + 'u'
        children.append((temp,states[1],states[2],child4))
    if ((empty%size!=size-1)):
        child1 = swap_tiles(state,state[empty],state[empty+1])
        temp = previous + 'r'  #child includes all previous states as a list
        children.append((temp,states[1],states[2],child1))
    if ((empty%size!=0)):
        child2 = swap_tiles(state,state[empty],state[empty-1])
        temp = previous + "l"
        children.append((temp,states[1],states[2],child2))
    return children
def BFS_edited(startstate, goals, sizes):
    global goal #edit global variables
    goal = goals
    global size
    size = sizes
    #print(startstate)
    next = collections.deque([('',startstate)])    #BFS algorithm from class of a list of states
    visited = {startstate}
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return False, visited, 0, end - start
    while len(next) != 0:
        v = next.popleft()
        if(goal_test(v)):
            end = time.process_time()
            #print("path length: " + str(len(v[0])) + ". seconds to run: %s" % (end - start) + "."+v[0])
            return True, visited, len(v[0]), end - start
        for child in get_children2(v):
            if not child[-1] in visited:
                visited.add(child[-1])  #add just new state, not whole child
                next.append(child)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start
def kDFS2(startstate, goals, sizes, depth):
    global goal  # edit global variables
    goal = goals
    global size
    size = sizes
    startdepth = 0
    visited = {startstate}
    next = [('', startdepth, visited, startstate)]  # BFS algorithm from class of a list of states
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return None
    while len(next) !=0:
        v = next.pop()
        if goal_test(v):
            end = time.process_time()
            return True, visited, len(v[0]), end - start
        if v[1]<depth:
            for c in get_children3(v):
                if c[-1] not in v[2]:
                    visit = set()
                    for strs in v[2]:
                        visit.add(strs)
                    visit.add(c[3])
                    c = (c[0],v[1]+1,visit,c[3])
                    next.append(c)
    return None
def get_children4(states):   #returns list of children by checking both 1 and 3 indexes away from "0"
    empty = states[-1].index("0")
    state = states[-1]
    previous = states[1]   #in order to add all previous states to the next child
    children = []
    if ((empty%size!=size-1)):
        child1 = swap_tiles(state,state[empty],state[empty+1])
        temp = previous + 'r'  #child includes all previous states as a list
        children.append((len(temp)+taxicabParity(states,size,goal),temp,child1))
    if ((empty%size!=0)):
        child2 = swap_tiles(state,state[empty],state[empty-1])
        temp = previous + "l"
        children.append((len(temp)+taxicabParity(states,size,goal),temp,child2))
    if (empty < len(state)-(size)):
        child3 = swap_tiles(state,state[empty],state[empty+size])
        temp = previous + 'd'
        children.append((len(temp)+taxicabParity(states,size,goal),temp,child3))
    if (empty > (size-1)):
        child4 = swap_tiles(state,state[empty],state[empty-size])
        temp = previous + 'u'
        children.append((len(temp)+taxicabParity(states,size,goal),temp,child4))
    return children
def Astar(startstate, goals, sizes):
    global goal #edit global variables
    goal = goals
    global size
    size = sizes
    next = [(0,'',startstate)]    #BFS algorithm from class of a list of states
    visited = {startstate}
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return False, visited, 0, end - start
    while len(next) != 0:
        v = heappop(next)
        if(goal_test(v)):
            end = time.process_time()
            print("path length: " + str(len(v[1])) + ". seconds to run: %s" % (end - start) + "."+v[1])
            return True, visited, len(v[1]), end - start
        for child in get_children4(v):
            if not child[-1] in visited:
                visited.add(child[-1])  #add just new state, not whole child
                heappush(next,child)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start
def IDDFS(startstate, goals, sizes, depth):
    for k in range((depth+1)):
        solution = kDFS2(startstate,goals,sizes,k)
        if solution!=None:
            return solution
    return None
def taxicabParity(state,sizes,goals):
    global goal  # edit global variables
    goal = goals
    global size
    size = sizes
    sizes = size**2
    totaldist = 0
    for x in state[-1]:
        if state[-1].index(x)==goal.index(x):
            totaldist+=0
        elif x!="0":
            index = goal.index(x)
            corrow = index % size
            corcol = index // size
            index2 = state[-1].index(x)
            row = index2 % size
            column = index2 // size
            totaldist+=abs(row-corrow)+abs(column-corcol)
    return totaldist
def indextogrid(targ,state,size):
    index = state[-1].index(targ)
    corrow = index%size
    corcol = index//size
    return corrow,corcol

print(BFS_part2("012345678"))
#BFS_edited("087654321","012345678",3)
#run_100_tests()
#filename = sys.argv[1]
print(taxicabParity((4,"0ABCDEFGHIJKLMNO"),4,"0ABCDEFGHIJKLMNO"))
filename = "8puzzle_tests.txt"
file = open(filename)
list = file.readlines()
totaltime = 0
for x in range(1, len(list)):
    list[x]=list[x].rstrip()
    if list[x] != '':
        #totaltime+=kDFS(str(list[x]),str(list[0].rstrip()),4,30)[3]
        print(list[x])
        start = time.process_time()
        temp = IDDFS(str(list[x]), str(list[0].rstrip()), 4, 53)
        #Astar(str(list[x]),str(list[0].rstrip()),4)
        end = time.process_time()
        if temp != None:
            print("IDDFS: " + str(temp[2])+ " " + str(end-start))
            totaltime += end-start
        try:
            temp = BFS_edited(str(list[x]), str(list[0].rstrip()), 4)
            if temp != None:
                print("BFS: " + str(temp[2]) + " " + str(temp[-1]))
                totaltime += temp[3]
        except:
            print("Memory Error")
print("total run time: " + str(totaltime))

