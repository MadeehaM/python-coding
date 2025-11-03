def bitsnumber(n):
    ones = 0
    zeros = 0
    while n:
        if n&1==1:
            ones+=1
        else:
            zeros+=1
        n=n>>1

    print("ones=",ones,"\nzeros=",zeros)
num= int(input("Enter a number:"))
bitsnumber(num)
