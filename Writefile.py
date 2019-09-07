def main():
    f=open("textfile.txt","a")
    for i in range(10):
        f.write("This is line "+ str(i)+"\r\n")
        print("Test")
    f.close()

main()