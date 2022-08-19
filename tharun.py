def prime_number(N,i=2):
    if N==1:
        return False
    if N==i:
        return True
    elif N%i==0:
        return False
    return prime_number(N,i+1)
N=int(input("enter the number: "))
if prime_number(N):
    print(N,"is a prime number")
else:
    print(N,"is not a prime number")
