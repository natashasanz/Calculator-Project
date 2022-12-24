#Natasha Sanchez 
#11/05/22
#Sanchez-Calculator.py
#This application will alllow the user to calculate the sum of two numbers (add), the difference between two numbers (subtract), the product of two numbers (multiple), or the quotient of two numbers (division)


option = input ('Please select one option: add/subtract/multiply/divide: ').lower()
print ('You chose {}.'.format(option))

first_number = input ('What is your first number? ')
second_number = input ('What is your second number? ')

first_number = float (first_number)
second_number = float (second_number)
result = 0

if option == 'add':
    result = first_number + second_number
    print ('{} + {} = {}'.format(first_number, second_number, result) )
elif option == 'subtract':
    result = first_number - second_number
    print ('{} - {} = {}'.format(first_number, second_number, result))
elif option == 'multiply':
    print ('{} * {} = {}'.format(first_number, second_number, result))
elif option == 'divide':
    print ('{} / {} = {}'.format(first_number, second_number, result))
else :
    print ('The option you chose {} is not valid'.format(option))
    print ('Please try this program again.')
