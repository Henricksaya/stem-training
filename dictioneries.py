#Dictioneries in python
my_dict={
    "book":"dynamics",
    "Publisher":"Longhorn",
    "year":2001

     
   
}
#Accessing item
x=my_dict ["year"]
print(x)

#accesing using get()
y= my_dict["year"]
print(y)

# all keys
x=my_dict.keys()
print(x)


#all values
x=my_dict.values()
print(x)

#print all items in the dictionary
x=my_dict.items()
print(x)

#cheking iff keys exist
if "publisher" in my_dict:
    print("publisher is one of the keys")


print(len(my_dict))