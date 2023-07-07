import random

player_name="A"
player_health=100
player_attack=10

enemy_name="B"
enemy_health=50
enemy_attack=5

def player_turn():
    global enemy_health

    action=input("action? (attack/skill)")

    if action=="attack":
        attack_damage=random.randint(1,player_attack)
        attack(player_name,attack_damage)
        enemy_health-=attack_damage
        current_health(enemy_name,enemy_health)
    elif action=="skill":
        skill_damage=random.randint(1,player_attack+5)
        attack(player_name,attack_damage)
        enemy_health-=attack_damage
        current_health(enemy_name,enemy_health)
    else:
        print("wrong input")
        player_turn()

def enemy_turn():
    global player_health
    enemy_attack_damage=random.randint(1,enemy_attack)
    attack(enemy_name,enemy_attack_damage)
    player_health-=enemy_attack_damage
    current_health(player_name,player_health)

def attack(character_name,attack_damage):
    print(f"{character_name}'s attack, {attack_damage} damage to enemy")

def current_health(character_name,remain_health):
    print(f"{character_name}'s health remains {remain_health} points")

while player_health > 0 and enemy_health > 0:
    print(f"{player_name}'s turn")
    player_turn()

    print(f"{enemy_name}'s turn")
    enemy_turn()

if player_health > 0:
    print("Victory")
else:
    print("Lose")