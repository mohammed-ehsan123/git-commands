
# wap to check if the given number is prime or not

n = int(input("Enter the number: "))

for i in range(2,n):

    if n % i == 0:

        print("It is not a Prime Number")

        break

else:

    print("It is a prime number")



