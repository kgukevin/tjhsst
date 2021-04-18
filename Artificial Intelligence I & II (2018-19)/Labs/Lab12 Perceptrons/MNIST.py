import numpy as np
import csv
import time
import pickle
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

# trainset = []
# f = open("mnist_train.csv")
# readin = csv.reader(f)
# readin = list(readin)
# for x in range(60000):
#     y = [0,0,0,0,0,0,0,0,0,0]
#     y[int(readin[x][0])]=1
#     trainset.append((np.matrix([int(readin[x][z])/255 for z in range(1,len(readin[x]))]),np.matrix([z for z in y])))
# pickle.dump(trainset, open("mnist_training3.txt","wb"))

# testset = pickle.load(open("mnist_training1.txt","rb"))
# for x in testset:
#     print(x)


def calc_error_spec(training_set,shape,weights,bias):
    err = 0
    tally = 0
    for coor in training_set:
        y = coor[1]
        a_levels = dict()
        a_levels[0] = coor[0]
        for layers in range(1, len(shape)):
            a_levels[layers] = vect_sig(a_levels[layers - 1] * weights[layers - 1] + bias[layers])

        for x in range(len(a_levels[len(shape)-1])):
            if a_levels[len(shape)-1][0, x] >= .5:
                a_levels[len(shape)-1][0, x] = 1
            else:
                a_levels[len(shape)-1][0, x] = 0
            if a_levels[len(shape)-1][0,x]!=y[0,x]:
                tally += 1
                break
        err += (np.linalg.norm(y-a_levels[len(shape)-1]))**2
    return err/len(training_set), tally

def backpropspec(training_set,shape,lmda,errorbound):
    weights = dict()
    bias = dict()
    for layer in range(len(shape) - 1):
        weights[layer] = np.matrix(2 * np.random.rand(shape[layer], shape[layer + 1]) - 1)
        bias[layer + 1] = np.matrix(2 * np.random.rand(1, shape[layer + 1]) - 1)
    while calc_error_spec(training_set,shape,weights,bias)[1] > errorbound:
        print("start training")
        for x in range(100000):
            start = time.perf_counter()
            errors = calc_error_spec(training_set,shape,weights,bias)
            print("epoch: " + str(x) + "\t"+ "error: " + str(errors[1]))
            if errors[1] <= errorbound:
                end = time.perf_counter()
                print("time: " + str(end - start) + "\n")
                return weights, bias
            for coor in training_set:
                y = coor[1]
                a_levels = dict()
                a_levels[0] = coor[0]
                for layers in range(1, len(shape)):
                    a_levels[layers] = vect_sig(a_levels[layers - 1] * weights[layers - 1] + bias[layers])
                deltas = dict()
                deltas[len(shape) - 1] = np.multiply(
                    vect_sigp(a_levels[len(shape) - 2] * weights[len(shape) - 2] + bias[len(shape) - 1]),y - a_levels[len(shape) - 1])
                for layers in range(1, len(shape) - 1):
                    deltas[len(shape) - 1 - layers] = np.multiply(vect_sigp(a_levels[len(shape) - 1 - layers - 1] * weights[len(shape) - 1 - layers - 1] + bias[len(shape) - 1 - layers]), deltas[len(shape) - 1 - layers + 1] * weights[len(shape) - 1 - layers].transpose())
                for layers in range(0,len(shape)-2):
                    new_w = weights[layers]+lmda*a_levels[layers].transpose()*deltas[layers+1]
                    weights[layers]=new_w
                    new_b = bias[layers+1]+lmda*deltas[layers+1]
                    bias[layers+1]=new_b
            pickle.dump(weights, open("mnist_weights.txt", "wb"))
            pickle.dump(bias, open("mnist_bias.txt", "wb"))
            end = time.perf_counter()
            print("time: " + str(end - start) + "\n")
    return weights,bias

