import random
import os
import time


def clear():
    os.system('clear')


def assign_doors(outcomes, doors):
    random.shuffle(outcomes)
    random.shuffle(doors)
    return [list(a) for a in zip(outcomes, doors)]


def play_again(wins_and_losses):
    play_again = input("\nPlay again? Y/n ").lower()
    if play_again != 'n':
        clear()
        game_loop(wins_and_losses)
    else:
        print("\n\nCatch ya later!\n\n\n\n")
        time.sleep(1.5)
        clear()
        exit()


def game_loop(wins_and_losses):

    playing_field = []
    pool = []
    outcomes = ['goat', 'goat', 'prize']
    doors = ['1', '2', '3']
    print("\t\tWelcome to the Monty (Python!) Hall Simulation\n")
    pick = random.choice('123')
    for door in assign_doors(outcomes, doors):
        if pick != door[1] and door[0] == 'goat' and len(pool) == 0:
            pool.append(door)
        else:
            playing_field.append(door)
    print(pool)
    print(playing_field)

    print("\nThe host reveals {}".format(pool))
    print("\nThere are 2 doors left!")

    for door in playing_field:
        if door[1] == pick:
            if door[0] == 'prize':
                print("{} YOU WIN!\n".format(door))
                wins_and_losses.append('1')
                break
            elif door[0] == 'goat':
                print("{} Enjoy your goat.\n".format(door))
                wins_and_losses.append('2')
                break


def main():
    clear()
    wins_and_losses = []
    game_loop(wins_and_losses)
    while len(wins_and_losses) < 999:
        game_loop(wins_and_losses)
    print("{} wins".format(wins_and_losses.count('1')))
    print("{} losses".format(wins_and_losses.count('2')))
    # print(wins_and_losses)


if __name__ == '__main__':
    main()
