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
    elif player_guess == 'next':
        exit
    else:
        return print("Sorry, that was the wrong answer. It is the next players turn")


for i in range(1, 101):
        print(i)
        player_guess = input("Enter if the number is either 'fizz' or 'buzz'. If the number is neither 'fizz' nor 'buzz', type 'next': ")
        if player_guess == "fizz buzz":
            if fizz_buzz(i) == "fizz buzz":
                print("Correct! You win!")
                break
        elif player_guess == "fizz":
            if fizz_buzz(i) == "fizz":
                print("Correct! Guess again.")
        elif player_guess == "buzz":
            if fizz_buzz(i) == 'buzz':
                print("Correct! Guess again.")
        elif player_guess == 'next':
            if fizz_buzz(i) != 'fizz' or 'buzz':
                print("Correct! Guess again")
        else:
            player_guess = input("That is not an acceptable input, please try again: ")