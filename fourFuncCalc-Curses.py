import curses

# Initializing Curses
screen = curses.initscr()

# Options area, only one for this and that's starting colors
curses.start_color()

# Setting a variable to True for the while loop to loop through the menu until user quits
bool = True
while bool:
    # Ensuring the screen is cleared before loading the menu
    screen.clear()
    # The Menu portion, probably could be condensed into one line but I prefer it like this until more options are added
    screen.addstr("4 Function Calculator in Curses\n", curses.A_BOLD)
    screen.addstr("1. Add\n")
    screen.addstr("2. Subtract\n")
    screen.addstr("3. Multiply\n")
    screen.addstr("4. Divide\n")
    screen.addstr("5. Exit\n")
    screen.addstr("Enter your choice: ")
    input = screen.getstr()

    screen.clear()

    # Try-Except clause to prevent user from entering letters (invalid number entries will be addressed later)
    try:
        # Simple If statement for the calculator

        # The Addition portion
        if int(bytes.decode(input)) == 1:
            screen.addstr("Enter your first number: ")
            num1 = screen.getstr()
            screen.addstr("Enter your second number: ")
            num2 = screen.getstr()

            screen.clear()

            sum = int(bytes.decode(num1)) + int(bytes.decode(num2))
            screen.addstr("Your sum is: ")
            screen.addstr(f"{sum}\n", curses.A_UNDERLINE)

        # The Subtraction portion
        elif int(bytes.decode(input)) == 2:
            screen.addstr("Enter your first number: ")
            num1 = screen.getstr()
            screen.addstr("Enter your second number: ")
            num2 = screen.getstr()

            screen.clear()

            difference = int(bytes.decode(num1)) - int(bytes.decode(num2))
            screen.addstr("Your difference is: ")
            screen.addstr(f"{difference}\n", curses.A_UNDERLINE)

        # Multiplication portion
        elif int(bytes.decode(input)) == 3:
            screen.addstr("Enter your first number: ")
            num1 = screen.getstr()
            screen.addstr("Enter your second number: ")
            num2 = screen.getstr()

            screen.clear()

            product = int(bytes.decode(num1)) * int(bytes.decode(num2))
            screen.addstr("Your product is: ")
            screen.addstr(f"{product}\n", curses.A_UNDERLINE)

        # Division portion
        elif int(bytes.decode(input)) == 4:
            screen.addstr("Enter your first number: ")
            num1 = screen.getstr()
            screen.addstr("Enter your second number: ")
            num2 = screen.getstr()

            screen.clear()

            quotient = int(bytes.decode(num1)) / int(bytes.decode(num2))
            screen.addstr("Your quotient is: ")
            screen.addstr(f"{quotient}\n", curses.A_UNDERLINE)

        # The exit handler
        elif int(bytes.decode(input)) == 5:
            bool = False
            curses.endwin()

        # Here is where we check to see if the user input a valid number
        elif int(bytes.decode(input)) != [1, 2, 3, 4, 5]:  # Probably a better way to compare the values
            screen.addstr("Error: Invalid Input\n", curses.A_STANDOUT)
            screen.addstr("Did you input a number within 1-5?\n")
            screen.addstr("Press any key to go back to the menu...")
            screen.refresh()

            c = screen.getch()
    except ValueError as e:
        screen.addstr(f"Error: {e}\n", curses.A_STANDOUT)
        screen.addstr("(In English: You input an invalid option)\n")  # Added this so in case the user isn't a programmer, they could read the error
        screen.addstr("Did you input a number within 1-5?\n")
        screen.addstr("Press any key to go back to the menu...")
        screen.refresh()

        c = screen.getch()

    screen.refresh()
