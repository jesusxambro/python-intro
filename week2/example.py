print("Example") #Hello
college_name = "Course 101"

print(college_name) #Passing a variable to a function.

x, y, z = 10, 1, 2 #Multi variable and value assignments.

print(x)
print(y)
print(z)

age = 44
a = 44

_age = 100
# $age = 100

Age = 100
age = 99

print(age) #Case sensitive names

print(x,"+",y,z) #multi argument print statement

x = "X Men"
print(x)
age = "99" #age is a string after this line
# age = int(input("What is your age?")) #take in a string, then convert to int
print(age)

# price_of_eggs = float(input("What is the cost of a dozen eggs?"))
# print(type(price_of_eggs)) #check the type of the variable. Here it is a float.

print("Remainder Example:")
remainder_example = 4%2
print(remainder_example)


print("Multi Line Assignment:")
super_long_variable = 4 + 3 +3 +4 \
                      + 3 +3+4 \
                      + 3 +3+4 \
                      + 3 +3

print(super_long_variable)

print("Multi Line Prints")
print("Monday's sales are", "monday",
      "and Tuesday's sales are", "tuesday",
      "and Wednesday's sales are", "Wednesday")

print("Concatenation")

message = 'Hello ' + 'world'
print(message)

#/n or /t causes a newline or tab
print("Hello\t", "Hello")

name = "Spider"
print("Hello", name, ".")
print(f'Hello {name +"man"}.')

num = 123.456789
print(f'{num:.4f}')

print(f'{num:<20.2f}')
print(f'{num:>20.2f}')
