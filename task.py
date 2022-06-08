#number=[1,2,3,4,5,6,7,8,9]

def print_func(n):
    for num in range (n):
        if num%3 ==0:
            print("foo")
        elif num%5 == 0:
            print("bar")
        elif num%3==0 and num%5==0:
            print("foobar")
        else:
            print(num)
    #return num
print_func(10)
