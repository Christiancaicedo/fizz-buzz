def fizz_buzz(num: int) -> str:
    """Play Fizz buzz
 
    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if num % 3 == 0 and num % 5 == 0:
        return("fizz buzz")
    elif num % 5 == 0:
        return("buzz")
    elif num % 3 == 0:
        return("fizz")
    else:
        return str(num)

input("Play Fizz Buzz.   Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print(f"You lose, the correct answer was {correct_answer}")
        break
    else:
        print(f"Well done, you reached {next_number}")