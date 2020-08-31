"""
kwargs are used to pass in named arguments to a function at runtime.
These are passed in the form of a dictionary.
Since dictionaries in python are mutable, you can manipulate the dictionary
"""

"""
Note the ** operator -> it is the unpacking operator to unpack dictionaries.
While * operator is used to unpack the Python iterables.
"""

def get_address(**kwargs): # the * is the unpacking operator
    address = ""
    
    # we can even add new keys
    kwargs["zip"] = "10292"

    # if we don't use the values() method we'll be iterating over the keys instead
    for component in kwargs.values():
        address += component
    return address


if __name__ == "__main__":
    # 22 Baker Street,London,England,10292
    print(get_address(street="22 Baker Street,", city="London,", country="England,"))
