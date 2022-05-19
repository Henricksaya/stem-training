print("Welcome To Basic Calculator")
a= int(input("enter 1st number :"))
b= int(input("enter 2nd number :"))
op=input("enter operation :")
if op == "+" :
    print("sum is")
    print(int(a+b))
if op == "*" :
    print("product is")
    print(int(a*b))
if op == "/" :
    print("divident is")
    print(int(a/b))
