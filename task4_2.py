def hash_function(key):
    return key % m
m=7
hash_table = [[] for _ in range(m)]

value_list = [3, 2, 9, 11, 7]
for value in value_list:
    key = hash_function(value)
    hash_table[key].append(value)

menu = "Choose an option:\n1. Construct the whole hash table\n2. Add a new element to the hash table\n3. Update a value of a certain key\n4. Delete an element from the hash table\n5. Search for an element in the hash table\n6. Print all elements with their keys of the hash table\nEnter your choice:"

while True:
    choice = input(menu)

    if choice == "1":
        print(hash_table)

    elif choice == "2":
        value = int(input("Enter a new value: "))
        key = hash_function(value)
        if value not in hash_table[key]:
            hash_table[key].append(value)
            print("Value added successfully.")
        else:
            print("Value already exists in the hash table.")

    elif choice == "3":
        key = int(input("Enter a key: "))
        if len(hash_table[key]) > 0:
            print(f"Current values for key {key}: {hash_table[key]}")
            old_value = int(input("Enter an old value: "))
            if old_value in hash_table[key]:
                new_value = int(input("Enter a new value: "))
                if new_value not in hash_table[key]:
                    index = hash_table[key].index(old_value)
                    hash_table[key][index] = new_value
                    print("Value updated successfully.")
                else:
                    print("New value already exists in the hash table.")
            else:
                print("Old value does not exist in the hash table.")
        else:
            print("Key does not exist in the hash table.")

    elif choice == "4":
        value = int(input("Enter a value to delete: "))
        key = hash_function(value)
        if value in hash_table[key]:
            index = hash_table[key].index(value)
            del hash_table[key][index]
            print("Value deleted successfully.")
        else:
            print("Value does not exist in the hash table.")

    elif choice == "5":
        value = int(input("Enter a value to search for: "))
        key = hash_function(value)
        if value in hash_table[key]:
            print(f"Value {value} found at key {key}.")
        else:
            print(f"Value {value} not found in the hash table.")

    elif choice == "6":
        for key, values in enumerate(hash_table):
            if len(values) > 0:
                print(f"Key {key}: {values}")

    elif choice.lower() == "exit":
        break


    else:
        print("Invalid input. Please try again.")

