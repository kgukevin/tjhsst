import time
import sys
from heapq import heappop, heappush
#
# Torbert, 22 Sept 2014
# White (ed), 5 Oct 2016
#
from math import pi, acos, sin, cos


#
def calcd(y1, x1, y2, x2):
    #
    # y1 = lat1, x1 = long1
    # y2 = lat2, x2 = long2
    # all assumed to be in decimal degrees

    # if (and only if) the input is strings
    # use the following conversions

    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)
    #
    r = 3958.76  # miles = 6371 km
    #
    y1 *= pi / 180.0
    x1 *= pi / 180.0
    y2 *= pi / 180.0
    x2 *= pi / 180.0
    #
    # approximate great circle distance with law of cosines
    #
    return acos(sin(y1) * sin(y2) + cos(y1) * cos(y2) * cos(x2 - x1)) * r
    #


#
# end of file
#

def make_graph():
    file = open("rrNodes.txt")
    temp = file.readlines()
    nodes = {}
    for iden in range(len(temp)):
        new = temp[iden].split(" ")
        nodes[new[0].rstrip()] = (new[1].rstrip(), new[2].rstrip())

    file = open("rrEdges.txt")
    temp = file.readlines()
    edges = {}
    for iden in range(len(temp)):
        new = temp[iden].split(" ")
        y1 = nodes[new[0].rstrip()][0]
        x1 = nodes[new[0].rstrip()][1]
        y2 = nodes[new[1].rstrip()][0]
        x2 = nodes[new[1].rstrip()][1]
        dist = calcd(y1, x1, y2, x2)
        if new[0].rstrip() not in edges.keys():
            edges[new[0].rstrip()] = {(new[1].rstrip(), (y1, x1, y2, x2), dist)}
        else:
            edges[new[0].rstrip()].add((new[1].rstrip(), (y1, x1, y2, x2), dist))
        if new[1].rstrip() not in edges.keys():
            edges[new[1].rstrip()] = {(new[0].rstrip(), (y2, x2, y1, x1), dist)}
        else:
            edges[new[1].rstrip()].add((new[0].rstrip(), (y2, x2, y1, x1), dist))

    file = open("rrNodeCity.txt")
    temp = file.readlines()
    citie = {}
    for iden in range(len(temp)):
        new = temp[iden].split(" ")
        if len(new) == 2:
            citie[new[1].rstrip()] = new[0].rstrip()
        elif len(new) == 3:
            citie[new[1].rstrip() + " " + new[2].rstrip()] = new[0].rstrip()
    return edges, citie, nodes


maps, cities, node = make_graph()  # map is iden:(next node, coordinates,distance)


def goal_test(city, goal):
    if city == goal:
        return True
    return False


def get_childrendij(city):
    children = []
    for nodes in maps[city]:
        children.append((nodes[-1], nodes[1], nodes[0]))
    return children


def dijkstra(start, end):
    startcityiden = cities[start]
    endcityiden = cities[end]
    fringe = [(0, startcityiden)]  # BFS algorithm from class of a list of states
    visited = set()
    start = time.process_time()
    while len(fringe) != 0:
        v = heappop(fringe)
        if v[-1] in visited:
            continue
        visited.add(v[-1])
        if goal_test(v[-1], endcityiden):
            end = time.process_time()
            print("Dijkstra path length: " + str(v[0]) + ". seconds to run: %s" % (end - start) + ".")
            return True, visited, len(v[1]), end - start
        for child in get_childrendij(v[-1]):
            if not child[-1] in visited:
                heappush(fringe, (child[0] + v[0], child[-1]))
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start


