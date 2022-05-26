#LITERABLES

#list= []  can add and remove its contents(manipulatable content)
#tuples=()   same as list but can't manpulate  its contents
#set= {}   sets are alws mixed up index given to characters always change the 1st character
          # is not neccesarily  index 0

#tuples and lists  allow redunduncy, sets don't


#list
fruits=[" apples"," orange"," banana"]
fruits_2=["pawpaw", "tomatoe"]
fruits.append("cherry")
print(fruits)
fruits.remove("cherry")
print(fruits)
my_fruits=fruits.pop(1)
print(fruits)
print(my_fruits)
fruits_3=fruits + fruits_2
print(fruits_3)
fruits.extend(fruits_2)
print(fruits)
fruits_2.clear()
print(fruits_2)
#tuple
fruits_4=(" apples"," orange"," banana")
print(fruits_4)
print(fruits_4[1])

new_list=list(fruits_4)#making tuple fruits_4 a list
new_list.append("grape")
fruits_4=tuple(new_list)#converting the list baack to tuple
print(fruits_4)

#set
fruits_5={"apples", "oranges", "oranges","oranges"}
print(fruits_5)
