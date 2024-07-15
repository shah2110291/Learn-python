# Explicit type casting, also known as type conversion, is when you manually convert a variable from one type to another using predefined functions. 
# Explicit type casting
num_str = "123"
num_int = int(num_str)  # Convert string to integer
print(num_int, type(num_int))  # Output: 123 <class 'int'>

num_float = float(num_str)  # Convert string to float
print(num_float, type(num_float))  # Output: 123.0 <class 'float'>

num_int = 10
num_str = str(num_int)  # Convert integer to string
print(num_str, type(num_str))  # Output: "10" <class 'str'>


# Implicit type casting, also known as type coercion, is when Python automatically converts one data type to another without any explicit instruction from the user. 
# Implicit type casting
num_int = 123
num_float = 1.23

result = num_int + num_float  # int is implicitly converted to float
print(result, type(result))  # Output: 124.23 <class 'float'>

num_int = 10
num_bool = True

result = num_int + num_bool  # bool is implicitly converted to int
print(result, type(result))  # Output: 11 <class 'int'>