def astar(start, end):
    startcityiden = cities[start]
    endcityiden = cities[end]
    fringe = [(0, 0, startcityiden)]  # BFS algorithm from class of a list of states
    visited = set()
    start = time.process_time()
    while len(fringe) != 0:
        v = heappop(fringe)
        if v[-1] in visited:
            continue
        visited.add(v[-1])
        if goal_test(v[-1], endcityiden):
            end = time.process_time()
            print("A* path length: " + str(v[1]) + ". seconds to run: %s" % (end - start) + ".")
            return True, visited, end - start
        for child in get_childrendij(v[-1]):
            if not child[-1] in visited:
                heuris = calcd(child[1][2], child[1][3], node[endcityiden][0], node[endcityiden][1])
                heappush(fringe, (child[0] + v[1] + heuris, v[1] + child[0], child[-1]))
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start


'''startcity = sys.argv[1]
endcity = sys.argv[-1]
dijkstra(startcity,endcity)
astar(startcity,endcity)'''
'''
astar("Washington DC","Charlotte")
dijkstra("Leon","Leon")
dijkstra("Albuquerque", "Atlanta")
dijkstra("Leon", "Tucson")
dijkstra("Ciudad Juarez", "Montreal")
astar("Albuquerque", "Atlanta")
astar("Ciudad Juarez", "Montreal")
dijkstra("Chicago", "Washington DC")
'''

import tkinter
from tkinter import ttk, Canvas, Scale, HORIZONTAL, LEFT, RIGHT, SUNKEN, Frame, TOP, BOTTOM

xancor = 1400
yancor = 670
xfactor = 10
yfactor = 10


def dijkstramap(start, end):
    startcityiden = cities[start]
    endcityiden = cities[end]
    fringe = [(0, [startcityiden], startcityiden)]  # BFS algorithm from class of a list of states
    visited = set()
    screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                       yancor - yfactor * float(node[startcityiden][0]) - 3,
                       xancor + xfactor * float(node[startcityiden][1]) + 3,
                       yancor - yfactor * float(node[startcityiden][0]) + 3,
                       fill="green")
    screen.create_oval(xancor + xfactor * float(node[endcityiden][1]) - 3,
                       yancor - yfactor * float(node[endcityiden][0]) - 3,
                       xancor + xfactor * float(node[endcityiden][1]) + 3,
                       yancor - yfactor * float(node[endcityiden][0]) + 3,
                       fill="green")
    screen.update()
    start = time.process_time()
    count = 0
    while len(fringe) != 0:
        count += 1
        v = heappop(fringe)
        if len(v[-2]) > 2:
            screen.create_line(xancor + xfactor * float(node[v[-2][-1]][1]),
                               yancor - yfactor * float(node[v[-2][-1]][0]),
                               xancor + xfactor * float(node[v[-2][-2]][1]),
                               yancor - yfactor * float(node[v[-2][-2]][0]),
                               fill="deep sky blue")
        if v[-1] in visited:
            continue
        visited.add(v[-1])
        if goal_test(v[-1], endcityiden):
            end = time.process_time()
            # print("path length: " + str(v[0]) + ". seconds to run: %s" % (end - start) + ".")
            screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                               yancor - yfactor * float(node[startcityiden][0]) - 3,
                               xancor + xfactor * float(node[startcityiden][1]) + 3,
                               yancor - yfactor * float(node[startcityiden][0]) + 3,
                               fill="green")
            screen.create_oval(xancor + xfactor * float(node[endcityiden][1]) - 3,
                               yancor - yfactor * float(node[endcityiden][0]) - 3,
                               xancor + xfactor * float(node[endcityiden][1]) + 3,
                               yancor - yfactor * float(node[endcityiden][0]) + 3,
                               fill="green")
            lbl2.configure(text="Progress: COMPLETE")
            lbl3.configure(text="Distance: " + str(v[0]) + " miles")
            screen.update()
            for iden in range(0, len(v[-2]) - 1):
                screen.create_line(xancor + xfactor * float(node[v[-2][iden]][1]),
                                   yancor - yfactor * float(node[v[-2][iden]][0]),
                                   xancor + xfactor * float(node[v[-2][iden + 1]][1]),
                                   yancor - yfactor * float(node[v[-2][iden + 1]][0]), fill="yellow")
                time.sleep(.005)
                screen.update()
            return v[-2], True, visited, len(v[1]), end - start
        for child in get_childrendij(v[-1]):
            if not child[-1] in visited:
                heappush(fringe, (child[0] + v[0], v[-2] + [child[-1]], child[-1]))
                screen.create_line(xancor + xfactor * float(child[1][3]), yancor - yfactor * float(child[1][2]),
                                   xancor + xfactor * float(child[1][1]), yancor - yfactor * float(child[1][0]),
                                   fill="magenta")
                if len(fringe) == 7:
                    screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                                       yancor - yfactor * float(node[startcityiden][0]) - 3,
                                       xancor + xfactor * float(node[startcityiden][1]) + 3,
                                       yancor - yfactor * float(node[startcityiden][0]) + 3, fill="green")
                if count % slider.get() == 0:
                    screen.update()
                # time.sleep(0.0000000001)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start


