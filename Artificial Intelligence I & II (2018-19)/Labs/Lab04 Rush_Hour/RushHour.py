import collections
import time

# car = (y-coor, x-coor, dir)
goalcar = (((2, 0), (2, 1)), "R", "s")
car1 = (((0, 3), (0, 4), (0, 5)), "A", "s")
car2 = (((2, 4), (3, 4), (4, 4)), "B", "u")
car3 = (((3, 2), (4, 2)), "C", "u")
car4 = (((5, 3), (5, 4)), "D", "s")
states = [goalcar, car1, car2, car3, car4]

'''car1 = (((0,0),(1,0),(2,0)),"A","u")
car2 = (((0,1),(0,2)),"B","s")
car3 = (((1,1),(2,1)),"C","u")
car4 = (((1,2),(2,2)),"D","u")
car5 = (((3,0),(3,1),(3,2)),"E","s")
car6 = (((4,2),(5,2)),"F","u")
car7 = (((5,0),(5,1)),"G","s")
car8 = (((3,3),(4,3)),"H","u")
car9 = (((5,3),(5,4)),"I","s")
car10 = (((4,4),(4,5)),"J","s")
car11 = (((1,5),(2,5),(3,5)),"K","u")
car12 = (((0,4),(1,4)),"L","u")
goalcar = (((2,3),(2,4)),"R","s")
states = [goalcar,car1,car2,car3,car4,car5,car6,car7,car8,car9,car10,car11,car12]
'''
'''goalcar = (((2, 2), (2, 3)), "R", "s")
car1 = (((1, 0), (2, 0)), "A", "u")
car2 = (((4, 1), (5, 1)), "B", "u")
car3 = (((3, 2), (4, 2)), "C", "u")
car4 = (((0, 3), (1, 3)), "D", "u")
car5 = (((0, 4), (1, 4), (2, 4)), "E", "u")
car6 = (((0, 5), (1, 5), (2, 5)), "F", "u")
car13 = (((0, 0), (0, 1), (0, 2)), "G", "s")
car14 = (((1, 1), (1, 2)), "H", "s")
car16 = (((3, 0), (3, 1)), "I", "s")
car17 = (((4, 4), (4, 5)), "J", "s")
car18 = (((5, 2), (5, 3)), "K", "s")
car24 = (((5, 4), (5, 5)), "L", "s")
states = [goalcar, car1, car2, car3, car4, car5, car6, car13, car14, car16, car17, car18, car24]
'''

#states = ["002Au","202Bs","232Rs"]
#states = ["003Au","012Bs","112Cu","122Du","303Es","422Fu","502Gs","332Hu","532Is","442Js","153Ku","042Lu","232Rs"]
states = ['002As','112Bu','202Cu','312Ds','032Eu','142Fs','242Gu','422Hu','502Is','432Js','252Ku','222Rs']
#states = ["003Au","013Bu","023Cs","143Du","122Es","052Fu","252Gu","302Hs","322Iu","432Js","512Ks","532Ls","222Rs"]
states = ["202Rs","012Au","022Bs","122Cs","152Du","223Eu","232Fu","342Gs","402Hu","513Is","432Js","452Ku"]
def state_maker(state):
    stater = []
    for strings in state:
        origin = (int(strings[0]),int(strings[1]))
        length = int(strings[2])
        direction = strings[4]
        name = strings[3]
        coordinates = []
        if direction == "s":
            for x in range(0,length):
                coordinates.append((origin[0],origin[1]+x))
        if direction == "u":
            for y in range(0,length):
                coordinates.append((origin[0]+y,origin[1]))
        stater.append((tuple(coordinates),name,direction))
    return stater


def print_puzzle(state):
    str = {0: ["  ", "  ", "  ", "  ", "  ", "  "],
           1: ["  ", "  ", "  ", "  ", "  ", "  "],
           2: ["  ", "  ", "  ", "  ", "  ", "  "],
           3: ["  ", "  ", "  ", "  ", "  ", "  "],
           4: ["  ", "  ", "  ", "  ", "  ", "  "],
           5: ["  ", "  ", "  ", "  ", "  ", "  "]}
    for cars in state:
        for x in cars[0]:
            str[x[0]][x[1]] = cars[-2]+" "
    for y in str.keys():
        print("|"+"".join(str[y])+"|")


def goal_check(state):
    for cars in state:
        if cars[-2] == "R":
            if cars[0][-1][-1] == 5:
                return True
    return False


