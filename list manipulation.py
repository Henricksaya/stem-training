#for loop in python
mangoes="book"
for i in mangoes:
    print(i)

print("done")

#for loops with lists
words=[" Dre,"," Dida,"," kings,"]
for word in words:
    print("dear;" + word +  " welcome to town")


#example 2
str="hello guys, welcome back to my class"
count=0
for x in str:
    if (x=='o'):
        count +=1
print("the number of zeros is: ",count)


#program extracting letter 'L'
str="hello guys, welcome back to my class"

for x in str:
    if (x=='l'):
        continue
    else:
        print(x)

str="hello guys, welcome back to my class"
outstr=""
for x in str:
    if x !='l' and x!='e' and x!='u':#not equal to
        outstr +=x
print(outstr)