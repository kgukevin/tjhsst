import numpy as np

# x = np.matrix([[1, 2],
#                [3, 4]])
# y = np.matrix([[2, 3],
#                [4, 5]])
#
# print(x + y)
# print(x * y)
# print(np.multiply(x, y))
# print(x.transpose())
# print(x[0, 1])
# print(y[1, 1])
#
# def ex_f(x):
#     return x**2 + 1
#
# vec_f = np.vectorize(ex_f)
#
# print(vec_f(x))
#
# print(np.linalg.norm(np.matrix([[1, -1]])))
# print(np.linalg.norm(np.matrix([[-3, 4]])))
#


def sig_f(x):
    return 1/(1+np.exp(-x))
def sig_fp(x):
    return np.exp(-x)/((1+np.exp(-x))**2)
def step_f(x):
    if x > 0:
        return 1
    return 0

vect_sig = np.vectorize(sig_f)
vect_sigp = np.vectorize(sig_fp)
vect_step = np.vectorize(step_f)



w0 = np.matrix([[2, -2],[1, -3]])
b1 = np.matrix([[-1, 4]])
w1 = np.matrix([[-1, -2],[2, 3]])
b2 = np.matrix([[1, -2]])
x = np.matrix([[.7, 1]])
y = np.matrix([[0, .9]])

a1 = vect_sig(x*w0+b1)
#print(a1)
a2 = vect_sig(a1*w1+b2)
#print(a2)
err = .5*(np.linalg.norm(y-a2))**2
#print(err)


a0 = x
a1 = vect_sig(a0*w0+b1)
a2 = vect_sig(a1*w1+b2)
delta2 = np.multiply(vect_sigp(a1*w1+b2), (y-a2))
#print(delta2)
delta1 = np.multiply(vect_sigp(a0*w0+b1), (delta2*w1.transpose()))
#print(delta1)

b1 = b1 + .25*delta1
w0 = w0 + .25*a0.transpose()*delta1
b2 = b2 + .25*delta2
w1 = w1 + .25*a1.transpose()*delta2
# print(w0)
# print()
# print(b1)
# print()
# print(w1)
# print()
# print(b2)
# print()
a1 = vect_sig(a0*w0+b1)
print(a1)
a2 = vect_sig(a1*w1+b2)
print(a2)

err = .5*(np.linalg.norm(y-a2))**2
print(err)



def XOR(matrx):
    #percep_step((percep_step((x1, x2), -0.5, (1, 1)), percep_step((x1, x2), 2.5, (-1, -2))), -2.5, (1, 2))
    w0 = np.matrix([[1, -1],
                    [1, -2]])
    b1 = np.matrix([[-.5, 2.5]])
    w1 = np.matrix([[1],
                    [2]])
    b2 = np.matrix([[-2.5]])

    a0 = matrx
    a1 = vect_step(a0*w0+b1)
    a2 = vect_step(a1*w1+b2)
    return a2

# x = np.matrix([0, 0])
# print(str(x)+" --> "+str(XOR(x)))
# x = np.matrix([0, 1])
# print(str(x)+" --> "+str(XOR(x)))
# x = np.matrix([1, 0])
# print(str(x)+" --> "+str(XOR(x)))
# x = np.matrix([1, 1])
# print(str(x)+" --> "+str(XOR(x)))

set_three = [((0,0),(0,0)),((1,0),(0,1)),((0,1),(0,1)),((1,1),(1,0))]

def calc_error(w0,b1,w1,b2,training_set):
    err = 0
    for coor in training_set:
        a0 = np.matrix([coor[0][0], coor[0][1]])
        y = np.matrix([coor[1][0],coor[1][1]])
        a1 = vect_sig(a0 * w0 + b1)
        a2 = vect_sig(a1 * w1 + b2)
        err += .5*(np.linalg.norm(y-a2))**2
    return err/4


def backprop(training_set):
    w0 = np.random.rand(2, 2)
    b1 = np.random.rand(1, 2)
    w1 = np.random.rand(2, 2)
    b2 = np.random.rand(1, 2)
    while calc_error(w0,b1,w1,b2,training_set)>0.0008:
        # w0 = np.random.rand(2, 2)
        # b1 = np.random.rand(1, 2)
        # w1 = np.random.rand(2, 2)
        # b2 = np.random.rand(1, 2)
        for x in range(10):
            print(calc_error(w0,b1,w1,b2,training_set))
            for coor in training_set:
                a0 = np.matrix([coor[0][0],coor[0][1]])
                y = np.matrix([coor[1][0],coor[1][1]])
                a1 = vect_sig(a0*w0+b1)
                a2 = vect_sig(a1*w1+b2)
                delta2 = np.multiply(vect_sigp(a1*w1+b2), y-a2)
                delta1 = np.multiply(vect_sigp(a0*w0+b1), delta2*w1.transpose())
                w0 = w0 + .1*a0.transpose()*delta1
                b1 = b1 + .1*delta1
                w1 = w1 + .1*a1.transpose()*delta2
                b2 = b2 + .1*delta2
    return w0,w1,b1,b2

