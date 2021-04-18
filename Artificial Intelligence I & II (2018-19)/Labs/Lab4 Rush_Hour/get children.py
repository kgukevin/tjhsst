def children(state):
    c = []
    for i in range(len(state)):
        car = state[i]
        if car[1]=='h':
            row = rowChildren(len(car[0]),car[0][0][0],car)
            for s in row:
                copy = state[:i]+tuple([s]) +state[i+1:]
                add = True
                hmmm = s[0]

                if hmmm[0][1]>car[0][0][1]:
                    for z in range(car[0][0][1]+len(car[0]),hmmm[0][1]):
                        hmmm = hmmm+tuple([(car[0][0][0],z)])
                else:
                    for z in range(hmmm[0][1]+len(car[0]),car[0][0][1]):
                        hmmm = hmmm+tuple([(car[0][0][0],z)])

                for vertices in hmmm:
                    for cars in state:
                        if cars !=car and vertices in cars[0]:
                            add = False
                if add:
                    c.append(copy)

        if car[1]=='v':
            column = columnChildren(len(car[0]), car[0][0][1], car)
            for s in column:
                copy = state[:i] + tuple([s]) + state[(i + 1):]
                add = True
                hmmm =s[0]

                if hmmm[0][0]>car[0][0][0]:
                    for z in range(car[0][0][0]+len(car[0]),hmmm[0][0]):
                        hmmm = hmmm+tuple([(z,car[0][0][1])])
                else:
                    for x in range(hmmm[0][0]+len(car[0]),car[0][0][0]):
                        hmmm = hmmm+tuple([(x,car[0][0][1])])

                for vertices in hmmm:
                    for cars in state:
                        if cars !=car and vertices in cars[0]:
                            add = False
                if add:
                    c.append(copy)
    return c
def columnChildren(size,column,car):

    list = []
    for i in range(7 - size):
        if size == 2:
            x = (((i, column), (i+1, column)), 'v')
        else:
            x =(((i, column), (i+1, column), (i+2, column)), 'v')
        if x != car:
            list.append(x)
    return list

def rowChildren(size,row,car):
    list =[]
    for i in range(7-size):
        if size == 2:
            x =(((row,i),(row,i+1)),'h')
        else:
            x = (((row,i),(row,i+1),(row,i+2)),'h')
        if x !=car:
            list.append(x)
    return list