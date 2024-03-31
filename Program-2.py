given_list = [10, 'abc', 12, 'xyz']

int_value = list(filter(lambda int_val:type(int_val)==int , given_list))

str_value = list(filter(lambda int_val:type(int_val)==str , given_list))

print("The Integer values in the given list are", int_value)
print("The String values in the given list are", str_value)