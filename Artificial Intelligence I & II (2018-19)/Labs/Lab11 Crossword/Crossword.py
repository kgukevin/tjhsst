import random
import re
import sys
import time
import collections
sys.setrecursionlimit(50000)
# # --> block;  "-" --> space;  xxx --> letter

### instantiations ###
blockcount = 0
# command = " ".join(sys.argv[0:])
command = "Cword.py 4x4 0 twentyk.txt"
#command = "Cword.py 5x5 0 twentyk.txt"
#command = "Cword.py 5x5 4 twentyk.txt v4x4D"
#command = "Cword.py 5x5 4 twentyk.txt v2x3T"
#command = "Cword.py 4x5 0 twentyk.txt"
#command = "Cword.py 11x9 30 wordlist.txt V0x1How"
#command = "Cword.py 15x15 39 wordlist.txt H0x0Mute V0x0mule V10x13Sunny H7x5# V3x4# H6x7# V11x3#"
#command = "Cword.py 10x13 32 scrabble.txt V6x0# V9x3# H3x9# V0x7SUBSTITUTE"
#command = "Cword.py 11x13 27 scrabble.txt H0x0begin V8x12end"
parts = command.split(" ")
sizes = parts[1].split("x")
height = int(sizes[0])
width = int(sizes[1])
size = height*width
prepuzzle = "-"*size
blocks = int(parts[2])
dictionary = parts[3]
immutable = set()
prepuzzle = list(prepuzzle)
if (size % 2 != 0) & (blocks % 2 != 0):
    prepuzzle[int(size / 2)] = '#'
    blockcount+=1
if len(parts)>4:
    for x in range(4,len(parts)):
        inputs = re.split(r"(\d+)",parts[x],re.I)
        #print(inputs)
        row = int(inputs[1])
        col = int(inputs[3])
        word = inputs[4].upper()
        if inputs[0].upper() == "H":
            for x in range(len(word)):
                prepuzzle[row*width+col+x]=word[x]
                immutable.add(row*width+col+x)
                if word[x]=="#":
                    prepuzzle[size - (row * width + col + x) - 1] = "#"
                else:
                    if prepuzzle[size-(row*width+col+x)-1]=="-":

                        prepuzzle[size-(row*width+col+x)-1]="?"
        if inputs[0].upper() == "V":
            for x in range(len(word)):
                prepuzzle[row*width+col+x*width]=word[x]
                immutable.add(row*width+col+x*width)
                if word[x]=="#":
                    prepuzzle[size - (row * width + col + x * width) - 1] = "#"
                else:
                    if prepuzzle[size-(row*width+col+x*width)-1]=="-":
                        prepuzzle[size-(row*width+col+x*width)-1] ="?"

prepuzzle = "".join(prepuzzle)

dictionarywords = ""
file = open(dictionary)
words = file.readlines()
for word in words:
    word = word.rstrip()
    if word.isalpha():
        dictionarywords+=word+" "

eng_freq = {"A":.0817, "B":.0149, "C":.0278, "D":.0425, "E":.1270, "F":.0223, "G":.0202, "H":.0609, "I":.0697, "J":.0015, "K":.0077, "L":.0403, "M":.0241,
            "N":.0675, "O":.0751,
            "P":.0193, "Q":.0010, "R":.0599, "S":.0633, "T":.0906, "U":.0276, "V":.0098, "W":.0236, "X":.0015, "Y":.0197, "Z":.0007}

def divide_dict(filename):
    file = open(filename)
    words = file.readlines()
    lengthdict = {}
    start = time.process_time()
    for word in words:
        word = word.rstrip()
        if word.isalpha():
            if len(word) in lengthdict.keys():
                lengthdict[len(word)].append(word.upper())
            else:
                lengthdict[len(word)]=[word.upper()]
    return lengthdict
lengths = divide_dict(dictionary)

def display_board(board):
    for x in range(height):
        if x == 0:
            numers = " " + "  ".join(str(x) for x in range(x * width, x * width + width))
        else:
            numers = " ".join(str(x) for x in range(x * width, x * width + width))
        board = "".join(board)
        # temp = board[x*height:x*height+width].replace("."," ")
        print("  ".join(board[x * width:x * width + width]))# + "   " + numers)

