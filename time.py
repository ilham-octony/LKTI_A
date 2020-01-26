import datetime
import time
# current date and time
now = datetime.datetime.now()
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)
while True:
    print(now)
    time.sleep(2.0)
    #timenow = time.localtime()
    #print(timenow)
    #print(timenow.tm_hour)
    #print(timenow.tm_min)
    #t = now.strftime("%H%M%S")
    #print("time:", t)
    #if (t >= '130700'):
        #print("lets go")
