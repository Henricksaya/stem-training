#set
fruit={"mango", "apple", " cherry" ,"banana", "pineapple"}
print (fruit)

a=input(" Please enter name ")
print("Hi ",a )

#method 2
def outputname (b):
    print("hi",b)
    outputname("shee")

#functions to replaace characters in string
def replace_in(phrace):
    word=""
    for letter in phrase :
        if letter.lower() in "a e i o u" :
            word =word +"g"
        else: word= word +letter
    return word
print(replace_in(input("enter a phrase :")))