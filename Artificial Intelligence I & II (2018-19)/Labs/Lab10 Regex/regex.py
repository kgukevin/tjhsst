import sys
# part1
idx = int(sys.argv[1])-31
myRegexList = [
    "/^0$|^10[10]$/",
    "/^[01]*$/",
    "/0$/",
    "/\w*[aeiou]\w*[aeiou]\w*/i",
    "/^1[01]*0$|^0$/",
    "/^[01]*110[01]*$/",
    "/^.{2,4}$/si",
    "/^\d{3} *-? *\d\d *-? *\d{4}$/",
    "/^.*?d/mi",
    "/^0[01]*0$|^1[01]*1$|^[01]$/",
    ""]
print(myRegexList[idx])

# part2
import sys
idx = int(sys.argv[1])-41
myRegexList = [
    "/^[ox.]{64}$/i",
    "/^[ox]*\.[ox]*$/i",
    "/^x+o*\.|^\.|\.o*x+$|\.$/i",
    "/^(..)*.$/s",
    "/^(0|1[01])([01]{2})*$/",
    "/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
    "/^(0|10)*1*$/",
    "/^([bc]+a?|a)[bc]*$/",
    "/^(b|c|(a[bc]*){2})+$/",
    "/^(20*|1[02]*10*|0$)+$/",
    ""]
print(myRegexList[idx])

# part3
import sys
idx = int(sys.argv[1])-51
myRegexList = [
    r"/(\w)*\w*\1\w*/i",
    r"/(\w)*(\w*\1){3}\w*/i",
    r"/^(0|1)([01]*\1|)$/",
    r"/\b(?=\w*cat)\w{6}\b/i",
    r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i",
    r"/\b((?!cat)\w){6}\b/i",
    r"/\b((\w)(?!\w*\2))+\b/i",
    r"/^((?!10011)[01])*$/",
    r"/\w*(?=([aeiou])+)(?!\1)\w*/i",
    r"/^((?!1[01]1)[01])*$/",
    ""]
print(myRegexList[idx])

# part5
import sys
idx = int(sys.argv[1])-71
myRegexList = [
    r"/^(?=(.)+(.*\1){3}).{,6}$/im",
    r"/^(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u).{,7}$/im",
    r"/^(?=([^aeiou]*[aeiou]){5}[^aeiou]*$)\w{18,}/im",
    r"/^(.)(.)(.).{6,}\3\2\1$/im",
    r"/^(?=(.)+\1).{22,}$/im",
    r"/^(?=(.)+(.*\1){5,})\w{14,}$/im",
    r"/^(?=((.)+\2){3})\w{13,}$/im",
    r"",
    r"",
    r"/^(?!(.)+.*\1.*\1)\w{18,}$/im",
    ""]
print(myRegexList[idx])