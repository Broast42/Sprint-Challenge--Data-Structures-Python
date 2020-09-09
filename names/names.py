import time
from singly_linked_list import LinkedList

start_time = time.time()


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names = names_1 + names_2
names.sort()

#duplicates = []  # Return the list of duplicates in this data structure
duplicates = LinkedList()

#Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.add_to_head(name_1)
new_list = LinkedList()
for n in names:
    new_list.add_to_head(n)

node = new_list.head
while node.next_node is not None:
    if node.value == node.next_node.value:
        duplicates.add_to_head(node.value)
    node = node.next_node



end_time = time.time()
#print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
duplicates.print_values()
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
