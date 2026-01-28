n = int(input("Enter the number of times you want to repeat the fibonacci sequence: "))
x = 0
y = 1 
for i in range(0,n):
    print(x)
    z = x + y
    x = y
    y = z
#we have to use z as a temporary storage space to store the sum of x and y before actually changing their value