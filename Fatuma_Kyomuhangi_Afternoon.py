# Exercise 1.
diction = {
    'name': 'Morris',
    'age': 24,
    'country': 'Uganda'}
# Using the values() method to get values.
dict_list = list(diction.values())
print(dict_list)

# Exercise 2.
# How to check if a key exists in a dictionary
if 'age' in diction:
    print("Age exists in the dictionary")

# Exercise 3
# How to change dictionary items and update them
diction['age'] = 20

# Exercise 4
# Example on how to add an item in a dictionary
diction['model'] = 'Cape-Verde'
print(diction)


# Exercise 5
# How to loop through  dictionaries
# Looping through a dictionary
for item in diction :
    print(item)
# Nest dictionaries
diction2 = {
    'name': 'Prilla',
    'class':'Senior 2',
    'subjects':{'subject1': 'Math', 'subject2': 'Chem', 'subject3': 'ComputerS'}
    }
print(diction2['subjects']['subject1'])

#STRINGS
# Exercise 1
name = "Susannitta"
print(len(name))

# Exercise 2
for x in name:
    print(x)
print('Next is string slicing')
# Exercise 3
# String slicing
print(name[2:5])