def astarmap(start, end):
    startcityiden = cities[start]
    endcityiden = cities[end]
    fringe = [(0, 0, [startcityiden], startcityiden)]  # BFS algorithm from class of a list of states
    visited = set()
    screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                       yancor - yfactor * float(node[startcityiden][0]) - 3,
                       xancor + xfactor * float(node[startcityiden][1]) + 3,
                       yancor - yfactor * float(node[startcityiden][0]) + 3,
                       fill="green")
    screen.create_oval(xancor + xfactor * float(node[endcityiden][1]) - 3,
                       yancor - yfactor * float(node[endcityiden][0]) - 3,
                       xancor + xfactor * float(node[endcityiden][1]) + 3,
                       yancor - yfactor * float(node[endcityiden][0]) + 3,
                       fill="green")
    screen.update()
    start = time.process_time()
    count = 0
    while len(fringe) != 0:
        count += 1
        v = heappop(fringe)
        if len(v[-2]) > 2:
            screen.create_line(xancor + xfactor * float(node[v[-2][-1]][1]),
                               yancor - yfactor * float(node[v[-2][-1]][0]),
                               xancor + xfactor * float(node[v[-2][-2]][1]),
                               yancor - yfactor * float(node[v[-2][-2]][0]),
                               fill="deep sky blue")
        if v[-1] in visited:
            continue
        visited.add(v[-1])
        if goal_test(v[-1], endcityiden):
            end = time.process_time()
            # print("path length: " + str(v[0]) + ". seconds to run: %s" % (end - start) + ".")
            screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                               yancor - yfactor * float(node[startcityiden][0]) - 3,
                               xancor + xfactor * float(node[startcityiden][1]) + 3,
                               yancor - yfactor * float(node[startcityiden][0]) + 3,
                               fill="green")
            screen.create_oval(xancor + xfactor * float(node[endcityiden][1]) - 3,
                               yancor - yfactor * float(node[endcityiden][0]) - 3,
                               xancor + xfactor * float(node[endcityiden][1]) + 3,
                               yancor - yfactor * float(node[endcityiden][0]) + 3,
                               fill="green")
            lbl2.configure(text="Progress: COMPLETE")
            lbl3.configure(text="Distance: " + str(v[1]) + " miles")
            screen.update()
            for iden in range(0, len(v[-2]) - 1):
                screen.create_line(xancor + xfactor * float(node[v[-2][iden]][1]),
                                   yancor - yfactor * float(node[v[-2][iden]][0]),
                                   xancor + xfactor * float(node[v[-2][iden + 1]][1]),
                                   yancor - yfactor * float(node[v[-2][iden + 1]][0]), fill="yellow")
                time.sleep(.005)
                screen.update()
            print(len(v[-2]))
            return v[-2], True, visited, end - start
        for child in get_childrendij(v[-1]):
            if not child[-1] in visited:
                heuris = calcd(child[1][2], child[1][3], node[endcityiden][0], node[endcityiden][1])
                heappush(fringe, (child[0] + v[1] + heuris, child[0] + v[1], v[-2] + [child[-1]], child[-1]))
                screen.create_line(xancor + xfactor * float(child[1][3]), yancor - yfactor * float(child[1][2]),
                                   xancor + xfactor * float(child[1][1]), yancor - yfactor * float(child[1][0]),
                                   fill="magenta")
                if len(fringe) == 10:
                    screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                                       yancor - yfactor * float(node[startcityiden][0]) - 3,
                                       xancor + xfactor * float(node[startcityiden][1]) + 3,
                                       yancor - yfactor * float(node[startcityiden][0]) + 3, fill="green")
                if count % slider.get() == 0:
                    screen.update()
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start


