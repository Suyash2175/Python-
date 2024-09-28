# Function to square a given number random code
def square_number(n):
    return n * n

# Creating a list of the first 50 integers
integers_list = list(range(1, 51))

# Example usage: Squaring each number in the list
squared_numbers = [square_number(n) for n in integers_list]

# Printing the squared numbers
print(squared_numbers)
