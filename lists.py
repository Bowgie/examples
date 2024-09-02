#Danny Hardawar
#Notes from Chapter 3 - Python Crash Course - By Eric Matthes

#Square Brackets indicate a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#To access elements in a list, you tell python of the index
print(bicycles[0])

#using string methods 
print(bicycles[0].title())

#index positions start at 0

#Using individual values
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)


#Using append to build a list automatically
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserting a new element
motorcycles.insert(0, 'ducati')
print(motorcycles)

#The pop method removes the last item in the list.
#But allows you to work with the item after removing it.
#The term pop relates to list like a stack of items.
#You pop one item off the top of the stack
