methodes_of_list = ['10', '221 ', '123', '1', '3232', '21', '12', '0']
print("Original List:", methodes_of_list)

# Create a copy of the original list
original_list = methodes_of_list.copy()

methodes_of_list.append("9012")
print("After Append:", methodes_of_list)

methodes_of_list.sort(key=int)
print("After sort:", methodes_of_list, "\n")

methodes_of_list.reverse()
print("After Reverse:", methodes_of_list, "\n")

# Insert value at index 1                                   # the insert methode samply will be like following:
insert_value= 1000                                          # methode_of_list.insert(index, number)
methodes_of_list.insert(1, str(insert_value))               # print(methode_of_list)
print("Insert Value is:" , insert_value)
print("After Insert:", methodes_of_list, "\n")

# Pop value at index 0
popped_value = methodes_of_list.pop(0)
print("POP value is:", popped_value)
print("After the POP:", methodes_of_list, "\n")

# Print the original list
print("Original list:", original_list)
