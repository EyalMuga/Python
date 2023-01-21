# # With these prerequisites out of the way,
# # let's go ahead and create a simple decorator that will convert a sentence to uppercase.
# # We do this by defining a wrapper inside an enclosed function.
# # def uppercase_decorator(function):
# #     # inside the function I have a wrapper function that returns make_uppercase
# #     def wrapper():
# #         func = function()
# #         make_uppercase = func.upper()
# #         return make_uppercase
# #
# #     return wrapper
# #
# import datetime
# import math
#
#
# # def greeting(function1):
# #
# #     def greeting_func():
# #         print(f"""
# # hello and welcome to {function1.__name__} function:
# #         """)
# #         print("==============================")
# #         function1()
# #         print(f""""
# # Thank for choosing our {function1.__name__} function""")
# #     return greeting_func
# #
# #
# # @greeting
# # def Factorial():
# #     number = int(input("please enter number:"))
# #     fact = math.factorial(number)
# #     print(f"the factorial of: {number} is {fact}")
# #
# #
# #
# # Factorial()
#
#
# # import time
# #
# #
# # def performance_log(func):
# #     def decorator(*args, **kwargs):
# #         start = time.perf_counter()
# #         result = func(*args, **kwargs)
# #         end = time.perf_counter()
# #         print(f"the running time of the function was: {end - start}")
# #         return result
# #
# #     return decorator
# #
# #
# # @performance_log
# # def long_running_func(num, iters):
# #     val = 1
# #     for i in range(iters):
# #         val *= num
# #     return val
# #
# #
# # long_running_func(1, 200000000)
#
#
# class Bank:
#     def __init__(self, bank_name):
#         self.name = bank_name
#
#     def working_hours(callable):
#
#         def wrapped_callable(*args, **kwargs):
#             x = datetime.datetime.today()
#             if x.strftime("%a") in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu'] and 17 > int(x.strftime("%H")) > 9:
#                 ret_val = callable(*args, **kwargs)
#                 return ret_val
#             else:
#                 raise Exception("not in Working time")
#
#         return wrapped_callable
#
#     @working_hours
#     def withdraw(self, amount: int):
#         print("callable withdraw", amount)
#         return amount
#
#     @working_hours
#     def deposit(self, amount):
#         print("callable deposit", amount)
#         return amount
#
#     @staticmethod
#     def feedback(feedback_text: str):
#         print("callable feedback")
#
#
# new_Bank = Bank('Muga')
# print(new_Bank.withdraw(123))


# def single_str_arg(func):
#     def wrapped(*args, **kwargs):
#         if len(args) == 1 and str:
#             return func(*args, **kwargs)
#         else:
#             raise ValueError("The decorated function must be called with a single string argument.")
#
#     return wrapped
#
# @single_str_arg
# def check_str(word:str):
#     print(word)
#
# def single_str_arg(func):
#     def wrapped(*args, **kwargs):
#         if len(args) == 1 and str:
#             return func(*args, **kwargs)
#         else:
#             raise ValueError("The decorated function must be called with a single string argument.")
#
#     return wrapped
#
# @single_str_arg
# def check_str(word:str):
#     print(word)
#
#
# check_str('eyal')

# check_str('eyal')


# Implement a decorator @valid_param_types that receives as parameter allowed argument types and validates whether
# the argument passed to a function answers this requirement. If the validation fails, the decorator should raise an
# InvalidArgument exception.


def valid_parameter_types(allowed_type):
    def decorator(func):
        def wrapper(*arg):
            if not isinstance(*arg, allowed_type):
                raise Exception(f"Not the expected type")
            return func(*arg)

        return wrapper

    return decorator
