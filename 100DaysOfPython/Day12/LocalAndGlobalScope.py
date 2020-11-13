enemies = 1 # global scope

def increase_enemies():
    enemies = 2 # local scope
    print(f"Enimies inside function {enemies} ")

increase_enemies()
print(f"Enimies outside function {enemies}")

enemies = ["zombie", "Alien", "skelton"]
game_level = 3

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # this is still global only in function it is local

# to change global variable use global keyword

enemies = 1 # global scope

def increase_enemies():
    global enemies
    enemies = 2 # local scope
    print(f"Enimies inside function {enemies} ")

increase_enemies()
print(f"Enimies outside function {enemies}")