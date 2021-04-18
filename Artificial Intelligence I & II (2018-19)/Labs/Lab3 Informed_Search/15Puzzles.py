import collections
import time
import random
import cProfile
import math
import sys
from heapq import heappop, heappush

# global variables
goal = "012345678"
size = 3


def goal_test(state):  # returns goal test if state is equal to goal
    if state[-1] == goal:
        return True
    return False


def swap_tiles(state, char1, char2):  # used to swap the values from get_children() to make the actual new children
    state = state.replace(char2, "\"")
    state = state.replace(char1, char2)
    state = state.replace("\"", char1)
    return state


def parity_check(startstate):  # check if solvable for all sizes
    inversions = 0
    size = int(math.sqrt(len(startstate)))
    empty = startstate.index("0")
    if size % 2 == 1:  # checks for parity in odd size puzzles
        startstate = startstate.replace("0", "")
        for x in range(0, len(startstate)):  # calculates # of inversions
            for y in range(0, x):
                if (startstate[x] < startstate[y]):
                    inversions += 1
        if (inversions % 2 == 1):
            return 1
        else:
            return 0
    elif (size % 2 == 0):  # checks for parity in even size puzzles
        startstate = startstate.replace("0", "")
        for x in range(0, len(startstate)):  # calculates # of inversions
            for y in range(0, x):
                if startstate[x] < startstate[y]:
                    inversions += 1
        if empty // size % 2 == 0:  # checks which line empty is in.
            if inversions % 2 == 1:
                return 1
            else:
                return 0
        else:
            if inversions % 2 == 0:
                return 1
            else:
                return 0


def get_children2(states):  # returns list of children by checking both 1 and 3 indexes away from "0"
    empty = states[-1].index("0")
    state = states[-1]
    previous = states[0]  # in order to add all previous states to the next child
    children = []
    if ((empty % size != size - 1)):
        child1 = swap_tiles(state, state[empty], state[empty + 1])
        temp = previous + 'r'  # child includes all previous states as a list
        children.append((temp, child1))
    if ((empty % size != 0)):
        child2 = swap_tiles(state, state[empty], state[empty - 1])
        temp = previous + "l"
        children.append((temp, child2))
    if (empty < len(state) - (size)):
        child3 = swap_tiles(state, state[empty], state[empty + size])
        temp = previous + 'd'
        children.append((temp, child3))
    if (empty > (size - 1)):
        child4 = swap_tiles(state, state[empty], state[empty - size])
        temp = previous + 'u'
        children.append((temp, child4))
    return children


def get_children3(states):  # returns list of children by checking both 1 and 3 indexes away from "0"
    empty = states[-1].index("0")
    state = states[-1]
    previous = states[0]  # in order to add all previous states to the next child
    children = []
    if (empty < len(state) - (size)):
        child3 = swap_tiles(state, state[empty], state[empty + size])
        temp = previous + 'd'
        children.append((temp, states[1], states[2], child3))
    if (empty > (size - 1)):
        child4 = swap_tiles(state, state[empty], state[empty - size])
        temp = previous + 'u'
        children.append((temp, states[1], states[2], child4))
    if ((empty % size != size - 1)):
        child1 = swap_tiles(state, state[empty], state[empty + 1])
        temp = previous + 'r'  # child includes all previous states as a list
        children.append((temp, states[1], states[2], child1))
    if ((empty % size != 0)):
        child2 = swap_tiles(state, state[empty], state[empty - 1])
        temp = previous + "l"
        children.append((temp, states[1], states[2], child2))
    return children


def BFS_edited(startstate, goals, sizes):
    global goal  # edit global variables
    goal = goals
    global size
    size = sizes
    count = 0
    # print(startstate)
    next = collections.deque([('', startstate)])  # BFS algorithm from class of a list of states
    visited = {startstate}
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return False, visited, 0, end - start
    while len(next) != 0:
        v = next.popleft()
        count += 1
        if (goal_test(v)):
            end = time.process_time()
            # print("path length: " + str(len(v[0])) + ". seconds to run: %s" % (end - start) + "."+v[0])
            return True, visited, len(v[0]), end - start, count
        for child in get_children2(v):
            if not child[-1] in visited:
                visited.add(child[-1])  # add just new state, not whole child
                next.append(child)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start, count


