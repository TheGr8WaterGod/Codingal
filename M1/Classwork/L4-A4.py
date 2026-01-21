n = int(input("Enter the number: "))
flag = True

for i in range(2, n):
    if n % i == 0:
        print("not a prime number")
        flag = False
        break

if flag:
    print("number is prime")