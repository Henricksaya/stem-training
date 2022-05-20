#lists
word=["1.apples","2.love","3.people","4.chairs"]
#in python everthing is indexed from 0
print(word[0])
print(word[1])
print(word[2])
print(word[3])
numbers=[5,6,7,8]
print(numbers[2])
#lists can store any data type
data=["a", 1, "foo", 6, 7, "hey"]
print(data)
#nested list
m=[
    [5,7,8],#first row
    [3,2,1] #second row
]
print(m[1][1])
print(m)







#lists can be readdressed
strg= ["hello" ,"class","123","51","abc","hey","b","a"]
print(strg)
print(strg[5]) #space between hello and class
print(strg[6])#the leter c from class
print(strg[7-3])
strg[0]=strg[7-2]#replacing an index/reasigning an index in this case index zero been
print(strg)#reasigned to index 5


subjects=["maths","science","religeous"]
subjects[2]= "mechanics"
print(subjects)
