#INSTRUCTIONS:
#
#Part 1: If statements

# Using if statements, try to print out
#
#
#
#
#
#
# Part X: Lists

#Make the string "sentence_string" into a list called "sentence_list"
#Use a for loop and an append function like this: list.append(something)

sentence_string = "Hello, my name is Monty Python."

sentence_list = []
for letter in sentence_string:
    sentence_list.append()



# Print every item of the list using a for loop
sentence_list = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'm', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'M', 'o', 'n', 't', 'y', ' ', 'P', 'y', 't', 'h', 'o', 'n']

# Using a for statement and an if statement, print all the vowels from the sentence
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in sentence_list:
    if letter in vowels:
        print letter

#Make a new function that will spit out all the vowels in any list.
#The function's parameters should be "list" and "vowels."
