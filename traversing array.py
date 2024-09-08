# Initializing a 2D array (list of lists)
two_d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Function to traverse and print the elements of a 2D array
def traverse_2d_array(array):
    print("Traversing the 2D array:")
    for i in range(len(array)):  # Loop through each row
        for j in range(len(array[i])):  # Loop through each column in the row
            print(array[i][j], end=' ')  # Print the element
        print()  # New line after each row

# Call the function to traverse the 2D array
traverse_2d_array(two_d_array)
