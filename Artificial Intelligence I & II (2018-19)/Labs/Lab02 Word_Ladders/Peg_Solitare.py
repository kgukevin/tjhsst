import collections
import time
goal = "x00000000000000"
size = 15
def goal_test(start):
    for x in range(len(start[-1])):
        z = start[-1][x]
        y = goal[x]
        if start[-1][x] != goal[x]:
            return False
    return True

def get_children(states):
    empty = states[-1].index("0")
    state = list(states[-1])
    previous = states  # in order to add all previous states to the next child
    children = []
    if (empty == 0):
        state = list(states[-1])
        if (state[1]=="x") & (state[3]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 3, empty)
            child1[1]="0"
            child1= "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[2] == "x") & (state[5] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 5, empty)
            child2[2] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 1):
        state = list(states[-1])
        if (state[3]=="x") & (state[6]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 6, empty)
            child1[3]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[4] == "x") & (state[8] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 8, empty)
            child2[4] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 2):
        state = list(states[-1])
        if (state[4]=="x") & (state[7]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 7, empty)
            child1[4]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[5] == "x") & (state[9] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 9, empty)
            child2[5] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 3):
        state = list(states[-1])
        if (state[10]=="x") & (state[6]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 10, empty)
            child1[6]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[7] == "x") & (state[12] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 12, empty)
            child2[7] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
        if (state[4] == "x") & (state[5] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 5, empty)
            child2[4] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
        if (state[1] == "x") & (state[0] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 0, empty)
            child2[1] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 4):
        state = list(states[-1])
        if (state[7]=="x") & (state[11]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 11, empty)
            child1[7]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[13] == "x") & (state[8] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 13, empty)
            child2[8] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 5):
        state = list(states[-1])
        if (state[12]=="x") & (state[8]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state,12, empty)
            child1[8]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[14] == "x") & (state[9] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state,14, empty)
            child2[9] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
        if (state[3] == "x") & (state[4] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 3, empty)
            child2[4] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
        if (state[0] == "x") & (state[2] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 0, empty)
            child2[2] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 6):
        state = list(states[-1])
        if (state[8]=="x") & (state[7]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 8, empty)
            child1[7]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[1] == "x") & (state[3] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 1, empty)
            child2[3] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 7):
        state = list(states[-1])
        if (state[9]=="x") & (state[8]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, state[9], state[empty])
            child1[8]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[2] == "x") & (state[4] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 2, empty)
            child2[4] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 8):
        state = list(states[-1])
        if (state[6]=="x") & (state[7]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 6, empty)
            child1[7]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[1] == "x") & (state[4] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 1,empty)
            child2[4] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 9):
        state = list(states[-1])
        if (state[7]=="x") & (state[8]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 7, empty)
            child1[8]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[2] == "x") & (state[5] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state,2, empty)
            child2[5] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 10):
        state = list(states[-1])
        if (state[3]=="x") & (state[6]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 3, empty)
            child1[6]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[12] == "x") & (state[11] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 12, empty)
            child2[11] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 11):
        state = list(states[-1])
        if (state[4]=="x") & (state[7]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 4, empty)
            child1[7]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[13] == "x") & (state[12] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 13, empty)
            child2[12] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 12):
        state = list(states[-1])
        if (state[10]=="x") & (state[11]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 10, empty)
            child1[11]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[14] == "x") & (state[13] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 14, empty)
            child2[13] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
        if (state[3]=="x") & (state[7]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 3, empty)
            child1[7]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[5] == "x") & (state[8] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 5, empty)
            child2[8] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 13):
        state = list(states[-1])
        if (state[4]=="x") & (state[8]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 4, empty)
            child1[8]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[11] == "x") & (state[12] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 11, empty)
            child2[12] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    if (empty == 14):
        state = list(states[-1])
        if (state[12]=="x") & (state[13]=="x"):
            state = list(states[-1])
            child1 = swap_tiles(state, 12, empty)
            child1[13]="0"
            child1 = "".join(child1)
            temp = previous + [child1]  # child includes all previous states as a list
            children.append(temp)
        if (state[5] == "x") & (state[9] == "x"):
            state = list(states[-1])
            child2 = swap_tiles(state, 5,empty)
            child2[9] = "0"
            child2 = "".join(child2)
            temp = previous + [child2]
            children.append(temp)
    return children
def swap_tiles(state,char1,char2):  #used to swap the values from get_children() to make the actual new children
    states = state
    temp = states[char1]
    states[char1]=states[char2]
    states[char2]=temp
    return state
