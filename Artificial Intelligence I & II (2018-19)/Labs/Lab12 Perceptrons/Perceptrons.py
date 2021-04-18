
def percep_step( w, b, x):

    def activation(num):
        if num > 0:
            return 1
        return 0

    temp = sum(p*q for p,q in zip(w,x))+b
    return activation(temp)

import itertools
def truth_table(bits, n):
    numoutputs = 2**bits
    output=("{0:0" + str(numoutputs) + "b}").format(n)
    #print(output)
    table = list(itertools.product([0, 1], repeat=bits))
    table.reverse()
    for x in range(len(table)):
        table[x] = (table[x],int(output[x]))
    #print(table)
    return table

def pretty_print_tt(table):
    print("   IN   |  OUT  ")
    print("----------------")
    for values in table:
        print(" "+str(values[0])+" |  "+str(values[1])+"  ")

def check(n, w, b):
    ttable = truth_table(len(w), n)
    #pretty_print_tt(ttable)
    correct = 0
    for x in range(len(ttable)):
        #print(percep_step(w, b, ttable[x][0]))
        #print(ttable[x][1])
        if (percep_step(w, b, ttable[x][0]))==(ttable[x][1]):
            correct+=1
    return correct/len(ttable)
count = 0
def train(bits, n):
    global count
    w = tuple([0 for p in range(bits)])
    b = 0.5
    ttable = truth_table(len(w),n)
    pretty_print_tt(ttable)
    for epoch in range(100):
        for xvalue in ttable:
            ystar = percep_step(w, b, xvalue[0])
            err = xvalue[1]-ystar
            w = tuple([(w[x]+err*xvalue[0][x]) for x in range(len(xvalue[0]))])
            #print(w)
            b +=err*1
        if check(n, w, b)==1:
            count+=1
            print("epoch: "+str(epoch))
            print(str(w) + " " + str(b))
            return n, w, b
    return n, w, b
#pretty_print_tt(truth_table(2,8))
#print(train(2, 8))

def test_all(n):
    for test in range(2**(2**n)):
        x = train(n,test)
        print(check(x[0],x[1],x[2]))
        print(count)

def graph_twobit(n):
    import time
    import matplotlib.pyplot as plt
    import numpy as np
    start = time.perf_counter()
    #test_all(4)
    plt.axis((-2,2,-2,2))
    #plt.xticks(np.arange(-2, 2, step=0.1))
    #plt.yticks(np.arange(-2, 2, step=0.1))
    plt.ylabel('some numbers')
    for x in range(-20,21):
        for y in range(-20,21):
            xcoor = x/10
            ycoor = y/10
            plt.plot(xcoor,ycoor,"r.")
            t = train(2,n)
            if percep_step(t[1], t[2], (xcoor,ycoor))==1:
                plt.plot(xcoor,ycoor, "b.")
    plt.plot(0,0,"bo")
    plt.plot(0,1,"bo")
    plt.plot(1,0,"bo")
    plt.plot(1,1,"bo")
    plt.show()
    end = time.perf_counter()

def two_bit_XOR(x1,x2):
    return percep_step((percep_step((x1,x2), -0.5, (1,1)), percep_step((x1,x2), 2.5, (-1,-2))), -2.5, (1,2))

def percep_sigmoid( w, b, x):

    def activation(num,k):
        return 1/(1+2.7128**(-k*num))

    z = sum(p*q for p,q in zip(w,x))+b
    return activation(z,3)

