from binarytree import build, Node

# Construct a binary tree from a list of integers
s=input('enter the numbers : ')
data=list(map(int,s.split()))
root = build(data)

# Define function to add a new element to the binary tree
def add_element():
    value = int(input("Enter the value of the new element: "))
    node =Node(value)
    root.add(node)

# Define function to delete an existing element from the binary tree
def delete_element():
    value = int(input("Enter the value of the element to be deleted: "))
    node = root.search(value)
    if node is not None:
        root.remove(node)
        print(f"Element {value} has been deleted.")
    else:
        print(f"Element {value} not found in the tree.")

# Main program loop
while True:
    print("\nBinary Tree:")
    print(root)

    # Ask user for choice of action
    choice = input("\nEnter your choice (1=add, 2=delete): ")

    # Perform chosen action
    if choice == "1":
        add_element()
    elif choice == "2":
        delete_element()
    else:
        print("Invalid choice. Please try again.")
