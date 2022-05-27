print("Welcome To Basic Calculator")
try:
    a= int(input("enter 1st number :"))
except ValueError:
    print("invalid number entered")
try:
    b= int(input("enter 2nd number :"))
except ValueError:
    print("invalid number entered")

try:
    op=input("enter operation :")
    if op == "+" :
        print("sum is")
        print(int(a+b))
        print("done")
    elif op == "*" :
        print("product is")
        print(int(a*b))
        print("done")
    elif op == "/" :
        print("divident is")
        print(int(a/b))
        print("done")
    elif op == "%" :
        print("modulus is")
        print(int(a%b))
        print("done")
    else :
        print("SORRY INVALID OPERATOR")
except ValueError:
    print("sorry invalid function")
