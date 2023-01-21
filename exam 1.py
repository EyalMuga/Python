# Implement a function second_largest that receives a list of numbers and returns the second-largest number in the list.
# You can assume that there are no non-numeric values in the list.
# list1= [54, -1, 45, 987, 5, 2, 65, 7, 12]
# list1 = [1000, 54, -1, 45, 987, 5, 2, 65, 7, 12]


def max_number(list1: list) -> int:
    max_num = max(list1[0], list1[1])
    second_max = min(list1[0], list1[1])
    len_n = len(list1)
    for i in range(2, len_n):
        if list1[i] > max_num:
            second_max = max_num
            max_num = list1[i]
        elif second_max < list1[i] and max_num != list1[i]:
            second_max = list1[i]
        elif max_num == second_max and second_max != list1[i]:
            second_max = list1[i]
            print(f"second highest number is: {second_max}")
    return second_max

print(max_number(list1))

#
# Implement a functions fizz_buzz that receives an integer num and returns
# list of strings ret_val of length num, such that:
# ret_val[i] == "FizzBuzz" if i is divisible by 3 and 5.
# ret_val[i] == "Fizz" if i is divisible by 3.
# ret_val[i] == "Buzz" if i is divisible by 5.
# ret_val[i] == i (as a string) if none of the above conditions are true.
#

def fiz_buzz() -> list:
    num_user = int(input("please enter number: "))
    list_nums = []
    for i in range(1, num_user+1):
        if i % 3 == 0 and i % 5 == 0:
            list_nums.append('fizzbuzz')
            continue
        elif i % 3 == 0:
            list_nums.append("fizz")
            continue
        elif i % 5 == 0:
            list_nums.append("buzz")
            continue
        list_nums.append(i)
    return list_nums
print(fiz_buzz())


# Implement a function my_sqrt that receives a non-negative integer x, and returns the square root of x rounded down
# to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator like x ** 0.5 or math.sqrt()  in python.
# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
#
def my_sqrt(x: int) -> int:
    x_square = None
    while True:
        x = int(input("enter number: "))
        if x < 0:
            print("enter positive number please ")
            continue
        else:
            x_square = x ** (1/2)
            x_square_rounded = round(x_square)
            print(f"the square root of {x} is {x_square} and the rounded number is: {x_square_rounded}")
            break
    return x_square_rounded
print(my_sqrt(13))

