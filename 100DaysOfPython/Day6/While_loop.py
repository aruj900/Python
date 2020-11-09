def jump():
    move()
    turn_left()
    move()
    turnright()
    move()
    turnright()
    move()
    turn_left()
def turnright():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    jump()