def astarmmap(start, end, m):
    startcityiden = cities[start]
    endcityiden = cities[end]
    fringe = [(0, 0, [startcityiden], startcityiden)]  # BFS algorithm from class of a list of states
    visited = set()
    screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                       yancor - yfactor * float(node[startcityiden][0]) - 3,
                       xancor + xfactor * float(node[startcityiden][1]) + 3,
                       yancor - yfactor * float(node[startcityiden][0]) + 3,
                       fill="green")
    screen.create_oval(xancor + xfactor * float(node[endcityiden][1]) - 3,
                       yancor - yfactor * float(node[endcityiden][0]) - 3,
                       xancor + xfactor * float(node[endcityiden][1]) + 3,
                       yancor - yfactor * float(node[endcityiden][0]) + 3,
                       fill="green")
    screen.update()
    start = time.process_time()
    count = 0
    while len(fringe) != 0:
        count += 1
        v = heappop(fringe)
        if len(v[-2]) > 2:
            screen.create_line(xancor + xfactor * float(node[v[-2][-1]][1]),
                               yancor - yfactor * float(node[v[-2][-1]][0]),
                               xancor + xfactor * float(node[v[-2][-2]][1]),
                               yancor - yfactor * float(node[v[-2][-2]][0]),
                               fill="deep sky blue")
        if v[-1] in visited:
            continue
        visited.add(v[-1])
        if goal_test(v[-1], endcityiden):
            end = time.process_time()
            # print("path length: " + str(v[0]) + ". seconds to run: %s" % (end - start) + ".")
            screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                               yancor - yfactor * float(node[startcityiden][0]) - 3,
                               xancor + xfactor * float(node[startcityiden][1]) + 3,
                               yancor - yfactor * float(node[startcityiden][0]) + 3,
                               fill="green")
            screen.create_oval(xancor + xfactor * float(node[endcityiden][1]) - 3,
                               yancor - yfactor * float(node[endcityiden][0]) - 3,
                               xancor + xfactor * float(node[endcityiden][1]) + 3,
                               yancor - yfactor * float(node[endcityiden][0]) + 3,
                               fill="green")
            lbl2.configure(text="Progress: COMPLETE")
            lbl3.configure(text="Distance: " + str(v[1]) + " miles")
            screen.update()
            for iden in range(0, len(v[-2]) - 1):
                screen.create_line(xancor + xfactor * float(node[v[-2][iden]][1]),
                                   yancor - yfactor * float(node[v[-2][iden]][0]),
                                   xancor + xfactor * float(node[v[-2][iden + 1]][1]),
                                   yancor - yfactor * float(node[v[-2][iden + 1]][0]), fill="yellow")
                time.sleep(.005)
                screen.update()
            print(len(v[-2]))
            return v[-2], True, visited, end - start
        for child in get_childrendij(v[-1]):
            if not child[-1] in visited:
                heuris = calcd(child[1][2], child[1][3], node[endcityiden][0], node[endcityiden][1])
                heappush(fringe, (m * (child[0] + v[1]) + heuris, child[0] + v[1], v[-2] + [child[-1]], child[-1]))
                screen.create_line(xancor + xfactor * float(child[1][3]), yancor - yfactor * float(child[1][2]),
                                   xancor + xfactor * float(child[1][1]), yancor - yfactor * float(child[1][0]),
                                   fill="magenta")
                if len(fringe) == 10:
                    screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                                       yancor - yfactor * float(node[startcityiden][0]) - 3,
                                       xancor + xfactor * float(node[startcityiden][1]) + 3,
                                       yancor - yfactor * float(node[startcityiden][0]) + 3, fill="green")
                if count % slider.get() == 0:
                    screen.update()
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start


