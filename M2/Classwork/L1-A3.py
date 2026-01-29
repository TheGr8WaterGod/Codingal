def convert_to_dict(lst):
    result = {}
    for item in lst:  # item = [2, 'Lula Powell', 'V']
        result[item[0]] = item[1]  # Use first element as key, second as value
    return result

students = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

print("\nOriginal list of lists:")
print(students)

print("\nConverted list to dictionary:")
print(convert_to_dict(students))
'''
# Looping examples
lst = [1, 2, 3, 4, 5]

# Case 1: Using index
for i in range(0, 5):
    print(lst[i])

# Case 2: Direct iteration
for i in lst:
    print(i) 
'''