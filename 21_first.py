import random


def game(players):
    total = 0
    p1 = "player1"

    if players == 2:
        p2 = "player2"
    elif players == 1:
        p2 = "bot"
        diff = int(input("bot difficulty(1-10)?:"))

    turn = p1
    while (total < 21):
        print("{0}'s turn".format(turn))
        i = 0
        if players == 1 and turn == p2:
            i = bot(total, diff)
        else:
            try:
                i = int(input("enter a no between 1 and 3 inclusive:"))
            except:
                print("enter a valid int")

        if i > 3 or i < 1 or total+i > 21:
            print("invalid input")
        else:
            total += i
            if turn == p1:
                turn = p2

            else:
                turn = p1

        print("total={0}\n".format(total))

    if turn == p1:
        turn = p2
    else:
        turn = p1
    print("{0} wins".format(turn))


def bot(total, diff):
    keystone_values = [1, 5, 9, 13, 17, 21]
    a = random.randint(1, 10)
    i = 0
    if a <= diff:
        while total+i not in keystone_values:
            i += 1
    else:
        i = random.randint(1, 3)
        if i+total > 21:
            i = 21-total

    print("bot picked={0}".format(i))
    return i


p = int(input("no of players(1/2)?:"))
game(p)