def dfsmap(start, end):
    startcityiden = cities[start]
    endcityiden = cities[end]
    fringe = [(0, [startcityiden], startcityiden)]  # BFS algorithm from class of a list of states
    visited = set()
    screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                       yancor - yfactor * float(node[startcityiden][0]) - 3,
                       xancor + xfactor * float(node[startcityiden][1]) + 3,
                       yancor - yfactor * float(node[startcityiden][0]) + 3,
                       fill="green")
    screen.create_oval(xancor + xfactor * float(node[endcityiden][1]) - 3,
                       yancor - yfactor * float(node[endcityiden][0]) - 3,
                       xancor + xfactor * float(node[endcityiden][1]) + 3,
                       yancor - yfactor * float(node[endcityiden][0]) + 3,
                       fill="green")
    screen.update()
    start = time.process_time()
    count = 0
    while len(fringe) != 0:
        count += 1
        v = fringe.pop()
        if len(v[-2]) > 2:
            screen.create_line(xancor + xfactor * float(node[v[-2][-1]][1]),
                               yancor - yfactor * float(node[v[-2][-1]][0]),
                               xancor + xfactor * float(node[v[-2][-2]][1]),
                               yancor - yfactor * float(node[v[-2][-2]][0]),
                               fill="deep sky blue")
        if v[-1] in visited:
            continue
        visited.add(v[-1])
        if goal_test(v[-1], endcityiden):
            end = time.process_time()
            # print("path length: " + str(v[0]) + ". seconds to run: %s" % (end - start) + ".")
            screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                               yancor - yfactor * float(node[startcityiden][0]) - 3,
                               xancor + xfactor * float(node[startcityiden][1]) + 3,
                               yancor - yfactor * float(node[startcityiden][0]) + 3,
                               fill="green")
            screen.create_oval(xancor + xfactor * float(node[endcityiden][1]) - 3,
                               yancor - yfactor * float(node[endcityiden][0]) - 3,
                               xancor + xfactor * float(node[endcityiden][1]) + 3,
                               yancor - yfactor * float(node[endcityiden][0]) + 3,
                               fill="green")
            lbl2.configure(text="Progress: COMPLETE")
            lbl3.configure(text="Distance: " + str(v[0]) + " miles")
            screen.update()
            for iden in range(0, len(v[-2]) - 1):
                screen.create_line(xancor + xfactor * float(node[v[-2][iden]][1]),
                                   yancor - yfactor * float(node[v[-2][iden]][0]),
                                   xancor + xfactor * float(node[v[-2][iden + 1]][1]),
                                   yancor - yfactor * float(node[v[-2][iden + 1]][0]), fill="yellow")
                time.sleep(.005)
                screen.update()
            return v[-2], True, visited, len(v[1]), end - start
        for child in get_childrendij(v[-1]):
            if not child[-1] in visited:
                fringe.append((child[0] + v[0], v[-2] + [child[-1]], child[-1]))
                screen.create_line(xancor + xfactor * float(child[1][3]), yancor - yfactor * float(child[1][2]),
                                   xancor + xfactor * float(child[1][1]), yancor - yfactor * float(child[1][0]),
                                   fill="magenta")
                if len(fringe) == 7:
                    screen.create_oval(xancor + xfactor * float(node[startcityiden][1]) - 3,
                                       yancor - yfactor * float(node[startcityiden][0]) - 3,
                                       xancor + xfactor * float(node[startcityiden][1]) + 3,
                                       yancor - yfactor * float(node[startcityiden][0]) + 3, fill="green")
                if count % slider.get() == 0:
                    screen.update()
                # time.sleep(0.0000000001)
    end = time.process_time()
    print("No Solution." + " seconds to run: %s" % (end - start) + ".")
    return False, visited, 0, end - start


