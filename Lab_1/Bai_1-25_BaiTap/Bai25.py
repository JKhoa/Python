# Define a function called is_group_member that takes two parameters: group_data (a list) and n (an integer).
def is_group_member(group_data, n):
    # Iterate through the elements (values) in the group_data list.
    for value in group_data:
        # Check if the current value is equal to the given integer, n.
        if n == value:
            return True  # If found, return True.
    return False  # If the loop completes and no match is found, return False.

# Call the is_group_member function with two different lists and integers, and print the results.
print(is_group_member([1, 5, 8, 3], 3))  # Output: True (3 is in the list)
print(is_group_member([5, 8, 3], -1))    # Output: False (-1 is not in the list)
