def sieve(n):
    prime = [True for i in range(n+1)]
    num =2
    while (num*num<=n):
        if prime[num]:
            for i in range(num**2,n+1,num):
                prime[i]=False
        num +=1
    prime[0]=prime[1]=False
    for p in range(n+1):
        if prime[p]:
            print(p)

n = int(input("Enter a number to find prime numbers less than the number:"))
sieve(n)