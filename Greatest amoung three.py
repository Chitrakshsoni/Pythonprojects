a = int(input("Enter a  number: "))
b = int(input("Enter second  number: "))
c = int(input("Enter third number: "))
if a>=b and a>=c:
    max = a
elif b>=c and b>=a:
    max=b
else:
    max=c
print("Max amoung three is: ",max)
