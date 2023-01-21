# # You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
# # one of the numbers in
# # s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# # You are given an integer array nums representing the data status of this set after the error.
# # Find the number that occurs twice and the number that is missing and return them in the form of an array.

#     x = len(nums) * (len(nums) + 1) // 2
#     y = sum(nums)
#     z = sum(set(nums))
#
#     return [y - z, x - z]
# import doctest
# from collections import Counter
# from itertools import count
#
#
# def findErrorNums(nums: list[int]) -> list[int]:
#     counter = Counter(nums)
#     result = []
#     # Find the number that appears twice in the list
#     for i in counter:
#         if counter[i] == 2:
#             result.append(i)
#     # Find the missing number
#     for i in range(1, len(nums) + 1):
#         if i not in counter:
#             result.append(i)
#     return result
#
#
# print(findErrorNums([1, 2, 2, 4]))
#
#
# def countBinarySubstrings(s):
#     counter = 0
#     prev_count = 0
#     curr_count = 0
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             curr_count += 1
#         else:
#             if prev_count and curr_count:
#                 counter += min(prev_count, curr_count)
#             prev_count = curr_count
#             curr_count = 1
#     return counter
#
#
# def longestCommonPrefix(strs) -> str:
#     pre = strs[0]
#     for i in strs:
#         while not i.startswith(pre):
#             pre = pre[:-1]
#
#     return pre
#
# print(longestCommonPrefix(["cartoon", "cartrtrt", "carwerwe"]))


# def missing_number(nums):
#     # nums = [1,2,2,4] - > [2, 3]
#
#     n = sum(nums)
#     m = sum(set(nums))
#     y = len(nums) * (len(nums) + 1) // 2
#
#     duplicated_num = n - m
#     missing_num = y - m
#     return [duplicated_num, missing_num]
#
#
# print(missing_number([1, 2, 2, 4]))

def checkRecord(s: str) -> bool:
    if s.count('A') < 2:
        for i in range(len(s)):
            if s[i] == 'L' and s[i + 1] == 'L' and s[i + 2] == 'L':
                return False
    else:
        return True


print(checkRecord('PPALLP'))
