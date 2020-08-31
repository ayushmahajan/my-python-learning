"""
args are used to pass in multiple arguments to a function at runtime.
"""

"""
Traditional way of passing multiple arguments is via passing them in a list.
But the problem with the Traditional way is that we need to store the
values in a list. And for that sole purpose we need to create a list.
"""

def sum_of_nums(nums):
    total = 0
    for num in nums:
        total += num
    return total


"""
Using args. There are two changes in the traditional approach.
1. We pass *args(we can use any name instead of args) as the argument to the function.
2. When we call sum_of_nums_using_args, we don't pass a list of numbers rather
   we simply pass in a tuple.

So, we need to remember that whenever we pass multiple arguments using *args
those are passed in the form of a tuple. Since tuples are immutable in python,
we cannot manipulate them inside our function.
"""

def sum_of_nums_using_args(*args): # the * is the unpacking operator
    total = 0
    for num in args:
        total += num
    return total


if __name__ == "__main__":
    list_of_nums = [5, 2, 3]
    print(sum_of_nums(list_of_nums)) # 10
    print(sum_of_nums_using_args(5, 2, 4)) # 11
