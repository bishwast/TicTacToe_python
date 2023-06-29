""" 
tic tac toe board: This is a simple 2-Dimensional board. The Board is a list, which contains list of rows.
[
    [-, -, -],
    [-, -, -],
    [-, -, -]

]

user_input : Something from 1 to 9. If the input is not within 1-9 then try again.

Check if the user input is already taken. 
If not add the input to the board
Check if the user won: checking rows, columns, and diagonals
Toggle between users once their move is successful.

logic: Have a loop running when the game starts, unless a user breaks out of the loop.

Inputs:
    x, o => For players
    q => Breaks out of the game or the Loop
"""
# list of board
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Print the Tic tac toe board to the terminal for the user.
# To print the board list, first iterate through each rows, then on wach rows iterate through each Slots.
def print_board(board):
    for row in board:       # iterate through the row
        for slot in row:    # iterate through slot elements in each row
            print(f"{slot} ", end="")     # by default print() adds a new line 'end="\n"', leaving " " blank removes a line
        print()                     # Adding a new line once the iteration is complete in one row  


print_board(board)

# Function to quit. no matter what case user types, func also converts the letter to a lower case.         
def quit(user_input):
    if user_input.lower() == "q": 
        print("Thank you for playing Tic tac toe")
        return True
    else:
        return False
        
while True:
    # input 'q' breaks the loop
    user_input = input("Please enter a position from 1 through 9 or enter \"q\" to quit the game: ")
    if quit(user_input):
        break