# empty dictionary 
my_dict = {}  

# Dictionary with integer keys
my_dict = {1: 'candy', 2: 'chocolate'}


# Dictionary with mixed keys
my_dict = {'name': 'Varun', 1: [2, 4, 3]}

my_dict = {'name': 'John', 'age': 11}

# Output: Varun
print(my_dict['name'])
print(my_dict.get('age'))


#update value 
my_dict['age'] = 10
print(my_dict)

#add item
my_dict['address'] = 'Downtown' 
print(my_dict)  

#access a particular element
print("Address:", my_dict.get('address'))

#remove all elements
my_dict.clear()
print(my_dict)