def circle():
    import time
    import matplotlib.pyplot as plt
    import numpy as np
    start = time.perf_counter()
    # test_all(4)
    plt.axis((-2, 2, -2, 2))
    plt.gca().set_aspect("equal",adjustable = "box")
    # plt.xticks(np.arange(-2, 2, step=0.1))
    # plt.yticks(np.arange(-2, 2, step=0.1))
    plt.ylabel('some numbers')
    bias = -1
    dbx = []
    dby = []
    dgx = []
    dgy = []
    lgx = []
    lgy = []
    lbx = []
    lby = []
    for x in range(-400, 400):
        for y in range(-400, 400):
            xcoor = x / 200
            ycoor = y / 200
            #plt.plot(xcoor, ycoor, "r.")
            dbx.append(xcoor)
            dby.append(ycoor)
            one = percep_sigmoid((-1,0),bias,(xcoor,ycoor))
            two = percep_sigmoid((0,-1),bias,(xcoor,ycoor))
            three = percep_sigmoid((1, 0), bias, (xcoor, ycoor))
            four = percep_sigmoid((0,1), bias, (xcoor, ycoor))
            last = percep_sigmoid((-1,-1,-1,-1),.5,(one,two,three,four))
            #if (one or two or three or four) == 1:
            #if one == 1:
            if last >= .42769999:
                #plt.plot(xcoor,ycoor,"b.")
                dgx.append(xcoor)
                dgy.append(ycoor)
                if xcoor**2+ycoor**2>1:
                    lgx.append(xcoor)
                    lgy.append(ycoor)
            if xcoor ** 2 + ycoor ** 2 < 1:
                lbx.append(xcoor)
                lby.append(ycoor)
    plt.plot(dbx, dby, ".", color="darkblue")
    plt.plot(lbx, lby, ".", color="lightgreen")
    plt.plot(dgx,dgy,".",color = "darkgreen")
    plt.plot(lgx,lgy,".",color = "lightblue")

    #         plt.plot(xcoor, ycoor, "r.")
    #         if percep_sigmoid((1,0), .5, (xcoor, ycoor)) >= bound\
    #                 and percep_sigmoid((-1,0),.5,(xcoor,ycoor))>=bound\
    #                 and percep_sigmoid((0,1),.5,(xcoor,ycoor))>=bound\
    #                 and percep_sigmoid((0,-1),.5,(xcoor,ycoor))>=bound:
    #             plt.plot(xcoor, ycoor, "b.")
    plt.show()
    end = time.perf_counter()

training_set = []
with open("10000_pairs.txt", "r") as f:
    for line in f:
        xs, ys = line.split()
        x, y = float(xs), float(ys)
        answer = True if x**2 + y**2 <= 1 else False
        training_set.append(tuple(((x, y), answer)))
training_set = tuple(training_set)

tally = 0
for x_vec, output in training_set:
    xcoor = x_vec[0]/200
    ycoor = x_vec[1]/200
    bias = -1
    one = percep_sigmoid((-1, 0), bias, (xcoor, ycoor))
    two = percep_sigmoid((0, -1), bias, (xcoor, ycoor))
    three = percep_sigmoid((1, 0), bias, (xcoor, ycoor))
    four = percep_sigmoid((0, 1), bias, (xcoor, ycoor))
    trained_out = percep_sigmoid((-1, -1, -1, -1), .5, (one, two, three, four)) # Change this to match your code; True means inside and False means outside!
    if trained_out >= .42769999:
        tally += 1

print("My code got this many correct out of 10,000: %s" % tally)
circle()

#print(two_bit_XOR(0,1))


# graph_twobit(14)
# print(two_bit_XOR(1,1))
# print(two_bit_XOR(0,1))
# print(two_bit_XOR(1,0))
# print(two_bit_XOR(0,0))
#test_all(2)


# from keras.models import Sequential
# from keras.layers import Dense
# import numpy as np
#
# X = [np.array((x,y)) for x in range(-400,400) for y in range(-400,400)]
# print(X)
# Y = [np.array([(1-x[0]**2)**(1/2)]) for x in X]
# X = np.array(X)
# Y= np.array(Y)
# # create model
# sklearn.test_train_split
# model = Sequential()
# model.add(Dense(4, activation='sigmoid'))
# model.add(Dense(1, activation='sigmoid'))
#
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(X, Y, epochs=150, batch_size=10)
# scores = model.evaluate(X, Y)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
