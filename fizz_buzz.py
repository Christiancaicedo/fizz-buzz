def fizz_buzz(num):
    """Fizz buzz game that takes a number and determines if its "fizz", "buzz", or "fizz buzz".
    If the number is divisible by 3, the function will print "fizz".
    If the number is divisible by 5, the function will print "buzz".
    If the number is divisible by 3 & 5, the function will print "fizz buzz".

    Args:
        num: A given integer.
    """
    if num % 3 == 0 and num % 5 == 0:
        print("fizz buzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 2 == 0:
        print("fizz")
    else:
        print(None)
        


fizz_buzz(9)