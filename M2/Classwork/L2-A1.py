#empty tuple
my_tuple = ()

#Tuple having integers
my_tuple = (1, 2, 3,)
print(my_tuple)

#Tuple having mixed datatypes
my_tuple = (1, "Hello", 3.4, [1,2])
print(my_tuple)

#nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#Accessing tuple elements using indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])    # 'p'
print(my_tuple[-1])    # 't'

#nested tuple
n_tuple = ("mouse", [8, 4, 6, (1, 2, "abcd", {'1':2})], (1, 2, 3))

#nested index
print(n_tuple[0][3])  # 'c'
print(n_tuple[1][1])  # '4'
print(n_tuple[1][3][3]['1'])  # '2'

#slicing
print("Sliced tuple:", my_tuple[1:4])  # ('e', 'r', 'm')

#iterating through a tuple
for letter in my_tuple:
    print("hello", letter)