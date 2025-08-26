ans=0
x=int(input("enter an integer: "))
if x < 0:
    while ans**2<-x:
        ans = ans+1
    if ans**2 == -x:
        print("Square root of ", str(x), "is", str(ans)+"i")
    else: 
        print("this is not perfect square")
elif x > 0:
    while ans**2 < x:
        ans = ans+1
    if ans**2 == x:
        print(ans)
    else: 
        print("this is not perfect square")