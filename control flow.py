#if statements
x=4
if x >=1 :
    print ("hey im here")
    x-=1
    print(x)
print("im done")


#else statemens
x=2
if x==10 :
    print(x)
else :
    print ("not 10")


#elif (to creat grading system)
grade=int(input("write student score: "))
if grade >80 & grade <=100 :
    print("Student got an A") 
elif grade >=70 & grade < 80 :
     print("Student got a B")
elif grade >=60 & grade < 70 :
        print ("student got a C")
elif grade >=50 & grade <60 :
        print("Student got a D")
elif grade < 50 & grade > 0 :
        print("You got an E !, go study mehn")
else :
    print("invalid marks")
