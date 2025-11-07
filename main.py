from random import choice, shuffle

doors = {"Door1": "Goat", "Door2": "Goat", "Door3": "Car"}


def shuffle_doors(doors):
    """
    this function shuffles the values for simulate better
    """
    values = list(doors.values())
    shuffle(values)
    for key, value in zip(doors.keys(), values):
        doors[key] = value


def guess(doors):
    """
    this function dont changes the guess
    """
    doors = doors.copy()
    doors_list = list(doors.keys())
    guess = choice(doors_list)
    doors_list2 = doors_list.copy()
    doors_list2.remove(guess)
    shuffle(doors_list2)
    for door in doors_list2:
        if doors[door] != "Car":
            doors_list.remove(door)
            del doors[door]
            break

    if doors[guess] == "Car":
        return True

    return False


def changed_guess(doors):
    """
    this function changes the guess
    """
    doors = doors.copy()
    doors_list = list(doors.keys())
    guess = choice(doors_list)
    doors_list2 = doors_list.copy()
    doors_list2.remove(guess)
    shuffle(doors_list2)
    for door in doors_list2:
        if doors[door] != "Car":
            doors_list.remove(door)
            del doors[door]
            break

    final_guess = [d for d in doors.keys() if d != guess][0]

    if doors[final_guess] == "Car":
        return True

    return False


def monty_hall(doors, times):
    """
    this function calculates the likelihood
    """
    guess1_counter = 0
    guess2_counter = 0

    for time in range(times):
        shuffle_doors(doors)
        guess2 = changed_guess(doors)
        guess1 = guess(doors)

        if guess1:
            guess1_counter += 1
        if guess2:
            guess2_counter += 1

    guess1_probablibity = guess1_counter / times
    guess2_probablibity = guess2_counter / times
    print(
        f"the probablibity of first method (without changing the guess) is: {guess1_probablibity}"
    )
    print(
        f"the probablibity of second method (with changing the guess) is: {guess2_probablibity}"
    )


monty_hall(doors, 100_000)
