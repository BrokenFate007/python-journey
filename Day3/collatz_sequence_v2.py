# Collatz Sequence
# Given a positive integer n from the user:
# If n is even, divide it by 2.
# If n is odd, multiply by 3 and add 1.
# Repeat until n = 1.



n = c = int(input("Enter a positive integer:"))
while c<int(2**20):
    n=c
    steps = 0
    print("This is the number:",n)
    while n!=1:
        if n%2==0:
            n=int(n/2)
        elif n%2!=0:
            n = n*3+1
        steps+=1
        # print(n,end=" ")
    if n == 1:
        print("Pity!!!")
        print("No. of steps taken:",steps)
        c+=1