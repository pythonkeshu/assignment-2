#Q2. write a python program to print a dictionary whose keys should be the alphabet
# from a-z and the value should be corresponding ASCII values.

my_dict = dict()
required_data = range(97,123)
for i in required_data:
    my_dict[chr(i)] = str(i)
print(my_dict)