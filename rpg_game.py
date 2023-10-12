import random

# Definition of the Character class that represents characters, monsters, and heroes.
class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def is_alive(self):
        return self.health > 0
    
    def attack_target(self, target):
        defense = random.randint(0, self.defense)
        damage = random.randint(0, self.attack)
        if damage > defense:
            print(f'{self.name} attacca {target.name} e infligge {damage} danni!')
            target.take_damage(damage)
        else:
            print(f'{self.name} attacca {target.name} ha parato i danni!')

# Definition of the Player class that inherits from the Character class.
class Player(Character):
    def __init__(self, name, health, attack, defense, magic_power):
        super().__init__(name, health, attack, defense)
        self.magic_power = magic_power

    def cast_spell(self, target):
        if self.magic_power > 0:
            damage = random.randint(0, self.magic_power)
            print(f"{self.name} usa la magia contro {target.name} e infligge {damage} danni!")
            target.take_damage(damage)
            self.magic_power -= 1
        else:
            print(f"{self.name} ha esaurito la magia!")

# Definition of the Monster class that inherits from the Character class.
class Monster(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)

# Main function to handle the combat between the player and the monster.
def main(player, monster):
    while player.is_alive() and monster.is_alive():
        if monster.is_alive():
            monster.attack_target(player)
        if player.is_alive():
            action = input("Vuoi attaccare (A) o lanciare un incantesimo (M)? ").upper()
            if action == 'A':
                player.attack_target(monster)
            elif action == 'M':
                player.cast_spell(monster)
            else:
                print("Azione non valida. Scegli A o M.")

    if player.is_alive():
        print(f"{player.name} ha sconfitto {monster.name}!")
    else:
        print(f"{monster.name} ha sconfitto {player.name}. Game Over!")

# Main block to start the game.
if __name__ == "__main__":
    player = Player("Eroe", 100, 20, 10, 10)
    monster = Monster("Orco", 100, 20, 10)
    main(player, monster)



