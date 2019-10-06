from datetime import datetime, date, time, timedelta

def main():
    print(timedelta(days=365,hours=5,minutes=1))
    now=datetime.now()
    print("Today is:"+str(now))
    print("One year from now it will be:"+str(now + timedelta(days=365)))
    print("In two days and three weeks it will be:"+str(now + timedelta(days=2, weeks=3)))

    t=datetime.now()-timedelta(weeks=1)
    s=t.strftime("%A %B %d %Y")
    print("One week ago it was:"+s)
main()
