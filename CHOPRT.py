for i in range(int(input())):
    a,b = input().split(" ")
    if int(a) > int(b):
        print(">")
    elif int(a) < int(b):
        print("<")
    else:
        print("=")