def backprop(training_set,weights,bias,shape,lmda,errorbound):
    # weights = dict()
    # bias = dict()
    # for layer in range(len(shape) - 1):
    #     weights[layer] = np.matrix(2 * np.random.rand(shape[layer], shape[layer + 1]) - 1)
    #     bias[layer + 1] = np.matrix(2 * np.random.rand(1, shape[layer + 1]) - 1)
    while calc_error_spec(training_set,shape,weights,bias)[1] > errorbound:
        print("start training")
        for x in range(100000):
            start = time.perf_counter()
            errors = calc_error_spec(training_set,shape,weights,bias)
            print("epoch: " + str(x) + "\t"+ "error: " + str(errors[1]))
            if errors[1] <= errorbound:
                end = time.perf_counter()
                print("time: " + str(end - start) + "\n")
                return weights, bias
            for coor in training_set:
                y = coor[1]
                a_levels = dict()
                a_levels[0] = coor[0]
                for layers in range(1, len(shape)):
                    a_levels[layers] = vect_sig(a_levels[layers - 1] * weights[layers - 1] + bias[layers])
                deltas = dict()
                deltas[len(shape) - 1] = np.multiply(
                    vect_sigp(a_levels[len(shape) - 2] * weights[len(shape) - 2] + bias[len(shape) - 1]),y - a_levels[len(shape) - 1])
                for layers in range(1, len(shape) - 1):
                    deltas[len(shape) - 1 - layers] = np.multiply(vect_sigp(a_levels[len(shape) - 1 - layers - 1] * weights[len(shape) - 1 - layers - 1] + bias[len(shape) - 1 - layers]), deltas[len(shape) - 1 - layers + 1] * weights[len(shape) - 1 - layers].transpose())
                for layers in range(0,len(shape)-2):
                    new_w = weights[layers]+lmda*a_levels[layers].transpose()*deltas[layers+1]
                    weights[layers]=new_w
                    new_b = bias[layers+1]+lmda*deltas[layers+1]
                    bias[layers+1]=new_b
            pickle.dump(weights, open("mnist_weights.txt", "wb"))
            pickle.dump(bias, open("mnist_bias.txt", "wb"))
            end = time.perf_counter()
            print("time: " + str(end - start) + "\n")
    return weights,bias

# trainset = pickle.load(open("mnist_training3.txt","rb"))
weights = pickle.load(open("mnist_weights.txt","rb"))
bias = pickle.load(open("mnist_bias.txt","rb"))
# backprop(trainset,weights,bias, [784,400,200,100,10], .1, 60000*.04)



# testset = []
# f = open("mnist_test.csv")
# readin = csv.reader(f)
# readin = list(readin)
# for x in range(10000):
#     y = [0,0,0,0,0,0,0,0,0,0]
#     y[int(readin[x][0])]=1
#     testset.append((np.matrix([int(readin[x][z])/255 for z in range(1,len(readin[x]))]),np.matrix([z for z in y])))
# pickle.dump(testset, open("mnist_test.txt","wb"))

testset = pickle.load(open("mnist_test.txt","rb"))

def output(training_set,shape,weights,bias):
    err = 0
    tally = 0
    for coor in training_set:
        y = coor[1]
        a_levels = dict()
        a_levels[0] = coor[0]
        for layers in range(1, len(shape)):
            a_levels[layers] = vect_sig(a_levels[layers - 1] * weights[layers - 1] + bias[layers])

        for x in range(len(a_levels[len(shape)-1])):
            if a_levels[len(shape)-1][0, x] >= .5:
                a_levels[len(shape)-1][0, x] = 1
            else:
                a_levels[len(shape)-1][0, x] = 0
            if a_levels[len(shape)-1][0,x]!=y[0,x]:
                tally += 1
                break
        err += (np.linalg.norm(y-a_levels[len(shape)-1]))**2
        print("error: "+ str(tally))
    return err/len(training_set), tally
output(testset, [784,400,200,100,10], weights, bias)