def kDFS2(startstate, goals, sizes, depth):
    global goal  # edit global variables
    goal = goals
    global size
    size = sizes
    startdepth = 0
    count = 0
    visited = {startstate}
    next = [('', startdepth, visited, startstate)]  # BFS algorithm from class of a list of states
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        #print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return None, count
    while len(next) != 0:
        v = next.pop()
        count += 1
        if goal_test(v):
            end = time.process_time()
            return True, visited, len(v[0]), end - start, count
        if v[1] < depth:
            for c in get_children3(v):
                if c[-1] not in v[2]:
                    visit = set()
                    for strs in v[2]:
                        visit.add(strs)
                    visit.add(c[3])
                    c = (c[0], v[1] + 1, visit, c[3])
                    next.append(c)
    return None, count


def get_childrenA2(states):  # returns list of children by checking both 1 and 3 indexes away from "0"
    empty = states[-1].index("0")
    state = states[-1]
    previous = states[2]  # in order to add all previous states to the next child
    children = []
    if (empty < len(state) - (size)):
        child3 = swap_tiles(state, state[empty], state[empty + size])
        temp = previous + 'd'
        children.append((temp, child3))
    if (empty > (size - 1)):
        child4 = swap_tiles(state, state[empty], state[empty - size])
        temp = previous + 'u'
        children.append((temp, child4))
    if ((empty % size != size - 1)):
        child1 = swap_tiles(state, state[empty], state[empty + 1])
        temp = previous + 'r'  # child includes all previous states as a list
        children.append((temp, child1))
    if ((empty % size != 0)):
        child2 = swap_tiles(state, state[empty], state[empty - 1])
        temp = previous + "l"
        children.append((temp, child2))
    return children


def Astar4(startstate, goals, sizes, m): #the god of all Astar jk Astar with implementation of the required explorations
    global goal  # edit global variables
    goal = goals
    global size
    size = sizes
    next = [(manhattan(startstate, size, goal), random.random(), '',
             startstate)]  # BFS algorithm from class of a list of states
    visited = set()
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        #print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return False, visited, 0, end - start
    while len(next) != 0:
        v = heappop(next)
        '''heuris = m * (len(v[1]) + 1) + manhattan(v, size, goal)
        if (str(heuris)+v[-1]) in visited:
            continue
        visited.add((str(heuris)+v[-1]))'''
        if (goal_test(v)):
            end = time.process_time()
            #print("path length: " + str(len(v[2])) + ". seconds to run: %s" % (end - start) + "." + v[2])
            return True, visited, len(v[2]), end - start
        for child in get_childrenA2(v):
            heuris = m * (len(v[2]) + 1) + manhattan(child[-1], size, goal)
            if not (str(heuris) + child[-1]) in visited:
                visited.add((str(heuris) + child[-1]))
                heappush(next, (heuris, random.random(), child[0], child[-1]))
    end = time.process_time()
    #print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start


def get_childrenA(states):  # returns list of children by checking both 1 and 3 indexes away from "0"
    empty = states[-1].index("0")
    state = states[-1]
    previous = states[2]  # in order to add all previous states to the next child
    children = []
    if (empty < len(state) - (size)):
        child3 = swap_tiles(state, state[empty], state[empty + size])
        temp = previous + 'd'
        children.append((temp, child3))
    if (empty > (size - 1)):
        child4 = swap_tiles(state, state[empty], state[empty - size])
        temp = previous + 'u'
        children.append((temp, child4))
    if ((empty % size != size - 1)):
        child1 = swap_tiles(state, state[empty], state[empty + 1])
        temp = previous + 'r'  # child includes all previous states as a list
        children.append((temp, child1))
    if ((empty % size != 0)):
        child2 = swap_tiles(state, state[empty], state[empty - 1])
        temp = previous + "l"
        children.append((temp, child2))
    return children


def Astar5(startstate, goals, sizes, m): #working order messed up, essentially Astar 4
    global goal  # edit global variables
    goal = goals
    global size
    size = sizes
    next = [(manhattan(startstate, size, goal), random.randint(0, 100), '',
             startstate)]  # BFS algorithm from class of a list of states
    visited = set()
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return False, visited, 0, end - start
    while len(next) != 0:
        v = heappop(next)
        '''heuris = m * (len(v[1]) + 1) + manhattan(v, size, goal)
        if (str(heuris)+v[-1]) in visited:
            continue
        visited.add((str(heuris)+v[-1]))'''
        if (goal_test(v)):
            end = time.process_time()
            print("path length: " + str(len(v[2])) + ". seconds to run: %s" % (end - start) + "." + v[2])
            return True, visited, len(v[2]), end - start
        for child in get_childrenA(v):
            heuris = m * (len(v[2]) + 1) + manhattan(child[-1], size, goal)
            if not (str(heuris) + child[-1]) in visited:
                visited.add((str(heuris) + child[-1]))
                heappush(next, (heuris, random.randint(0, 100), child[0], child[-1]))
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start


