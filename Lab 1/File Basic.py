#Problem 1: 
#Print Hello, Python!
print ("hello, Python ")
#Print the same message without newline
print ("hello, Python ",end ="")

#Print the message with words separa---

print ("hello ", "Python", sep ="---")

#Problem 2: 
#Define 3 variables with the same value in a single line and print the
a=b=c =10
print (a)
print (b)
print (c)
#Problem 3: 
#Ask the user to enter two numbers, then swap their values using two different methods, and print the results before and after swapping.

X= input ("Enter first num ")
Y= input ("Enter second num")
# before 
print (X)
print (Y)

X,Y=Y,X
# After
print (X)
print (Y)

temp = X
X = Y
Y = temp

#Problem 4: 
#Ask the user to input two numbersPrint the results of: addition, subtraction, multiplication, division, floor division, modulus, exponentiation .

num1=  int(input ("Enter first num "))
num2= int(input ("Enter second num"))
print ("Addition",num1+num2)
print ("Subtraction",num1 - num2)
print ("multiplication",num1*num2)
print ("Division",num1/num2)
print ("floor division",num1//num2)
print ("Modulus",num1%num2)
print ("exponential",num1**num2)

#Problem 5: 
#Ask the user to enter two numbers. Print the first number repeated as many times as the second number.


num = int(input("Enter the number to repeat: "))
times = int(input("Enter how many times to repeat: "))

print(str(num) * times)




