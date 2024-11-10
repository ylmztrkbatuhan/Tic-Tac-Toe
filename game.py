from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print("***********************************")
        print(" Welcome to TicTacToeGame ")
        print("***********************************")


        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        # Ask the user if he/she would like to
        # #play round
        while True: # GAME
            #Get move, check tie, check game over

            while True: #ROUND

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_tie():
                    print("Its a tie! Try again.")
                elif board.check_is_game_over(player, player_move):
                    print("Awesome. You won the game!")
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("Ooops...The computer won . Try again")
                        break
            play_again = input("Would you like to play again? Enter X for YES and O for NO").upper()

            if play_again == "O":
                print("Bye! Come back soon")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("Your inpu was not valid but i will assume that you want to play again.")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("****************")
        print("  NEW ROUND  ")
        print("****************")
        board.reset_board()
        board.print_board()

