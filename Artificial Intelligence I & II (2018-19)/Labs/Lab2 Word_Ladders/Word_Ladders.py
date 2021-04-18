import pickle
import time
import collections
data = [1,2,3,'a','b','c']
with open("my_data.pkl", "wb") as outfile:
    pickle.dump(data, outfile)

with open("my_data.pkl", "rb") as infile:
    data = pickle.load(infile)


    buckets = {}
    graph = {}
def graph_maker(filename):

    file = open(filename)
    words = file.readlines()

    start = time.process_time()
    for word in words:
        word = word.rstrip()
        temp = list(word)
        graph[word]=set()
        for x in range(len(word)):
            temp[x]="_"
            key = "".join(temp)
            if key not in buckets.keys():
                buckets[key] = [word]
            else:
                buckets[key].append(word)
            temp = list(word)

    '''print(buckets)'''

    for bucket in buckets.keys():
        for x in buckets[bucket]:
            for y in buckets[bucket]:
                graph[x].add(y)
    for key in graph.keys():
        if key in graph[key]:
            graph[key].remove(key)
    end = time.process_time()

    '''print()
    print(graph)
    print(len(graph))'''
    print("time taken to create graphs: %s" % (end - start))
    print()
    return graph

def goal_test(start, stop):
    return start[-1]==stop
def get_children(state):
    children = []
    previous = state
    temp = state[-1]
    for word in graph[temp]:
        temp2 = previous + [word]
        children.append(temp2)
    return children
def BFS(begin, goal, graph):
    next = collections.deque([[begin]])
    visited = {begin}
    start = time.process_time()
    while len(next) != 0:
        v = next.popleft()
        if(goal_test(v,goal)):
            end = time.process_time()
            print(v)
            print("path length: " + str(len(v)-1) + ". seconds to run: %s" % (end - start) + ".")
            return True, visited, len(v)-1, end - start
        for child in get_children(v):
            if not child[-1] in visited:
                visited.add(child[-1])
                next.append(child)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start
def BFS_maxpath(graph):
    maxlength = 0
    maxpath = []
    start = time.process_time()
    for words in graph.keys():
        next = collections.deque([[words]])
        visited = {words}
        while len(next) != 0:
            v = next.popleft()
            for child in get_children(v):
                if not child[-1] in visited:
                    visited.add(child[-1])
                    next.append(child)
            pathlength = len(v)
        if pathlength > maxlength:
            maxlength = pathlength
            maxpath = v
    end = time.process_time()
    print(maxpath)
    print("path length: " + str(maxlength - 1) + ". seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start
def BFS_maxpath2(graph):
    for words in graph.keys():
        next = collections.deque([words])
        visited = {words}
        while len(next) != 0:
            v = next.popleft()
            for child in graph[v]:
                if not child in visited:
                    visited.add(child)
                    next.append(child)
    return False, visited, 0
def BFS_parity(graph):
    connected = []
    start = time.process_time()
    count = 0
    graphs = 0
    for words in graph.keys():
        next = collections.deque([words])
        visited = {words}
        while len(next) != 0:
            v = next.popleft()
            for child in graph[v]:
                if not child in visited:
                    visited.add(child)
                    next.append(child)
        connected.append(set(visited))
    components = set()
    for x in range(len(connected)):
        connected[x] = frozenset(connected[x])
        components.add(connected[x])
    end = time.process_time()
    print("path length: " + str(len(components)) + ". seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start
file2 = open("puzzles.txt")
lists = file2.readlines()
graph = graph_maker("words_6.txt")
for line in lists:
    line = line.rstrip()
    words = line.split(" ")
    BFS(words[0], words[1], graph)
    print()
#BFS("crafty", "dimmed", graph)
#BFS_maxpath(graph)
BFS_parity(graph)
