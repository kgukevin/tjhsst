import sys
idx = int(sys.argv[1])-1
myRegexList = [
    r"/(\b\w*\b)(?=\W*said)/im",
    r"/.*\b(\w+)\b.*\b\1\b/is",
    r"/^(?=(.*a){4})(?=(.*b){3})(?!(.*a){5,})(?!(.*b){4,})[abc]*$/im",
    r"/^\w*(?=([^aeiou])(?!\1)([^aeiou])(?!\1|\2)[^aeiou])\w*$/im",
    r"/^(x|y)([abcd])(?!\2)[abcd]\1$/im"
]
print(myRegexList[idx])
