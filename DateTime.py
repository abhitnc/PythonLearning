from datetime import datetime, time, date

def main():
    now=datetime.now()
    print(now.strftime("the current date is:%A %d %b %Y"))

    print(now.strftime("locals datetime: %c"))
    print(now.strftime("locals date: %x"))
    print(now.strftime("locals time: %X"))
    
main()
