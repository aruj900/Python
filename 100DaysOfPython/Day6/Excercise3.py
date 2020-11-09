#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
def jump():
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
    while front_is_clear():
        move()
    if wall_in_front():
        jump()