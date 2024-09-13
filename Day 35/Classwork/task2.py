"""Classwork 3: List Functions and Methods
Create a list named numbers that contains the following integers: 10, 20, 30, 40, 50, 60, 70, 80, 90.
Use the append() function to add the number 100 to the end of the list.
Use the insert() function to add the number 5 at the beginning of the list.
Use the remove() function to remove the number 30 from the list.
Use the sort() function to sort the list in ascending order.
Use the reverse() function to reverse the order of the list.
Use the index() function to find the index of the number 50.
Use the count() function to count how many times 20 appears in the list."""


integers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
integers.append(100)
integers.insert(0 , 5)
integers.remove(30)  
integers.sort()
integers.reverse()
integers.index(50)
integers.count(20)
print(integers)