height = 610
width = 1250
window = tkinter.Tk()
window.title("Train Routes")
window.geometry(str(width) + "x" + str(height))
lbl = tkinter.Label(window, bg="black", text="Train Routes in North America", height=2, width=width, fg="white")
lbl.pack()

box = Frame(window)
box.pack(side=RIGHT)
# lbl4 = tkinter.Label(box, bg="black", text="Stops along the way: ", height=15, width=50, fg="white")
# lbl4.pack(side=BOTTOM)
button4 = ttk.Button(box, text="RESET", width=58)


def callback4():
    screen.delete("all")
    for iden in maps.keys():
        for edges in maps[iden]:
            screen.create_line(xancor + xfactor * float(edges[1][1]), yancor - yfactor * float(edges[1][0]),
                               xancor + xfactor * float(edges[1][3]), yancor - yfactor * float(edges[1][2]),
                               fill="white")
    lbl2.configure(text="Progress:             ")
    lbl3.configure(text="Distance:             ")


button4.configure(command=callback4)
button4.pack(side=BOTTOM)
lbl3 = tkinter.Label(box, bg="black", text="Distance:             ", height=10, width=50, fg="white")
lbl3.pack(side=BOTTOM)
lbl2 = tkinter.Label(box, bg="black", text="Progress:             ", height=10, width=50, fg="white")
lbl2.pack(side=BOTTOM)

box1 = Frame(box)
box1.pack(side=TOP)
labl = tkinter.Label(box1, bg="black", text="Select Cities:", height=2, width=50, fg="white")
labl.pack(side=TOP)
mb = ttk.Combobox(box1, text="Select Start City: ", width=25)
values = []
for iden in cities.keys():
    values.append(iden)
mb.config(values=tuple(values))
mb.pack(side=LEFT)

mb2 = ttk.Combobox(box1, text="Select End City: ", width=26)
mb2.config(values=tuple(values))
mb2.pack(side=RIGHT)
# labl = tkinter.Label(box1, bg="black", text="Select Cities", height=2, width=50, fg="white")
# labl.pack(side = TOP)
screen = Canvas(window, bg="black", height=height, width=width, relief=SUNKEN, borderwidth=10)
screen.pack(side=LEFT)
for iden in maps.keys():
    for edges in maps[iden]:
        screen.create_line(xancor + xfactor * float(edges[1][1]), yancor - yfactor * float(edges[1][0]),
                           xancor + xfactor * float(edges[1][3]), yancor - yfactor * float(edges[1][2]), fill="white")

box2 = Frame(box)
box2.pack(side=TOP)
button = ttk.Button(box2, text="dijkstra", width=8)


def callback():
    lbl2.configure(text="Progress: Searching...")
    lbl3.configure(text="Distance: Searching...")
    dijkstramap(mb.get(), mb2.get())


button.configure(command=callback)
button.pack(side=LEFT)
button2 = ttk.Button(box2, text="astar", width=8)


def callback2():
    lbl2.configure(text="Progress: Searching...")
    lbl3.configure(text="Distance: Searching...")
    astarmap(mb.get(), mb2.get())


button2.configure(command=callback2)
button2.pack(side=RIGHT)
button3 = ttk.Button(box2, text="astar*m", width=8)


def callback3():
    lbl2.configure(text="Progress: Searching...")
    lbl3.configure(text="Distance: Searching...")
    astarmmap(mb.get(), mb2.get(), 0.2)


button3.configure(command=callback3)
button3.pack(side=RIGHT)
button4 = ttk.Button(box2, text="dfs", width=8)


def callback4():
    lbl2.configure(text="Progress: Searching...")
    lbl3.configure(text="Distance: Searching...")
    dfsmap(mb.get(), mb2.get())


button4.configure(command=callback4)
button4.pack(side=RIGHT)

slider = Scale(box, from_=1, to=1000, length=300, orient=HORIZONTAL)
slider.pack(side=BOTTOM)

speedlabl = tkinter.Label(box, bg="black", text="Select Speed:", height=2, width=50, fg="white")
speedlabl.pack(side=BOTTOM)

window.mainloop()
