'''import sys

sum = int(sys.argv[1])+int(sys.argv[2])
print(sum)

for index in range(1,len(sys.argv)):
    sum += int(sys.argv[index])
print(sum)
print("\"Dont't quote me,\" she said")
'''

s = input("Enter input")
print(s[1])
print(s[4])
print(len(s))
print(s[0])
print(s[len(s)-1])
print(s[len(s)-2])
print(s[:5]) #till index 5
print(s[3:]) #index 3 till
print(s[3:5]) #index 3 till index 5
#negative index numbers denote index away from end
print(s[:-4]) #till 4 away from last
print(s[-4:]) #4 away from last till
print(s[::2]) #every other letter
print(s[2::3]) #every third letter from second
print(s[::-1]) #every previous letter
print(s.index(" "))
print(s.lower())
print(s.split(" "))
print(len(s.split(" ")))
print(list(s)) #list of all letters in string
listout = []
for string in list(s):
    listout.append(ord(string))
listout.sort()
for int in range(0,len(listout)):
    listout[int]=chr(listout[int])
print("".join(listout))
if(s==s[::-1]):
    print("true")
else:
    print("false")

print(s.replace(s[0],"")) #replace same letters
print("'")
