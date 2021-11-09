#Defines a function hash_key that accepts the parameters key and m.
#Uses a simple modulus operation(returns the remainder or signed remainder of a division) to determine the hash value
def hash_key( key, m):
    return key % m
#Defines a variable m that is initialized to the value 7. This is the size of our hash table
m = 7
print(f'The hash value for 3 is {hash_key(3,m)}')
print(f'The hash value for 2 is {hash_key(2,m)}')
print(f'The hash value for 9 is {hash_key(9,m)}')
print(f'The hash value for 11 is {hash_key(11,m)}')
print(f'The hash value for 7 is {hash_key(7,m)}')

#python dictionary, a type of hashtable
employee = {
    'name': 'John Doe',
    'age': 36,
    'position': 'Business Manager.'
}

print (f"The name of the employee is {employee['name']}")
employee['position'] = 'Software Engineer'
print (f"The position of {employee['name']} is {employee['position']}")
employee.clear()