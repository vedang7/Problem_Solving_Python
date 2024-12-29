# def my_first_deco(func):
#     def log_func(*args, **kwargs):
#         print("Inside function {}".format(func.__name__))
#         func(*args, **kwargs)
#         print("Completed function {}".format(func.__name__))
#     return log_func

# def my_second_deco(func):
#     def print_func(*args, **kwargs):
#         print("Bye")
#         func(*args, **kwargs)
#     return print_func

# @my_first_deco
# @my_second_deco
# def test_add(a: int, b: int) -> int:
#     print (a+b)

# test_add(9, 8)
arr = [1, 4, 8, 9]
arr.insert(80, 90)
print(arr)