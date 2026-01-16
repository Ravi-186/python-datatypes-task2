# 1. Declare variables of different types
num_int = 10                  # Integer
num_float = 3.5              # Float
text = "Python"              # String
is_active = True             # Boolean

# 2. Print values and their types
print("Integer value:", num_int, "Type:", type(num_int))
print("Float value:", num_float, "Type:", type(num_float))
print("String value:", text, "Type:", type(text))
print("Boolean value:", is_active, "Type:", type(is_active))

print("\n---------------------------")

# 3. Perform arithmetic operations
sum_result = num_int + num_float
difference = num_int - num_float
product = num_int * num_float
division = num_int / num_float

print("Addition:", sum_result)
print("Subtraction:", difference)
print("Multiplication:", product)
print("Division:", division)

print("\n---------------------------")

# 4. String concatenation with numbers
age = 22
message = "My age is " + str(age)   # converting int to string for concatenation
print(message)

print("\n---------------------------")

# 5. Type casting with user input
try:
    user_input = input("Enter a number: ")

    # Convert string input to integer
    int_value = int(user_input)      # string → int conversion
    print("Integer value:", int_value)

    # Convert string input to float
    float_value = float(user_input)  # string → float conversion
    print("Float value:", float_value)

except ValueError:
    # Handles invalid input like letters or symbols
    print("Invalid input! Please enter a valid number.")

print("\n---------------------------")

# 6. Demonstrate dynamic typing
value = 100        # integer
print("Value:", value, "Type:", type(value))

value = "Hello"    # now string
print("Value:", value, "Type:", type(value))

value = 45.6       # now float
print("Value:", value, "Type:", type(value))