### blocking ###
def blocking(board):
    def get_children(board):
        global blockcount
        childs = set()
        board = list(board)
        visit = []
        for x in range(int(size/2)):
            if board[x]=="-":
                visit.append(x)
        while len(visit)!=0:
            temp = board.copy()
            rand = random.choice(visit)
            visit.remove(rand)
            temp[rand]=temp[size-rand-1]="#"
            childs.add("".join(temp))
        return childs

    def blockit(board):
        global blockcount
        next = collections.deque([board])
        visited = {board}
        while len(next) != 0:
            v = next.pop()
            #display_board(v)
            if v.count("#")==blocks:
                return v
            for child in get_children(v):
                if not child in visited:
                    visited.add(child)
                    if valid_blocking(child):
                        next.append(child)
        return None

    def valid_blocking(board):
        if board.count("#")==size:
            return True
        for x in range(size):
            rowindex = "".join([board[r] for r in range(int(x / width) * width, int(x / width) * width + width)])
            colindex = "".join([board[c] for c in range(int(x % width), size, width)])
            rowchar = rowindex.split("#")
            colchar = colindex.split("#")
            for m in rowchar:
                if 0<len(m)<3:
                    return False
            for l in colchar:
                if 0<len(l)<3:
                    return False
        if maxAreaOfIsland(board,board.index("-"))<(size-blocks):
            return False
        return True

    def make_valid(board):
        board = list(board)
        while valid_blocking(board) == False:
            for x in range(int(size/2)):
                if board[x]=="#":
                    if (x+3<int(x/width+1)*width and board[x+3]==("#")) or ((x+3>=int(x/width+1)*width) and (x+2<int(x/width+1)*width)):
                        board[x+2]=board[size-(x+2)-1]=board[x+1]=board[size-(x+1)-1]="#"
                    elif (x+2<int(x/width+1)*width and board[x+2]=="#") or ((x+2>=int(x/width+1)*width) and (x+1<int(x/width+1)*width)):
                        board[x+1]=board[size-(x+1)-1]="#"
                    if (int(x/width)*width<=x-3 and board[x-3]=="#") or ((x-3<int(x/width)*width) and (x-2>=int(x/width)*width)):
                        board[x-2]=board[size-(x-2)-1]=board[x-1]=board[size-(x-1)-1]="#"
                    elif (int(x/width)*width<=x-2 and board[x-2]=="#") or ((x-2<int(x/width)*width) and (x-1>=int(x/width)*width)):
                        board[x-1]=board[size-(x-1)-1]="#"
                    if (x+width*3<size and board[x+width*3]=="#") or (x+width*3>=size and x+width*2<size):
                        board[x+width*2]=board[size-(x+width*2)-1]=board[x+width]=board[size-(x+width)-1]="#"
                    elif (x+width*2<size and board[x+width*2]=="#") or (x+width*2>=size and x+width<size):
                        board[x+width]=board[size-(x+width)-1]="#"
                    if (0<=x-width*3 and board[x-width*3]=="#") or (0>x-width*3 and 0<=x-width*2):
                        board[x-width*2]=board[size-(x-width*2)-1]=board[x-width]=board[size-(x-width)-1]="#"
                    elif (0<=x-width*2 and board[x-width*2]=="#") or (0>x-width*2 and 0<=x-width):
                        board[x-width]=board[size-(x-width)-1]="#"
        for x in range(int(size/2)):
            if x+1<int(x/width+1)*width and board[x+1]=="-" and maxAreaOfIsland(board,x+1)<size-blocks:
                board=fillAreaOfIsland(board,x+1)[1]
            if x-1>int(x/width)*width and board[x-1]=="-" and maxAreaOfIsland(board,x-1)<size-blocks:
                board=fillAreaOfIsland(board,x-1)[1]
        return "".join(board)

    def maxAreaOfIsland(board,index):
        seen = set()
        def area(x):
            if not ((0 <= x < size) and (x not in seen) and (board[x]!="#")):
                return 0
            seen.add(x)
            if not (int(x / width) * width <= (x + 1) < int(x / width + 1) * width):
                return 1 + area(x - width) + area(x + width) + area(x - 1)
            elif not (int(x / width) * width <= (x - 1) < int(x / width + 1) * width):
                return 1 + area(x - width) + area(x + width) + area(x + 1)
            else:
                return 1 + area(x - width) + area(x + width) + area(x - 1) + area(x + 1)
        return area(index)

    def fillAreaOfIsland(board,index):
        seen = set()
        def area(x):
            if not ((0 <= x < size) and (x not in seen) and (board[x]=="-")):
                return 0
            seen.add(x)
            if not (int(x / width) * width <= (x + 1) < int(x / width + 1) * width):
                board[x]=board[size-x-1]="#"
                return 1 + area(x - width) + area(x + width) + area(x - 1)
            elif not (int(x / width) * width <= (x - 1) < int(x / width + 1) * width):
                board[x] = board[size-x-1]="#"
                return 1 + area(x - width) + area(x + width) + area(x + 1)
            else:
                board[x] = board[size-x-1]="#"
                return 1 + area(x - width) + area(x + width) + area(x - 1) + area(x + 1)
        return area(index),board


    if blocks == size:
        return "#"*size

    board = list(board)
    if valid_blocking(board) == False:
        board = make_valid(board)
    board = "".join(board)

    x = blockit(board).replace("?","-")
    return x


