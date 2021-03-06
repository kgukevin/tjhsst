import sys
idx = int(sys.argv[1])-1
myRegexList = [
    r"/^\w*[aeiou][b-df-hj-np-tv-z]{4}[aeiou]\w*$/i",
    r"/\".+\"/is",
    r"/\bdef .*\(.*\):(\n   *.+)*/i",
    r"/^((0|10)(10)+1?|01|10|101|010)$/",
    r"/^0*(1|00+)*0*$/",
    r"/^[01]*(2([01]+|2[01]+|22[01]+|22$)|2$|22$)*[01]*$/",
    r"/^[1-9]\d*([02468][048]|[13579][26])$|^[048]$|^([02468][048]|[13579][26])$/",
    r"/^[1235679]*$/",
    r"/^\?{9}(\?(\.|x|o){7}\?){6}\?{9}$/i",
    r"",
    r""]
print(myRegexList[idx])