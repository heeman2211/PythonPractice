#Write a function that generates prime numbers up to a given limit. The function should take an integer as input and return a list of prime numbers up to that limit.
def prime(a,b):
    prime = []
    for i in range(a,b+1):
        count = 0
        for j in range(2,i//2):
            if i%j == 0:
                count +=1
                break
        if (count == 0) and (i != 1):
            prime.append(i)
    return prime

a = int(input("Enter lower Limit of Prime Number series:\n"))
b = int(input("Enter upper Limit of Prime Number series:\n"))

print(prime(a,b))