def get_children(stated):
    state = list(stated)
    children = []
    for cars in stated:
        move = moves2(state, cars)
        for new in move:
            state.remove(cars)
            if cars[-1] == "s":
                if len(cars[0]) == 2:
                    newcar = ((new, (new[0], new[1] + 1)), cars[-2], "s")
                    state.append(newcar)
                    children.append(tuple(state))
                elif len(cars[0]) == 3:
                    newcar = ((new, (new[0], new[1] + 1), (new[0], new[1] + 2)), cars[-2], "s")
                    state.append(newcar)
                    children.append(tuple(state))
            elif cars[-1] == "u":
                if len(cars[0]) == 2:
                    newcar = ((new, (new[0] + 1, new[1])), cars[-2], "u")
                    state.append(newcar)
                    children.append(tuple(state))
                if len(cars[0]) == 3:
                    newcar = ((new, (new[0] + 1, new[1]), (new[0] + 2, new[1])), cars[-2], "u")
                    state.append(newcar)
                    children.append(tuple(state))
            state = list(stated)
    return children


def moves(state, target):
    moves = set()
    block = blocked(state, target)
    if target[-1] == "s":
        y = target[0][0][0]
        for x in range(0, 6 - len(target[0]) + 1):
            if ((y, x) not in block) & ((y, x + len(target[0]) - 1) not in block) & (
                    (y, x + len(target[0]) - 2) not in block) & (
                    (y, x) != target[0][0]):
                moves.add((y, x))
    elif target[-1] == "u":
        x = target[0][0][1]
        for y in range(0, 6 - len(target[0]) + 1):
            if ((y, x) not in block) & ((y + len(target[0]) - 1, x) not in block) & (
                    (y + len(target[0]) - 2, x) not in block) & (
                    (y, x) != target[0][0]):
                moves.add((y, x))
    for coor in block:
        if coor in moves:
            moves.remove(coor)
    return moves

def moves2(state, target):
    moves = []
    block = blocked2(state, target)
    if target[-1] == 's':
        y = target[0][0][0]
        for x in range(0, 6 - len(target[0]) + 1):
            if ((y, x) not in block) & ((y, x + len(target[0]) - 1) not in block) & (
                    (y, x + len(target[0]) - 2) not in block) & (
                    (y, x) != target[0][0]):
                moves.append((y,x))
    if target[-1] == 'u':
        x = target[0][0][1]
        for y in range(0, 6 - len(target[0]) + 1):
            if ((y, x) not in block) & ((y + len(target[0]) - 1, x) not in block) & (
                    (y + len(target[0]) - 2, x) not in block) & (
                    (y, x) != target[0][0]):
                moves.append((y, x))
    return moves


def blocked(state, target):
    blocks = set()
    block = {0: set(),
             1: set(),
             2: set(),
             3: set(),
             4: set(),
             5: set()}
    if target[-1] == "s":
        for y in block.keys():
            if y != target[0][0][0]:
                for x in range(0, 6):
                    block[y].add(x)

    elif target[-1] == "u":
        for y in block.keys():
            for x in range(0, 6):
                if x != target[0][0][1]:
                    block[y].add(x)

    for cars in state:
        if target != cars:
            for coor in cars[0]:
                block[coor[0]].add(coor[1])
                if (target[-1] == "s") & (coor[0] == target[0][0][0]):
                    if target[0][0][1] < coor[1]:
                        for num in range(coor[1], 6):
                            block[target[0][0][0]].add(num)
                    elif target[0][0][1] > coor[1]:
                        for num in range(0, coor[1]):
                            block[target[0][0][0]].add(num)
                if (target[-1] == "u") & (coor[1] == target[0][0][1]):
                    if target[0][0][0] < coor[0]:
                        for num in range(coor[0], 6):
                            block[num].add(coor[1])
                    elif target[0][0][0] > coor[0]:
                        for num in range(0, coor[0]):
                            block[num].add(coor[1])
    for y in block.keys():
        #print(block[y])
        for x in block[y]:
            blocks.add((y, x))
    return blocks

