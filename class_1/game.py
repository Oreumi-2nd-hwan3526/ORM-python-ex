import random


class Player:
    def __init__(self,name,health,attack):
        self.name=name
        self.health=health
        self.attack=attack

class Game:
    def __init__(self):
        self.player=Player("A",100,10)
        self.enemy=Player("B",50,5)

        while self.player.health > 0 and self.enemy.health > 0:
            print(f"{self.player.name}'s turn")
            self.player_turn()

            print(f"{self.enemy.name}'s turn")
            self.enemy_turn()

        if self.player.health > 0:
            print("Victory")
        else:
            print("Lose")

    def player_turn(self):
        action=input("action? (attack/skill)")

        if action=="attack":
            attack_damage=random.randint(1,self.player.attack)
            self.attack(self.player.name,attack_damage)
            self.enemy.health-=attack_damage
            self.current_health(self.enemy.name,self.enemy.health)
        elif action=="skill":
            skill_damage=random.randint(1,self.player.attack+5)
            self.attack(self.player.name,skill_damage)
            self.enemy.health-=skill_damage
            self.current_health(self.enemy.name,self.enemy.health)
        else:
            print("wrong input")
            self.player_turn()

    def enemy_turn(self):
        enemy_attack_damage=random.randint(1,self.enemy.attack)
        self.attack(self.enemy.name,enemy_attack_damage)
        self.player.health-=enemy_attack_damage
        self.current_health(self.player.name,self.player.health)

    def attack(character_name,attack_damage):
        print(f"{character_name}'s attack, {attack_damage} damage to enemy")

    def current_health(character_name,remain_health):
        print(f"{character_name}'s health remains {remain_health} points")
