import sys, re, os
usage = "Usage: rex.py fileName.txt /regexPattern/options"

try:
  import colorama
  colorama.init()
except Exception as exc:
  pass

# Parse input arguments
if len(sys.argv) < 3: exit(usage)
if not os.path.isfile(sys.argv[1]): exit("'{}' was not found.\n  {}".format(sys.argv[1], usage))
regex = sys.argv[2].strip()
match = re.search(r"^/(.*)/([ismISM]*)$", regex)
if not match: exit("'{}' does not appear to be a proper regular expression\n  {}".format(regex, usage))

# Read in the file to be searched
lines = open(sys.argv[1],'r').read().splitlines()
text  = "\n".join(lines)      # neutralizes platform dependent newline issues

# Parse the search spec (ie. the regular expression)
options = {"s":re.S, "i":re.I, "m":re.M}
opt = sum(options[ltr] for ltr in {*match.group(2).lower()})
pattern = match.group(1)
try:
  if opt: rec = re.compile(pattern, opt)
  else:   rec = re.compile(pattern)
except Exception as exc:
  exit("'{}' is not a valid RegEx\n  {}".format(pattern, usage))

# Apply the regular expression
startEndLst = [(m.start(), m.end()) for m in rec.finditer(text)]
if not startEndLst: exit("No matches found")

# Make a lookup dictionary to identify idx to word number
basePos, idxToLine = 0, {0: 0}
for lineNum, line in enumerate(lines):
  idxToLine[basePos] = lineNum
  basePos += 1 + len(line) 

def idxToWordAndPos(idx, idxToLine):
  # identify the line (or word) number given an index position into the text
  for x in range(idx,-1,-1):
    if x in idxToLine:
      return (idxToLine[x], idx-x)
  exit("Got an error in idxToWordAndPos with idx {}".format(idx))

# Translate index positions to (word number, offset) tuple
sePairs = [(idxToWordAndPos(p[0], idxToLine), idxToWordAndPos(p[1], idxToLine)) for p in startEndLst]   # start end pairs

escapes = ["\033[37m", "\033[31m"]
def determinePrintLine(word, intervals):
  # assemble word so that at each interval, the font color (eventually: background) swaps
  intervals.append(len(word))
  output = ""
  for idxNum, endPos in enumerate(intervals[1:]):
    if endPos > intervals[idxNum]:
      output += escapes[idxNum&1] + word[intervals[idxNum]:endPos]
  return output

# Then identify each word
wordDct = {}
for p0, p1 in sePairs:
  w0,o0 = p0; w1, o1 = p1     # start word, offset into start word; end word, offset into end word
  if w0 not in wordDct: wordDct[w0] = []
  wordDct[w0].append(o0)
  for wordNum in range(w0, w1):
    wordDct[wordNum].append(len(lines[wordNum])+1)
    if wordNum+1 not in wordDct: wordDct[wordNum+1] = []
    wordDct[wordNum+1].append(0)
  wordDct[w1].append(o1)

# Now output them in a color coded fashion
for wordNum in wordDct:
  output = determinePrintLine(lines[wordNum]+ " ", [0] + wordDct[wordNum])
  print(output)

print ("\n{} matches in {} lines".format(len(startEndLst), len(wordDct)))

# References
# https://stackoverflow.com/questions/48445616/why-printing-in-color-in-a-windows-terminal-in-python-does-not-work
# https://stackoverflow.com/questions/12492810/python-how-can-i-make-the-ansi-escape-codes-to-work-also-in-windows
# https://pypi.org/project/colorama/