
y= int(input("Enter your number :"))
ranger = range(2,30)
print(y, "is divisible by: ", end='')
for x in ranger :
    if x%y==0:
        print(x,"," ,end = '')



