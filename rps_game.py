import random

N_GAMES = 3


def main():
    row = 0
    human_win = 0
    ai_win = 0
    print_welcome()
    while row < N_GAMES:
        ai_move = get_ai_move()
        human_move = get_human_move()
        winner = get_winner(ai_move, human_move)

        # show move

        print('Your move is:', human_move)
        print('AI move is:', ai_move)

        # announce the winner of each row

        if ai_move != human_move:
            print('The winner is', get_winner(ai_move, human_move))

            # calculate the result and announce the final winner

            if winner == 'human':
                human_win += 1
                row += 1
                print('The score is now ', str(human_win), '-', str(ai_win))
                if human_win > ai_win and row == 3:
                    print('')
                    print('Congratulation! You beat the AI')
                    break
            if winner == 'AI':
                ai_win += 1
                row += 1
                print('The score is now ', str(human_win), '-', str(ai_win))
                if ai_win > human_win and row == 3:
                    print('')
                    print('The AI beat you. Try better next time.')
                    break
        # if tie then reset row

        else:
            print('It was a', get_winner(ai_move, human_move))
            row = 0


def print_welcome():
    print("Welcome to the RPS game! Here's how it works")
    print('Rock beats Scissors/Scissors beats Paper/Paper beats Rock, and the one who gets wins more row wins the game')
    print('Remember to type "Rock/Paper/Scissors" and nothing else')
    print("Now let's play 3 rows vs an AI: ")


def get_ai_move():

    # random ai move

    move_list = ['Rock', 'Paper', 'Scissors']
    move = random.choice(move_list)
    return move


def get_human_move():
    while True:
        human_move = input("Your move: ")
        if human_move == 'Rock' or human_move == 'Paper' or human_move == 'Scissors':
            return human_move
        else:
            print('Invalid move')


def get_winner(ai_move, human_move):
    if ai_move != human_move:
        if ai_move == 'Rock' and human_move == 'Paper':
            return 'human'
        elif ai_move == 'Rock' and human_move == 'Scissors':
            return 'AI'
        if ai_move == 'Paper' and human_move == 'Scissors':
            return 'human'
        elif ai_move == 'Paper' and human_move == 'Rock':
            return 'AI'
        if ai_move == 'Scissors' and human_move == 'Rock':
            return 'human'
        elif ai_move == 'Scissors' and human_move == 'Paper':
            return 'AI'
    else:
        return 'tie'


if __name__ == '__main__':
    main()