def get_children2(states):
    emptys = set()
    for x in range(len(states[-1])):
        if states[-1].find("0",x,len(states[-1]))==-1:
            break
        emptys.add(states[-1].find("0",x,len(states[-1])))
    state = states[-1]
    previous = states
    children = []
    for empty in emptys:
        if (empty == 0):
            children.append(jump_piece(state, previous, empty, 3, 1))
            children.append(jump_piece(state, previous, empty, 5, 2))
        if (empty == 1):
            children.append(jump_piece(state, previous, empty, 6, 3))
            children.append(jump_piece(state, previous, empty, 8, 4))
        if (empty == 2):
            children.append(jump_piece(state, previous, empty, 7, 4))
            children.append(jump_piece(state, previous, empty, 9, 5))
        if (empty == 3):
            children.append(jump_piece(state, previous, empty, 10, 6))
            children.append(jump_piece(state, previous, empty, 12, 7))
            children.append(jump_piece(state, previous, empty, 5, 4))
            children.append(jump_piece(state, previous, empty, 0, 1))
        if (empty == 4):
            children.append(jump_piece(state, previous, empty, 11, 7))
            children.append(jump_piece(state, previous, empty, 13, 8))
        if (empty == 5):
            children.append(jump_piece(state, previous, empty, 12, 8))
            children.append(jump_piece(state, previous, empty, 14, 9))
            children.append(jump_piece(state, previous, empty, 3, 5))
            children.append(jump_piece(state, previous, empty, 0, 2))
        if (empty == 6):
            children.append(jump_piece(state, previous, empty, 8, 7))
            children.append(jump_piece(state, previous, empty, 1, 3))
        if (empty == 7):
            children.append(jump_piece(state, previous, empty, 2, 4))
            children.append(jump_piece(state, previous, empty, 9, 8))
        if (empty == 8):
            children.append(jump_piece(state, previous, empty, 6, 7))
            children.append(jump_piece(state, previous, empty, 1, 4))
        if (empty == 9):
            children.append(jump_piece(state, previous, empty, 7, 8))
            children.append(jump_piece(state, previous, empty, 2, 5))
        if (empty == 10):
            children.append(jump_piece(state, previous, empty, 3, 6))
            children.append(jump_piece(state, previous, empty, 12, 11))
        if (empty == 11):
            children.append(jump_piece(state, previous, empty, 4, 7))
            children.append(jump_piece(state, previous, empty, 13, 12))
        if (empty == 12):
            children.append(jump_piece(state, previous, empty, 10, 11))
            children.append(jump_piece(state, previous, empty, 14, 13))
            children.append(jump_piece(state, previous, empty, 3, 7))
            children.append(jump_piece(state, previous, empty, 5, 8))
        if (empty == 13):
            children.append(jump_piece(state, previous, empty, 11, 12))
            children.append(jump_piece(state, previous, empty, 4, 8))
        if (empty == 14):
            children.append(jump_piece(state, previous, empty, 12, 13))
            children.append(jump_piece(state, previous, empty, 5, 9))
    r=len(children)
    return children
def jump_piece(state,previous,empty,jump,jumped):
    states = list(state)
    if (states[jump]=="x") & (states[jumped] == "x"):
        temp = states[jump]
        states[jump] = states[empty]
        states[empty] = temp
        states[jumped]="0"
        states = "".join(states)
        child = previous+[states]
        return child
    return previous
def print_puzzle(state):
    print("    "+state[0])
    print("   "+state[1]+" "+state[2])
    print("  "+state[3]+" "+state[4]+" "+state[5])
    print(" "+state[6]+" "+state[7]+" "+state[8]+" "+state[9])
    print(state[10]+" "+state[11]+" "+state[12]+" "+state[13]+" "+state[14])
def BFS(startstate):
    #print(startstate)
    next = collections.deque([[startstate]])    #BFS algorithm from class of a list of states
    visited = {startstate}
    start = time.process_time()
    while len(next) != 0:
        v = next.popleft()
        x = len(v)
        if(goal_test(v)):
            end = time.process_time()
            for x in v:
                print_puzzle(x)
            print("path length: " + str(len(v)-1) + ". seconds to run: %s" % (end - start) + ".")
            return True, visited, len(v)-1, end - start
        for child in get_children2(v):
            if not child[-1] in visited:
                visited.add(child[-1])  #add just new state, not whole child
                next.append(child)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start
BFS("0xxxxxxxxxxxxxx")