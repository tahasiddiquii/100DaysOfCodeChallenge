def reverse_array_in_place(arr):
    arr[:] = arr[::-1]

# Example usage:
my_array = [1, 2, 3, 4, 5]
reverse_array_in_place(my_array)
print(my_array)  # Output: [5, 4, 3, 2, 1]
