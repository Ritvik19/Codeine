def sod(n):
    sum = 0
    while n != 0:
        sum += n%10
        n//=10
    return (sum)

for i in range(int(input())):
    print(sod(int(input())))
