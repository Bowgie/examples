#Danny Hardawar
#Notes from Chapter 4 - Python Crash Course - By Eric Matthes


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#for magician in magicians
#Tells python to retreieve the first value from the list magicians and associate it with the variable magician.

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick {magician.title()}.\n")

#Using Range
for value in range(1,5):
    print(value)

for value in range(1,6):
    print(value)

#using range to make a list
numbers = list(range(1, 6))
print(numbers)

#defiining a tuple
#A tuple is like a list but you use parentheses instead of brackets.
# Once you define a tuple you can access individual elements using an index

dimensions = (200 , 50)
print(dimensions[0])
print(dimensions[1])

#looping through a tuple like looping through a list
for dimension in dimensions:
    print(dimension)
