# strings and casting

# Lets have a look at some industry practices
# single and double quotes example


# single_quotes = 'single quotes \'WoW\''
# doouble_quotes = "double quotes 'Wow'"
# print(single_quotes)
# print(doouble_quotes)



# String slicing

#greetings = "hello World" # string
# indexing in python starts from 0
# H e l l o   w o r l d   !
# 0 1 2 3 4 5 6 7 8 9 10 11
# how can we find out the length of this statement/ string

#print(len(greetings))
# We have a methos called len() to find out the total length of statement

# greetings = "hello World" # string
#
# print(greetings[0:5]) # outputs hello starting from 0 to 4
# print(greetings[6:11])
# print(greetings[-6:])

# Reverse indexing starts with -1

# #Lets have a look at some string methods
# white_space = "lot's of space at the end                "
# # strip() helps us delete all white spaces
# print(len(white_space))
# print(len(white_space.strip()))
#
# Example_text = "here's some text with lot's of text"
# # print(Example_text.count("text"))
#
# # Counts the number of times the word is mentioned in the statement
# print(Example_text)
#
# print(Example_text.upper()) # upper = capitals
# print(Example_text.lower()) # lower
# print(Example_text.capitalize()) # captalise the first letter of string
# print(Example_text.replace("with", ",")) # replaces with for a comma


# Concatination and Casting

First_Name = "James"
Last_Name = "Bond"
age = 99 #int
# print(First_Name, Last_Name, str(age))
print(type(int(age)))


# print(Last_Name)

# F- String is a formatting
print(f"{First_Name} {Last_Name} is {age} old")