def Astar3B(startstate, goals, sizes, m): # modified to calculate nodes/ sec for A*, nodes/sec IDDFS and BFS with counter within their code segments
    global goal  # edit global variables
    goal = goals
    global size
    size = sizes
    count = 0
    next = [(manhattan(startstate, size, goal), random.randint(0, 100), '',
             startstate)]  # BFS algorithm from class of a list of states
    visited = set()
    start = time.process_time()
    if (parity_check(startstate) != parity_check(goals)):
        end = time.process_time()
        print("No Solution." + " seconds to run: %s" % (end - start) + ".")
        return False, visited, 0, end - start
    while len(next) != 0:
        v = heappop(next)
        count += 1
        '''heuris = m * (len(v[1]) + 1) + manhattan(v, size, goal)
        if (str(heuris)+v[-1]) in visited:
            continue
        visited.add((str(heuris)+v[-1]))'''
        if (goal_test(v)):
            end = time.process_time()
            print("path length: " + str(len(v[2])) + ". seconds to run: %s" % (end - start) + "." + v[2])
            return True, visited, len(v[2]), end - start, count
        for child in get_childrenA(v):
            heuris = m * (len(v[2]) + 1) + manhattan(child[-1], size, goal)
            if not (str(heuris) + child[-1]) in visited:
                visited.add((str(heuris) + child[-1]))
                heappush(next, (heuris, random.randint(0, 100), child[0], child[-1]))
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start, count


def IDDFS(startstate, goals, sizes, depth):
    count = 0
    for k in range((depth + 1)):
        solution = kDFS2(startstate, goals, sizes, k)
        count+=solution[-1]
        if solution[0] != None:
            return (solution[0],solution[1],solution[2],solution[3],count)
    return None


def manhattan(state, sizes, goals): #returns estimate of distance of state to goal - never overestimating
    global goal  # edit global variables
    goal = goals
    global size
    size = sizes
    sizes = size ** 2
    totaldist = 0
    for x in state:
        index = goal.index(x)
        index2 = state.index(x)
        if index == index2:
            totaldist += 0
        elif x != "0":
            corrow = index // size
            corcol = index % size

            row = index2 // size
            column = index2 % size
            totaldist += abs(row - corrow) + abs(column - corcol)
    return totaldist


def BFS3C(startstate, sizes): #original code found frequency of pathlengths, edited to return dictionary of pathlengths to states
    global size
    size = sizes
    print(startstate)
    next = collections.deque([('', startstate)])
    visited = {startstate}
    start = time.process_time()
    paths = {}
    while len(next) != 0:
        v = next.popleft()
        if (goal_test(v)):
            print("solved")
            # print(len(v)-1)
        end = time.process_time()  # instead of returning after goal found, BFS_part2 keeps running through all of states
        for child in get_children2(v):
            if not child[-1] in visited:
                visited.add(child[-1])
                next.append(child)
                if (not len(child[0]) in paths.keys()):
                    paths[len(child[0])] = [child[-1]] #add states instead of frequency
                paths[len(child[0])].append(child[-1])
    end = time.process_time()
    print("Number of Visited States: %s" % (len(visited)))
    print("seconds to run: %s" % (end - start))
    print()
    for x in paths.keys():
        print(paths[x][random.randint(0, len(paths[x]) - 1)])
    return paths


def BFS3D(startstate, sizes): #essentially same as above but with a breakpoint to ensure code can give an output at some time
    global size
    size = sizes
    print(startstate)
    next = collections.deque([('', startstate)])
    visited = {startstate}
    start = time.process_time()
    paths = {}
    while len(next) != 0:
        v = next.popleft()
        if (goal_test(v)):
            print("solved")
            # print(len(v)-1)
        end = time.process_time()  # instead of returning after goal found, BFS_part2 keeps running through all of states
        for child in get_children2(v):
            if not child[-1] in visited:
                visited.add(child[-1])
                next.append(child)
                if (not len(child[0]) in paths.keys()):
                    paths[len(child[0])] = [child[-1]]
                paths[len(child[0])].append(child[-1])
        if len(paths.keys()) == 30:
            for x in paths.keys():
                print(paths[x][random.randint(0, len(paths[x]) - 1)])
            return paths
    end = time.process_time()
    print("Number of Visited States: %s" % (len(visited)))
    print("seconds to run: %s" % (end - start))
    print()
    for x in paths.keys():
        print(paths[x][random.randint(0, len(paths[x]) - 1)])
    return paths


