from datetime import datetime

def main():
    now=datetime.now()
    print(now.strftime("the current date is:%A %d %b %Y"))

    #Printing local system's date and time
    print(now.strftime("locals datetime: %c"))
    print(now.strftime("locals date: %x"))
    print(now.strftime("locals time: %X"))
    
main()