import math
def make_f(f, dir, loc):
    def funct(x):
        return f(loc[0]-x*dir[0], loc[1]-x*dir[1])
    return funct

def sinfunct(x):
    return math.sin(x)+math.sin(3*x)+math.sin(4*x)

def function1(x,y):
    return 4*x**2 - 3*x*y + 2*y**2 + 24*x - 20*y
def gradient1(x,y):
    return (8*x-3*y+24, -3*x+4*y-20)

def function2(x,y):
    return (1-y)**2 + 100*(x-y**2)**2
def gradient2(x,y):
    return (200*x-200*y**2, -2+2*y + 400*y**3 - 400*x*y)

def grad_desc_with_line_search(f,grad,start,range,tol):
    location = start
    while math.sqrt(grad(location[0],location[1])[0]**2+grad(location[0],location[1])[1]**2)>tol:
        dir = grad(location[0],location[1])
        one_var_f = make_f(f, dir, location)
        lmbd = one_d_minimize(one_var_f, range[0], range[1], tol)
        location = (location[0]-lmbd*dir[0], location[1]-lmbd*dir[1])
        print(location)
        print(f(location[0], location[1]))
    return location

def one_d_minimize(f, left, right, tol):
    if right - left < tol:
        return (right + left) / 2
    dist = (right - left) / 3
    leftbound = f(left + dist)
    rightbound = f(left + 2*dist)
    if leftbound > rightbound:
        return one_d_minimize(f, left+dist, right, tol)
    else:
        return one_d_minimize(f, left, left+2*dist, tol)
print(str(one_d_minimize(sinfunct,-1,0,10**(-8))) + " " + str(sinfunct(one_d_minimize(sinfunct,-1,0,10**(-8)))))

import time
start = time.perf_counter()
x = grad_desc_with_line_search(function2, gradient2, (0,0), (0,1), 10**-8)
print(function2(x[0],x[1]))
end = time.perf_counter()
print(end-start)




