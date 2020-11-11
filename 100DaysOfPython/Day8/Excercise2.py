n = int(input("Check this number: "))

def prime_checker(number):
    if n == 2:
        print("Its a primr number")
    for i in range(2,int(n/2) + 1):
        if n % i == 0:
            print("Its not a prime number")
        else:
            print("Its a prime number")

prime_checker(number=n)