def blocked2(state, target):
    blocks = set()
    y = target[0][0][0]
    x = target[0][0][1]
    '''for cars in state:
        if target[-1]=="s":
            if cars[0][0][0]==y:
                blocks.add((cars[0][0][0],cars[0][0][1]))
                if cars[0][0][1]<x:
                    for num in range(0, cars[0][0][1]):
                        blocks.add((cars[0][0][0],num))
                elif cars[0][0][1]>x:
                    for num in range(cars[0][0][1],6):
                        blocks.add((cars[0][0][0],num))
        if target[-1] == "u":
            if cars[0][0][1] == x:
                blocks.add((cars[0][0][0], cars[0][0][1]))
                if cars[0][0][0]<y:
                    for num in range(0, cars[0][0][0]):
                        blocks.add((num, cars[0][0][1]))
                elif cars[0][0][0]>y:
                    for num in range(cars[0][0][0],6):
                        blocks.add((num, cars[0][0][1]))'''

    if target[-1] == "s":
        for cars in state:
            if cars != target:
                if cars[0][0][0] == y:
                        blocks.add((cars[0][0][0], cars[0][0][1]))
                        if cars[0][0][1] < x:
                            for num in range(0, cars[0][0][1]):
                                blocks.add((cars[0][0][0], num))
                        elif cars[0][0][1] > x:
                            for num in range(cars[0][0][1], 6):
                                blocks.add((cars[0][0][0], num))
                if cars[0][1][0] == y:
                        blocks.add((cars[0][1][0], cars[0][1][1]))
                        if cars[0][1][1] < x:
                            for num in range(0, cars[0][1][1]):
                                blocks.add((cars[0][1][0], num))
                        elif cars[0][1][1] > x:
                            for num in range(cars[0][1][1], 6):
                                blocks.add((cars[0][1][0], num))
                if len(cars[0])==3:
                    if cars[0][2][0]==y:
                        blocks.add((cars[0][2][0], cars[0][2][1]))
                        if cars[0][2][1] < x:
                            for num in range(0, cars[0][2][1]):
                                blocks.add((cars[0][2][0], num))
                        elif cars[0][2][1] > x:
                            for num in range(cars[0][2][1], 6):
                                blocks.add((cars[0][2][0], num))
    if target[-1] == "u":
        for cars in state:
            if cars != target:
                if cars[0][0][1] == x:
                        blocks.add((cars[0][0][0], cars[0][0][1]))
                        if cars[0][0][0] < y:
                            for num in range(0, cars[0][0][0]):
                                blocks.add((num, cars[0][0][1]))
                        elif cars[0][0][0] > y:
                            for num in range(cars[0][0][0], 6):
                                blocks.add((num, cars[0][0][1]))
                if cars[0][1][1] == x:
                        blocks.add((cars[0][1][0], cars[0][1][1]))
                        if cars[0][1][0] < y:
                            for num in range(0, cars[0][1][0]):
                                blocks.add((num, cars[0][1][1]))
                        elif cars[0][1][0] > y:
                            for num in range(cars[0][1][0], 6):
                                blocks.add((num, cars[0][1][1]))
                if len(cars[0])==3:
                    if cars[0][2][1]==x:
                        blocks.add((cars[0][2][0], cars[0][2][1]))
                        if cars[0][2][0] < y:
                            for num in range(0, cars[0][2][0]):
                                blocks.add((num, cars[0][2][1]))
                        elif cars[0][2][0] > y:
                            for num in range(cars[0][2][0], 6):
                                blocks.add((num, cars[0][2][1]))

    return blocks

'''def moves3(state, target,blocked):
    moves = []
    if target[-1]=='s':
        for 
        for x in range(0,)'''
def blocked3(state,target):
    blocked = []
    for cars in state:
        for coor in cars[0]:
            blocked.append(coor)
    return blocked

def BFS(startstate):
    next = collections.deque([[startstate]])
    visited = {tuple(startstate)}
    start = time.process_time()
    while len(next) != 0:
        v = next.popleft()
        count =0
        if (goal_check(v[-1])):
            end = time.process_time()
            for states in v:
                print_puzzle(states)
                print()
            print(len(v)-1)
            print(len(visited))
            return True, visited, len(v[0]), end - start
        for child in get_children(v[-1]):
            count+=1
            if not tuple(child[-1]) in visited:
                visited.add(tuple(child))
                next.append(v+[child])
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    print(len(visited))
    return False, visited, 0, end - start

states = state_maker(states)
print(states)
print_puzzle(states)
print()
print(goal_check(states))
print()
print(blocked2(states, states[0]))
print()
print(moves2(states, states[0]))
print()
print(len(get_children(states)))
print()
'''for x in get_children(states):
    print_puzzle(x)
    print()'''
BFS(states)
