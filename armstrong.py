def happy(a):
    sum=0
    while a!=0:
        sum=sum+pow(a%10,2)
        a=a//10
    if sum==1:
        print("it is an happy number")
        return sum
    elif sum==4:
        print("it is not an happy number")
        return sum
    else:
        happy(sum)
a=int(input("enter the number"))
happy(a)

