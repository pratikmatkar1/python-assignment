# # What is 7 to the power of 4?
# print ("7**4 : ",end="")  
# print (pow(7,4))



# #split the string into a list
# s = "Hi there Sam!"
# x = s.split()
# print(x)


# # #Given this nested list, use indexing to grab the word “hello”
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
# print(lst[3][1][2][0])


# #Given this nested dictionary grab the word “Hello”
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# print(d['k1'][3]["tricky"][3]['target'][3])

#Create a function that grabs the email website domain from a string into the form
#for example, passing “user@domain.com” will return: domain.com
# def x(email):
#     print("Your domain is: " + email.split('@')[-1])

# email = input("Please enter your email: ")
# x(email)

# #Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. 
# def x(abc):
#     if 'dog' in abc.lower():
#         print("True")
#     else:
#         print("False")

# abc = input("Please enter a string with/without dog: ")
# x(abc)


# #Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. 
# string = input("Please enter your string: ")
# def count(string):
#     count = 0
#     for word in string.lower().split():
#         if word == 'dog' :
#             count = count + 1
#             print(count)

# count(string)


# Use lambda expressions and the filter() function to filter out words from a list that don’t start with the letter ‘s’. For example:
# for example
# seq = ['soup','dog','salad','cat','great']
# should be filtered down to:
# ['soup','salad']

# seq = ['soup','dog','salad','cat','great']
# list(filter(lambda word: word[0]=='s',seq))


# You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: “No ticket”, “Small ticket”, or “Big Ticket”. If your speed is 60 or less, the result is “No Ticket”. If speed is between 61 and 80 inclusive, the result is “Small Ticket”. If speed is 81 or more, the result is “Big Ticket”. Unless it is your birthday (encoded as a boolean value in the parameters of the function) — on your birthday, your speed can be 5 higher in all cases.
# print("Please enter the speed in miles/hr: ")
# speed = int(input(" "))

# print("Please enter your birthday MM/DD/YYYY: ")
# birthday = str(input(" "))

# def speeding(speed, birthday):
#     if birthday == '09/13/1996':
#         s = speed + 5
#     else:
#         s = speed

#     if s <= 60:
#         print("No ticket")
#     elif s > 61 and s <= 80:
#         print("You get a small ticket")
#     else:
#         print("You get a big ticket.")

# speeding(speed, birthday)




#"Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24"
# def multiply(numbers):  
#     total = 1
#     for x in numbers:
#         total *= x  
#     return total  
# print(multiply((1, 2, 3, 4)))

# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((1, 2, 3, 4)))



#Define a function reverse() that computes the reversal of a string. For example, reverse(\"I am testing\") should return the string \"gnitset ma I

# def reverse(x):
#     count =0
#     stri =""
#     for i in x:
#         count +=1
#         stri = stri + x[len(x)-count]
#     return stri

# print(reverse("I am testing"))



#Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome(\"radar\") should return True.**"

# def isPalindrome(z): 
#     return z == z[::-1] 
# x = "radar"
# y = isPalindrome(x) 
  
# if y: 
#     print("Yes") 
# else: 
#     print("No")


#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. 
# def x(l1, l2):
#      result = False
#      for x in l1:
#          for y in l2:
#              if x == y:
#                  result = True
#                  return result
# print(x([1,2,3,4,5], [5,6,7,8,9]))
# print(x([1,2,3,4,5], [6,7,8,9]))



#Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following
# def histogram(list):
#         for x in range(0,len(list)):
#                 print('*' * list[x])
#         return
# li=[int(x) for x in input().split()]
# histogram(li)


#Write a program able to play the \"Guess the number\"-game, where the number to be guessed is randomly chosen between 1 and 20. 
# import random
# number=random.randrange(1,20)
# guess="wrong"
# print("Welcome to Number Guess")

# while guess=="wrong":
# 	response=int(input("Please type a no. between 1 and 20:"))
# 	try:
# 		val=int(response)
# 	except ValueError:
# 		print("try again")
# 		continue
# 	val=int (response)
# 	if val<number:
# 		print("Error: number is less than actual")
# 	elif val>number:
# 		print("Error: number is more than actual")
# 	else:
# 		print("Bingo!! Correct no.")
# 		guess="correct"

# print("Thank you ")





#Write a program that maps a list of words into a list of integers representing the lengths of the correponding words

# words = ['pratik','rohit','aabhas','suyash','karan']
# integers = [] 
# for i in range(len(words)):
#     integers.append(len(words[i]))
# print ("words:"+str(words))    
# print ("length of words:"+str(integers))





