# #user define insertion
methodes_of_list = ['10', '221 ', '123', '1', '3232', '21', '12', '0']

insert_Index  = int(input("Enter the Index :"))
insert_value2 = input("Enter value to Insert :")
methodes_of_list.insert(insert_Index, insert_value2) 
print("After Insertion :", methodes_of_list)

delete_index =int(input("Enter Index for Delete :"))
methodes_of_list.pop(delete_index)
print("Updated List :", methodes_of_list)
 