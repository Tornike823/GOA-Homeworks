"""Classwork 2: Basic List Operations
Create a list named fruits that contains the following items: "apple", "banana", "cherry", "date", and "elderberry".
Print the entire list.
Access and print the first and last items in the list.
Add a new fruit "fig" to the list.
Remove "banana" from the list.
Change the value of the second item to "blueberry".
Print the length of the list."""

items = ["apple", "banana", "cherry", "date","elderberry"]
print(items)
print(items[0] , items[4])
items.append("fig")
items[1] = "blueberry"
n = len(items)
print(n)
