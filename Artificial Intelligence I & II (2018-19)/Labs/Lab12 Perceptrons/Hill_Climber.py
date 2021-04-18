import random

def percep_step( w, b, x):

    def activation(num):
        if num > 0:
            return 1
        return 0

    temp = sum(p*q for p,q in zip(w,x))+b
    return activation(temp)

def percep_sigmoid( w, b, x, k):

    def activation(num,k):
        return 1/(1+2.7128**(-k*num))

    z = sum(p*q for p,q in zip(w,x))+b
    return activation(z,k)

def circle_NN(xcoor,ycoor,v):
    one = percep_sigmoid((v[0], v[1]), v[2], (xcoor, ycoor), v[17])
    two = percep_sigmoid((v[3], v[4]), v[5], (xcoor, ycoor), v[17])
    three = percep_sigmoid((v[6], v[7]), v[8], (xcoor, ycoor), v[17])
    four = percep_sigmoid((v[9], v[10]), v[11], (xcoor, ycoor), v[17])
    last = percep_sigmoid((v[12], v[13], v[14], v[15]), v[16], (one, two, three, four), v[17])
    if last > v[18]:
        return 1
    return 0

def calc_error(NN, X, weights):
    sum = 0
    for test in X:
        if test[-1]==True:
            temp = 1
        else:
            temp = 0
        sum += (temp - NN(test[0][0],test[0][1],weights))**2
    return sum

def making_progress():
    return True

def hillclimb(NN, X, epsilon):
    w = [-1,0,-1,0,-1,-1,1,0,-1,0,1,-1,-1,-1,-1,-1,.5,3,.62769999]
    #w = [random.uniform(-1, 1) for x in range(19)]
    while calc_error(NN,X,w)>=3504:
        w = [random.uniform(-1,1) for x in range(19)]
    oe = calc_error(NN, X, w)
    print(oe)
    while(oe>epsilon):
        #w = [random.uniform(-1,1) for x in range(19)]
        while(making_progress()):
            delta_w = [.005*random.uniform(-1,1) for x in range(19)]
            w2 = [p+q for p,q in zip(w,delta_w)]
            e = calc_error(NN, X, w)
            e1 = calc_error(NN, X, w2)
            print("errors: " + str(e) + " " + str(e1))
            if e > e1:
                w = w2
            if calc_error(NN, X, w)<=epsilon:
                return w
    return w

training_set = []
with open("10000_pairs.txt", "r") as f:
    for line in f:
        xs, ys = line.split()
        x, y = float(xs), float(ys)
        answer = True if x**2 + y**2 <= 1 else False
        training_set.append(tuple(((x, y), answer)))
training_set = tuple(training_set)

weigh = hillclimb(circle_NN, training_set, 0)


tally = 0
for x_vec, output in training_set:
    xcoor = x_vec[0]
    ycoor = x_vec[1]
    one = percep_sigmoid((weigh[0], weigh[1]), weigh[2], (xcoor, ycoor), weigh[17])
    two = percep_sigmoid((weigh[3], weigh[4]), weigh[5], (xcoor, ycoor), weigh[17])
    three = percep_sigmoid((weigh[6], weigh[7]), weigh[8], (xcoor, ycoor), weigh[17])
    four = percep_sigmoid((weigh[9], weigh[10]), weigh[11], (xcoor, ycoor), weigh[17])
    trained_out = percep_sigmoid((weigh[12], weigh[13], weigh[14], weigh[15]), weigh[16], (one, two, three, four), weigh[17]) # Change this to match your code; True means inside and False means outside!
    if trained_out >= weigh[18]:
        tally+=1


print("My code got this many correct out of 10,000: %s" % tally)

