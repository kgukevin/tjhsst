import sys
import time
import random
from heapq import heappop, heappush

sys.setrecursionlimit(50000)


def initial_state(n):
    state = []
    for x in range(0, n):
        state.append(-1)
    return state


def goal_test(state):
    for x in state:
        if x == -1:
            return False
    return True


def get_next_unassigned_var(state):
    for x in range(0, len(state)):
        if state[x] == -1:
            return x
    return None


def get_most_constrained_var(state):
    open = len(state)
    index = get_next_unassigned_var(state)
    for x in range(0, len(state)):
        if state[x] == -1:
            vals = get_sorted_values(state, x)
            if open > len(vals):
                open = len(vals)
                index = x
    return index

def get_most_constraining_spot(state):
    '''invalid = []
    for y in range(0, len(state)):
        for x in range(0, len(state)):
            if state[x] == -1:
                for z in range(0, len(state)):
                    heappush(invalid,(z, state[x]))
                for z in range(0, len(state)):
                    heappush(invalid,(x, z))
                target = state[x]
                if target + (y - x) < 8:
                    heappush(invalid,(y, target + (y - x)))
                if target - (y - x) >= 0:
                    heappush(invalid,(y, target - (y - x)))
    return invalid[-1]'''
    invalid = set()
    for row in range(0, len(state)):
        if state[row]!=-1:
            for col in range(0, len(state)):
                invalid.add((row, col))
                invalid.add((col, state[row]+col))
                invalid.add((col, state[row]-col))
        #if state[row == -1]:







def get_random_var(state):
    reachable = []
    for x in range(0, len(state)):
        if state[x] == -1:
            reachable.append(x)
    if len(reachable) == 0:
        return None
    else:
        temp = reachable[random.randint(0, len(reachable) - 1)]
        return temp


# '''
def get_sorted_values(state, var):
    values = {num for num in range(0, len(state))}
    for x in range(0, len(state)):
        if state[x] != -1:
            if state[x] in values:
                values.remove(state[x])
            target = state[x]
            if target + (var - x) in values:
                values.remove(target + (var - x))
            if target - (var - x) in values:
                values.remove(target - (var - x))
    return values


'''
def get_sorted_values(state, var):
    values = []
    invalid = set()
    for x in range(0, len(state)):
        if state[x] != -1:
            invalid.add(state[x])
            target = state[x]
            invalid.add(target+(var-x))
            invalid.add(target-(var-x))

    for x in range(0, len(state)):
        if x not in invalid:
            values.append(x)
    return values
'''


# def check_code(state):
def csp(state):
    if goal_test(state): return state
    var = get_most_constrained_var(state)
    for val in get_sorted_values(state, var):
        # create new_state by assigning val to var
        new_state = state.copy()
        new_state[var] = val
        result = csp(new_state)
        if result is not None:
            return result
    return None


def csp2(state):
    if goal_test(state): return state
    var = get_most_constrained_var(state)
    posvals = list(get_sorted_values(state, var))
    if len(posvals) > 2:
        # reversed(posvals)
        random.shuffle(posvals)
    for val in posvals:
        # create new_state by assigning val to var
        new_state = state.copy()
        new_state[var] = val
        result = csp2(new_state)
        if result is not None:
            return result
    return None


# QS3 attempts
def compute_collisions(state):
    invalid = set()
    collisions = 0
    '''for vars, vals in enumerate(state):
        if vals == val:
            collisions+=1
        if vals == val - (var-vars):
            collisions+=1
        if vals == val + (var-vars):
            collisions+=1'''
    for y in range(0, len(state)):
        for x in range(0, len(state)):
            if state[x] != -1:
                for z in range(0, len(state)):
                    invalid.add((z, state[x]))
                for z in range(0, len(state)):
                    invalid.add((x, z))
                target = state[x]
                if target + (y - x) < 8:
                    invalid.add((y, target + (y - x)))
                if target - (y - x) >= 0:
                    invalid.add((y, target - (y - x)))
    for row, col in enumerate(state):
        if (row, col) in invalid:
            collisions += 1
    return collisions


def compute_collisions2(state):
    invalid = set()
    collisions = 0
    for row in range(0, len(state)):
        if state[row] != -1:
            for col in range(0, len(state)):
                invalid.add((row, col))
                invalid.add((col,state[row]))
                invalid.add((col, state[row] + (state[row]-col)))
                invalid.add((col, state[row] - (state[row]-col)))
                invalid.add(((col), state[row] + (state[row] - col)))
                invalid.add(((col), state[row] - (state[row] - col)))
    for row, col in enumerate(state):
        if (row, col) in invalid:
            collisions += 1
    return collisions


def reduce_collisions(state):
    row = random.randint(0, len(state) - 1)
    col = state[row]
    collis = len(state) + 10
    final = []
    states = []
    for x in range(0, len(state)):
        n = state.copy()
        n[x] = col
        temprow = state[x]
        n[row] = temprow
        states.append(n)
    for x in states:
        temp = compute_collisions(x)
        if temp < collis:
            collis = temp
            final = x
    return final


'''def get_freeorder_state(state):
    var = get_most_constrained_var(state)
    freeorder = []
    for val in get_sorted_values(state, var):
        # create new_state by assigning val to var
        new_state = state.copy()
        new_state[var] = val
        colis = compute_collisions(new_state)
        heappush(freeorder,(colis,new_state))
    return freeorder'''


def cspQS4(state, count, left):
    if goal_test(state): return state
    var = get_next_unassigned_var(state)
    if count == len(state) / 2:
        for val in get_sorted_values(state, var):
            # create new_state by assigning val to var
            new_state = state.copy()
            new_state[var] = val
            left.remove(val)
            result = cspQS4(new_state, count + 1, left)
            if result is not None:
                # reduce_collisions(result)
                return result
    else:
        val = left[random.randint(0, len(left) - 1)]
        new_state = state.copy()
        new_state[var] = val
        left.remove(val)
        result = cspQS4(new_state, count + 1, left)
        if result is not None:
            # reduce_collisions(result)
            return result
    return None


def test_code():
    #print(csp(initial_state(int(sys.argv[1]))))
    solve_time = 0
    size = 8
    while solve_time < 2:
        start = time.perf_counter()
        # state = cspQS4(initial_state(size),0,[x for x in range(0, size)])
        state = csp2(initial_state(size))
        #state = csp(initial_state(size))
        end = time.perf_counter()
        print(state)
        size += 1
        solve_time = end - start
        print("For size %s, the time was %s." % (size - 1, solve_time))


test_code()
#print(get_most_constraining_spot([-1,-1,-1,-1,-1,-1,-1,-1]))
#print(compute_collisions2([-1,1,3,3,4,7,-1,-1]))