# w0,w1,b1,b2 = backprop(set_three)
# a0=np.matrix([0,0])
# a1 = vect_sig(a0*w0+b1)
# a2 = vect_sig(a1*w1+b2)
# if a2[0,0]>=.5:
#     a2[0,0]=1
# else:
#     a2[0,0]=0
# if a2[0,1]>=.5:
#     a2[0,1]=1
# else:
#     a2[0,1]=0
# print(a2)
# a0=np.matrix([0,1])
# a1 = vect_sig(a0*w0+b1)
# a2 = vect_sig(a1*w1+b2)
# if a2[0,0]>=.5:
#     a2[0,0]=1
# else:
#     a2[0,0]=0
# if a2[0,1]>=.5:
#     a2[0,1]=1
# else:
#     a2[0,1]=0
# print(a2)
# a0=np.matrix([1,0])
# a1 = vect_sig(a0*w0+b1)
# a2 = vect_sig(a1*w1+b2)
# if a2[0,0]>=.5:
#     a2[0,0]=1
# else:
#     a2[0,0]=0
# if a2[0,1]>=.5:
#     a2[0,1]=1
# else:
#     a2[0,1]=0
# print(a2)
# a0=np.matrix([1,1])
# a1 = vect_sig(a0*w0+b1)
# a2 = vect_sig(a1*w1+b2)
# if a2[0,0]>=.5:
#     a2[0,0]=1
# else:
#     a2[0,0]=0
# if a2[0,1]>=.5:
#     a2[0,1]=1
# else:
#     a2[0,1]=0
# print(a2)

training_set = []
# with open("10000_pairs.txt", "r") as f:
#     for line in f:
#         xs, ys = line.split()
#         x, y = float(xs), float(ys)
#         answer = 1 if x**2 + y**2 <= 1 else 0
#         training_set.append(tuple(((x, y), answer)))
# training_set = tuple(training_set)

def calc_error_cir(w0,b1,w1,b2,training_set):
    err = 0
    tally = 0
    for coor in training_set:
        a0 = np.matrix([coor[0][0], coor[0][1]])
        y = np.matrix([coor[1]])
        a1 = vect_sig(a0 * w0 + b1)
        a2 = vect_sig(a1 * w1 + b2)
        if a2[0, 0] >= .5:
            a2[0, 0] = 1
        else:
            a2[0, 0] = 0
        if a2[0, 0] == y[0, 0]:
            tally += 1
        err += (np.linalg.norm(y-a2))**2
    return err/len(training_set), len(training_set)-tally

def backprop_cir(training_set):
    w0 = np.random.rand(2, 8)
    b1 = np.random.rand(1, 8)
    w1 = np.random.rand(8, 1)
    b2 = np.random.rand(1, 1)
    while calc_error_cir(w0,b1,w1,b2,training_set)[0]>.005:
        for x in range(100000):
            errors = calc_error_cir(w0,b1,w1,b2,training_set)
            print(errors[0])
            if errors[0]<=.005:
                return w0,w1,b1,b2
            for coor in training_set:
                a0 = np.matrix([coor[0][0],coor[0][1]])
                y = np.matrix([coor[1]])
                a1 = vect_sig(a0*w0+b1)
                a2 = vect_sig(a1*w1+b2)
                delta2 = np.multiply(vect_sigp(a1*w1+b2), y-a2)
                delta1 = np.multiply(vect_sigp(a0*w0+b1), delta2*w1.transpose())
                w0 = w0 + 2.2*(1/(x+1))*a0.transpose()*delta1
                b1 = b1 + 2.2*(1/(x+1))*delta1
                w1 = w1 + 2.2*(1/(x+1))*a1.transpose()*delta2
                b2 = b2 + 2.2*(1/(x+1))*delta2
    return w0,w1,b1,b2
# w0,w1,b1,b2 = backprop_cir(training_set)
# print(w0)
# print(b1)
# print(w1)
# print(b2)
#
# tally = 0
# for coor in training_set:
#     a0 = np.matrix([coor[0][0], coor[0][1]])
#     y = np.matrix([coor[1]])
#     a1 = vect_sig(a0 * w0 + b1)
#     a2 = vect_sig(a1 * w1 + b2)
#     if a2[0,0]>=.5:
#         a2[0,0]=1
#     else:
#         a2[0,0]=0
#     if a2[0,0]==y[0,0]:
#         tally+=1
# print(tally)