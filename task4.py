def hash_key(v, m):  # Defines a function hash_key that accepts the parameters key and m
    return v % m  # Uses a simple modulus operation to determine the hash value
m=int(input('Enter the size of input list/ number of all elements :'))
v=int(input('Enter the value: '))
print(f'The hash value is :{hash_key(v,m)}')