### filling ###
def add_word(newword,board):
    board = list(board)
    inputs = re.split(r"(\d+)", newword, re.I)
    #print(inputs)
    row = int(inputs[1])
    col = int(inputs[3])
    word = inputs[4].upper()
    if inputs[0] == "H":
        for x in range(len(word)):
            board[row * width + col + x] = word[x]
    if inputs[0] == "V":
        for x in range(len(word)):
            board[row * width + col + x * width] = word[x]
    board = "".join(board)
    return board

g=""
def fill_words(board):
    #usedword = set()
    vert = []
    hori = []
    for x in range(height):
        rowindex = "".join([board[r] for r in range(x * width, x * width + width)])
        hori.append(rowindex)
    print(hori)
    for x in range(width):
        colindex = "".join([board[c] for c in range(x, size, width)])
        vert.append(colindex)
    print(vert)

    def find_words():
        wordsindex = []
        for x in range(len(hori)):
            temp = ["H"]
            for y in range(len(hori[x])):
                if hori[x][y]!="#":
                    temp.append(int(width*x+y))
                    if (y+1<len(hori[x]) and hori[x][y+1]=="#") or y+1==len(hori[x]):
                        wordsindex.append(temp)
                        temp = ["H"]
        for x in range(len(vert)):
            temp = ["V"]
            for y in range(len(vert[x])):
                if vert[x][y]!="#":
                    temp.append(int(y*width +x))
                    if (y+1<len(vert[x]) and vert[x][y+1]=="#") or y+1==len(vert[x]):
                        wordsindex.append(temp)
                        temp = ["V"]
        return wordsindex

    def get_children(board):
        childs = []
        '''for x in edges.keys():
            for y in edges[x]:
                string = ""
                for z in y[1:]:
                    if board[z] == "-":
                        string += '[a-zA-z]'
                    else:
                        string += board[z]
                string = "\\b" + string + "\\b"
                results = [r[0] for r in re.finditer(string, dictionarywords, re.I)]
                if len(results)>0:
                    for l in results:
                        added = y[0] + str(int(y[1] / width)) + "x" + str(y[1] % width) + l
                        #temp = board.copy()
                        temp = add_word(added, board)
                        childs.add(temp)
                        #display_board(temp)'''

        board = list(board)
        eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        eng_freq = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0403, .0241,
                    .0675, .0751,
                    .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]
        frequency = ""
        for f in range(len(eng)):
            frequency+=eng[f]*int(eng_freq[f]*10000)
        for x in range(len(board)):
            if board.count("-")+board.count("#")!=size:
                if board[x]!=("-") and board[x]!="#":
                    if x+width<size and board[x+width]=="-":
                        temp = board.copy()
                        temp[x + width] = random.choice(frequency)
                        temp2 = "".join(temp)
                        childs.append(temp2)
                    if ((x + 1) < int(x / width + 1) * width) and board[x+1]=="-":
                        temp = board.copy()
                        temp[x + 1] = random.choice(frequency)
                        temp2 = "".join(temp)
                        childs.append(temp2)
            else:
                temp = board.copy()
                temp[x] = random.choice(frequency)
                temp2 = "".join(temp)
                childs.append(temp2)
        return childs

    global g
    g = find_words()

    def DFS(board):
        next = collections.deque([board])
        visited = {board}
        while len(next) != 0:
            v = next.pop()
            display_board(v)
            #display_board(v)
            if board.count("-")==0 and check_valid(v):
                return v
            for child in get_children(v):
                if not child in visited:
                    visited.add(child)
                    if check_valid(child)==True:
                        next.append(child)
        return None
    '''indexes = find_words()
    random.shuffle(indexes)
    for words in indexes:
        string = ""
        for x in words[1:]:
            if board[x]=="-":
                string+='[a-zA-z]'
            else:
                string+=board[x]
        string = "\\b"+string+"\\b"
        print(string)
        results = [r[0] for r in re.finditer(string,dictionarywords,re.I)]
        #print(results)
        #for r in re.finditer(string,dictionarywords,re.I|re.M):
            #print(r[0])
        #found = re.search(string,dictionarywords,re.I)
        #print(found)
        #print(words[0])
        row = int(words[1]/width)
        #col =
        #print(int(board[1]/width))
        added = words[0]+str(int(words[1]/width))+"x"+str(words[1]%width)+results[random.randint(0,len(results))]
        print(added)
        board = add_word(added,board)
        display_board(board)
        indexes.remove(words)'''

    used = set()
    def check_valid(board):
        words = set()
        for y in g:
            #print(y)
            word = ""
            string = ""
            for z in y[1:]:
                word+=board[z]
                if board[z] == "-":
                    string += '[a-zA-z]'
                else:
                    string += board[z]
            if word in words:
                return False
            elif "-" not in word:
                words.add(word)
            string = "\\b" + string + "\\b"
            results = re.search(string, " ".join(lengths[len(y)-1]), re.I)
            if results == None:
                return y
        '''for x in words:
            if "-" in x:
                continue
            if x in used:
                return False'''
        return True
    def get_next_set(state):
        global g
        random.shuffle(g)
        if state.count("-")!=0:
            for x in g:
                for z in x[1:]:
                    if state[z]=="-":
                        return x
        else:
            return check_valid(state)
    def get_sorted_values(state,var):
        string = ""
        for x in var[1:]:
            if state[x] == "-":
                string += '[A-Z]'
            else:
                string += state[x].upper()
        string = "\\b" + string + "\\b"
            #print(string)
        results = [r.group(0) for r in re.finditer(string, " ".join(lengths[len(var)-1]), re.I)]
        weight = dict()
        for r in results:
            #if r not in usedwords:
            score = 0
            for z in r:
                score+=eng_freq[z.upper()]*12
            weight[r]=score
                #print(added)
                #state = add_word(added, state)
        return sorted(weight,key = weight.__getitem__,reverse = True)
    def csp(state):
        if state.count("-")==0: return state
        #display_board(state)
        print(state)
        print()
        var = get_next_set(state)
        for val in get_sorted_values(state, var):
            # create new_state by assigning val to var
            #if val in used:
                #continue
            #used.add(val)
            new_state = state
            added = var[0] + str(int(var[1] / width)) + "x" + str(var[1] % width) + val
            new_state = add_word(added,new_state)
            #display_board(new_state)
            if check_valid(new_state)==True:
                #result = csp(new_state)
                result = csp(new_state)
                if result is not None:
                    return result
                #used.remove(val)
        '''global puzzle
        global g
        if state == puzzle:
            state = blocking(prepuzzle)
            g = find_words()
            return csp(state)'''
        '''
        backtrack = []
        wrong = check_valid(state)
        for x in g:
            for y in x[1:]:
                if y in wrong and y not in immutable:
                    backtrack.append(x)
        #print(backtrack)
        new_state = state
        var = random.choice(backtrack)
        new_state = add_word(var[0] + str(int(var[1] / width)) + "x" + str(var[1] % width) + "-"*(len(var)-1), new_state)
        result = csp(new_state)
        if result is not None:
            return result'''
        return None

    import time
    start = time.perf_counter()
    #display_board(csp(board))
    print(csp(board))
    end = time.perf_counter()
    print("secs: "+str(end-start))


#def fill_words(board):


# def check_valid():
#add_word("H0x0begin")
#print(fill_words(puzzle))

display_board(prepuzzle)
print()
#print(divide_dict("scrabble.txt"))
#add_blocking()
#print(valid_blocking(puzzle))
puzzle = blocking(prepuzzle)
display_board(puzzle)
fill_words(puzzle)


#print(valid_blocking(".XXXXX.XXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXX.XXXXX."))
#print(get_children("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"))
'''print()
test = "XXX.XXXXXXXXXXXXXXXXX...XXXXXXX.XXXXXXX...XXXXXXXXXXXXXXXXX.XXX"
display_board(test)
print(maxAreaOfIsland(test))'''