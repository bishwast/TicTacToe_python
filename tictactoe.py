""" 
tic tac toe board: This is a simple 2-Dimensional board. The Board is a list, which contains list of rows.
 
[
    [-, -, -],
    [-, -, -],
    [-, -, -]

]

Rows: 0, 1, 3
      2, 3, 4
      5, 6, 7
      here, each rows divided by 3 will give us the row from first, second and third. 
      As in first row, slots = 3, so 3/3 = 1
      As in second row, slows end at 6, so , 6/3 = 2
      in last row the slot starts at 7, 7/3 = 2.33, which is greater than the second row. This puts the row to third row automatically.

Columns: the remainder is the pattern. As,
first col remainder = 0 /3, remainder = 0
second col remainder = 1/3 = 0.33 which is less than 3 close to 1
third col remainder = 2/3 = 0.666, remainder of 2
In simple term, Applying modulus gives us 0, 1, and 2 for each columns slots, so we can divide teh columns as per this logic.

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

# Function to quit. no matter what case user types, func also converts the letter to a lower case.         
def quit(user_input):
    if user_input.lower() == "q": 
        print("Thank you for playing Tic tac toe")
        return True
    else:
        return False

# Func to check the user input
def check_input(user_input):
    # Check if user input is a number by calling the isnum() func. If not a number return False, else True
    if not isnum(user_input): 
        return False
    user_input = int(user_input)        ## Converting userinput into a integer
    # Check if the number is 1 through 9
    if not num_criteria(user_input):
        return False
    
# Check if user input is a number
def isnum(user_input):
        if not user_input.isnumeric():
            print("This is not a number!")
            return False
        else:
            return True

# Fun that checks if the number entered is from 1 - 9 our num_criteria
def num_criteria(user_input):
   if user_input >9 or user_input <1:
       print("This number does not meet the numeric criteria of 1 through 9!")
       return False
   else:
       return True

# Func to check if the slot is already taken in the board in the 2D Array list
def is_slotTaken(coordinates, board):
    row = coordinates[0]
    col = coordinates[1]
    if board[row][col] != "-":
        print("This position is already taken!")
        return True
    else:
        return False
    
    
# Func to get the coordinates of the 2D List. 
def coordinates(user_input):
    row = int(user_input / 3) 
    col = user_input
    if col > 2:
        col = int(col %3)
    return (row, col)




while True:
    # Re-print the board once the while loop is complete iterating.
    print_board(board)
    # input 'q' breaks the loop
    user_input = input("Please enter a position from 1 through 9 or enter \"q\" to quit the game: ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again.")
        continue    # Re run the loop from the begining. 
    # Array contains index starting from 0. Position 1 - 9, index for 9 is 10. 
    # So, subtracting 1 from user input gives us a correct index of a user input.
    user_input = int(user_input) - 1
    # Save coordinates as a value.
    coordinates = coordinates(user_input)
    # At 0th index, hard-coding it as 'x'
    board[0][0] = "x"
    if is_slotTaken(coordinates, board):
        print("Please try again!")
        continue    # Re run the loop from the begining. 
    
    
    
