
#  1.taking input from user and saying them, good afternoon
name = input("Enter your names: ")
d_o_b= input("Enter you Date of Birth:")
print(f"HI, {name} GOOD AfterNoon, and most Welcome and you date of birth is {d_o_b}")


#  2. Repleacing letter in the given TEXT
letter ='''
Dear <|Name|
you are selected
<|Date|>'''
print(letter.replace(f"<|Name|", "Shah khalid").replace("<|Date|>", "01/03/2025"))

# the following one is for that it repleace <|Name| by the user input.
print(letter.replace(f"<|Name|",  name).replace("<|Date|>",  d_o_b))


# Detecting Double Space in a string
find_double_space="shah khalid is good  boy"
print(find_double_space)
print(find_double_space.find("  "))
print(find_double_space.replace("  ", " ")) #this will replace double space into single space