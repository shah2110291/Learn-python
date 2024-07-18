name="M shah khalid"

a_letter= name[0]
short_name= name[0:5] 
reverse_order =name[-11:-6] 
 
print(a_letter)
print(short_name)
print(reverse_order)


print(name[:13]) #same is = print(name[0:13])
print(name[1:]) #same is = print(name[1:13])
print(name [2: 10 :2])


# printing some letters
name = "M shah khalid"
indices = [2, 7, 11]  # Indices of 's', 'k', 'l'
letters = [name[i] for i in indices]
print(''.join(letters))  # Output: s k l
