def my_function(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return my_function(x - 1) + my_function(x - 2)