# paths = BFS3C("012345678",3)
# paths = BFS3D("0ABCDEFGHIJKLMNOPQRSTUVWX",5)
# BFS_edited("087654321","012345678",3)
# run_100_tests()
# filename = sys.argv[1]
#Astar4("ALBCDG0KHIEFQMNUJTRSOPVWX","0ABCDEFGHIJKLMNOPQRSTUVWX",5,1)
'''filename = "15_puzzles.txt"
file = open(filename)
list = file.readlines()
totaltime = 0
#for x in range(0, 20):
Astar4("A0BCDEFGHIJKLMNO","0ABCDEFGHIJKLMNO",4,1)'''
'''
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, .5)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, .6)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, .7)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, .8)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, .9)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, 1)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, 1.1)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, 1.2)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, 1.3)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, 1.4)
temp = Astar4(str(list[30].rstrip()), str(list[0].rstrip()), 4, 1.5)
'''
'''for  x in range(1, len(list)):
    list[x] = list[x].rstrip()
    if list[x] != '':
        print("Puzzle: " + str(x) + " " + list[x])
        start = time.process_time()
        temp = IDDFS(str(list[x]), str(list[0].rstrip()), 4, 53)
        temp = Astar3B(str(list[x]), "0ABCDEFGHIJKLMNO", 4,1)

        if temp[-2]>10: #when running Astar
            print("Nodes per Second: "+str(temp[-1]/temp[-2]))
        end = time.process_time()

        if temp != None:
            print("IDDFS: " + str(temp[2])+ " " + str(end-start))
            totaltime += end-start
            if end-start>10:
                print("Nodes per Second: "+str(temp[-1]/(end-start)))
        try:
            temp = BFS_edited(str(list[x]), str(list[0].rstrip()), 4)
            if temp != None:
                print("BFS: " + str(temp[2]) + " " + str(temp[-2]))
                totaltime += temp[3]
            if temp[-2]>10:
                print("Nodes per Second: "+str(temp[-1]/temp[-2]))
        except:
            print("Memory Error")'''

#operation = sys.argv[1]
#state = sys.argv[2]
filename = sys.argv[1]
file = open(filename)
list = file.readlines()
for  x in range(0, len(list)):
    list[x] = list[x].rstrip()
    if list[x] != '':
        operation = list[x][0]
        state = list[x][2:]
        if operation == "B":
            temp = BFS_edited(state,"0ABCDEFGHIJKLMNO",4)
            print(str(temp[2])+ " BFS " + str(temp[-2]))
        if operation == "I":
            temp = IDDFS(state,"0ABCDEFGHIJKLMNO",4,50)
            print(str(temp[2])+ " ID-DFS " + str(temp[-2]))
        if operation == "2":
            print("Bidirectional BFS was not implemented.")
        if operation == "A":
            temp = Astar4(state,"0ABCDEFGHIJKLMNO",4,1)
            print(str(temp[2])+ " A* " + str(temp[-1]))
        if operation == "7":
            temp = Astar4(state,"0ABCDEFGHIJKLMNO",4,0.7)
            print(str(temp[2]) + " A*: 0.7 " + str(temp[-1]))
            temp = Astar4(state, "0ABCDEFGHIJKLMNO", 4, 0.7)
            print(str(temp[2]) + " A*: 0.7 " + str(temp[-1]))
            temp = Astar4(state, "0ABCDEFGHIJKLMNO", 4, 0.7)
            print(str(temp[2]) + " A*: 0.7 " + str(temp[-1]))
        if operation == "!":
            temp = BFS_edited(state, "0ABCDEFGHIJKLMNO", 4)
            print(str(temp[2]) + " BFS " + str(temp[-2]))
            temp = IDDFS(state, "0ABCDEFGHIJKLMNO", 4, 50)
            print(str(temp[2]) + " ID-DFS " + str(temp[-2]))
            print("Bidirectional BFS was not implemented.")
            temp = Astar4(state, "0ABCDEFGHIJKLMNO", 4, 1)
            print(str(temp[2]) + " A* " + str(temp[-1]))
            temp = Astar4(state, "0ABCDEFGHIJKLMNO", 4, 0.7)
            print(str(temp[2]) + " A*: 0.7 " + str(temp[-1]))
            temp = Astar4(state, "0ABCDEFGHIJKLMNO", 4, 0.7)
            print(str(temp[2]) + " A*: 0.7 " + str(temp[-1]))
            temp = Astar4(state, "0ABCDEFGHIJKLMNO", 4, 0.7)
            print(str(temp[2]) + " A*: 0.7 " + str(temp[-1]))
