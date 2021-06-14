num=int(input("Enter your  first number: "))
num1= int(input("Enter the second number : "))
ranger= range(num, num1)
for v in ranger:
    v_squared= v.__pow__(2)
    if v_squared%4==0:
        print(v_squared," is divisible by 4 ")
    else:
        print(v_squared," is not divisible by 4")
