import turtle

screen = turtle.Screen() # Create the screen.
screen.setup(640, 640) # Set Window size.

###### TURTLE SHAPE, SPEED, PEN SIZE, COLOR ######
TTL = turtle.Turtle()
TTL.speed(0) # Set the turtle's speed. 1 is slow, 10 is fast; 0 is fastest.
TTL.color("brown") # Set the turtle's color.
TTL.pensize(1) # Set width of turtle drawing pen.

###### Position ######
TTL.penup() # Do not let the turtle draw while moving to position (0, 110)
TTL.setposition(0, -100)
TTL.pendown() # Enable the turtle to draw
TTL.hideturtle()
TTL.setheading(90)

###### DEFINE treeFractal FUNCTION ######
def treeFractal(TTL, recursionLevel, branchLength, branchReduction, angle):
    if recursionLevel == 0:
        TTL.fd(0)
    else:
        branchLength = branchLength - branchReduction
        TTL.forward(branchLength)
        TTL.left(angle)
        treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
        TTL.right(angle * 2)
        treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
        TTL.left(angle)
        TTL.backward(branchLength)

# Get the recursion level from the user
while True:
    try:
        # Prompt the user to enter the recursion level as an integer
        recursion_level = int(input("Enter the recursion level (an integer, recommended 1-10): "))       
        # Check if the entered level is within the valid range
        if recursion_level < 1 or recursion_level > 10:
            print("Please enter a number between 1 and 10.")
        else:
            break  # Exit the loop if a valid input is received
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Please enter a valid integer.")

# Call the treeFractal function with parameters
# TTL is the turtle object, recursion_level is the user-defined recursion depth,
# 45 is the initial branch length, 5 is the branch length reduction per recursion,
# and 25 is the angle by which the branches turn.
treeFractal(TTL, recursion_level, 45, 5, 25)

# Exit the screen when the user clicks on it
screen.exitonclick()
