class Dog:
    def __init__(self,no_of_eyes,color,no_legs,fur_content,):
        self.no_of_eyes=no_of_eyes
        self.color=color
        self.no_legs=no_legs
        self.fur_content=fur_content
    def bark(self):
        print ("woof woof!")

    def pee(self):
        print("bruh bruh")

    def jump(self):
        print("dog jumps")

    def run(self):
        print("dog runs")
german_shephard=Dog(no_of_eyes=2,color='Grey',no_legs=4,fur_content='less')
dodger=Dog(no_of_eyes=1,color='white',no_legs=3,fur_content='more')
wagido=Dog(2,'Brown',4,'more')# si  must u specify, borake ufollow exact order
        
print(german_shephard.color,german_shephard.no_of_eyes)
print("your dogs colour is",dodger.color)

wagido.color='darkbrowm'#you can change class traits as so
print(wagido.color)
wagido.bark()
dodger.pee()
german_shephard.run()
print (wagido.no_legs)