# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
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
    
for i in range(0,6):
    jump()