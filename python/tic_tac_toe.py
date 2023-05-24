import random

def display_board(board):
# The function accepts one parameter containing the board's current status
# and prints it out to the console.
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i * 3 + j + 1], end=" | ")
            print("\n---------")
        
def enter_move(board):
# The function accepts the board's current status, asks the user about their move, 
# checks the input, and updates the board according to the user's decision.
    while True:
        user_move = input("Enter your move (1-9): ")
        if user_move.isdigit() and int(user_move) in range(1, 10) and board[int(user_move)] == " ":
            board[int(user_move)] == "0"
            break
        else:
            print("Invalid move. Please try again!")

def make_list_of_free_fields(board):
# The function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(1, 10):
        if board[i] == " ":
            free_fields.append(i)
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game.
    # Returns True if the specified sign wins, False otherwise.
    # check_rows
    for i in range(1, 10, 3):
        if board[i] == board[i + 1] == board[i + 2] == sign:
            return True
        
    # check columns
    for i in range(1, 4):
        if board[i] + board[i + 3] + board[i + 6] == sign:
            return True
    
    # check diagonals
    if board[1] == board[5] == board[9] == sign:
        return True
    if board[3] == board[5] == board[7] == sign:
        return True
    
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    computer_move = random.choice(board)
    board[computer_move] = "X"

def main():
    # Initialize the board
    board = [" "] * 10
    board[5] = "X" # computer first move

    # Game loop
    while True:
        display_board(board)
        enter_move(board)

        if victory_for(board, "O"):
            display_board(board)
            print("You Win!")
            break
        elif len(make_list_of_free_fields(board)) == 0:
            display_board(board)
            print("It's a Tie!")
            break

        draw_move(board)

        if victory_for(board, "X"):
            display_board(board)
            print("Computer Wins!")
            break
        elif len(make_list_of_free_fields(board)):
            display_board(board)
            print("It's a Tie!")
            break

if __name__ == "__main__":
    main()
