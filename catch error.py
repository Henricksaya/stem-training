try:
    div=10/0
    value=int(input("Enter a number: "))
    print(value)

except ValueError:
    print("invalid number entered")
except ZeroDivisionError:
    print("divident error")