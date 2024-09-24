def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25) # работает
print_params(c = [1,2,3]) # работает

values_list = [1, 'строка', True]
values_dict = {"a" : 1, "b" : 'строка', "c" : True}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [62, 'Danil']
print_params(*values_list_2, 42)
