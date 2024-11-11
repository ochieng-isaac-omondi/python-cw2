#Program enables users put there names, greets them ,calculates year of birth and  handles errors. 
try:   #try block wraps code that may arise an error.
    name = input('Whats your name:')  #get users name
    print('Hello ' + name)       #greet user    

    age = int(input('Enter your age: ')) #ask for users age

    #calculate year of bith assuming the current year is (2024)
    current_year = 2024 
    year_of_birth = current_year - age
    print("You were born in",year_of_birth) #display the year of birth

#Handles the case where the input is not numeric
except ValueError:  
    print("please enter your valid number of age!")

    #Extended Program
try:
    fav_number = int(input('What is your favorite number: '))  #ask for favorite number
    if fav_number % 2 == 0:   #check whelther the number is even or odd
            print('Your favorite number is an even number')
    else:
        print('Your favorite number is an odd number')

    #implementing chained and nested conditons to provide additonal feedback based on user's input.
    if fav_number > 10:
        print(" which exceeds 10")
    elif fav_number < 10:
        print("which is below 10")
    else:
        print("and it's exactly 10")
    except ValueError: #	Intentionally introducd an IndentationError
    print('please enter a valid number')

'''Testing and Debugging
Error: IndentationError
Line 33: The except block is in the wrong position. this can be resolved by aligning the except block with the try block because 
it is placed inside the if-elif-else structure.

Errors encountered:
SyntaxErrors: this were solved by reviewing the code line by line to check out for missing characters.
NameErrors:this were solved by checking the spellings and remembering the variable names which were case senstive
IndentationErrors: this were solved by checking missing extra or missing indentaation.'''
