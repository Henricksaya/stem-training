#create a single function that:
    #for a range of integers between 0 and n(inclusive)
    #if the number is an even number,
        #Half it
    #if the number is an odd number 
        #double it
    

    #for the output generated in the previous function,
    #write the result to a file named    'results.txt'
n=int(input("Enter no. range: "))

#n=10

def some_func(n):
    for num in range(0,n+1):
        if num % 2==0:
            num2=0.5*num
            print("For",num,"output is", num2)

        elif num % 2 != 0:
            num2=2*num
            print("For",num,"output is", num2)

output=some_func(n)
            
print(output)

#file =open('results.txt','a')
#file.write(output)
#file.close()
