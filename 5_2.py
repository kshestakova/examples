"""
У нас есть эльфы, орки и гоблины. 
Возможно, у них есть общий предок - существо, у которого есть имя, сила, здоровье. 
Эльфы метко стреляют.
Орки бьют рубилом. И громко кричат. 
Гоблины могут драться копьями или палицами.
 
Нам нужно собрать армию для двух игроков: сгенерировать эльфов, орков и гоблинов случайным образом. 
А потом заставить этих игроков в цикле драться между собой. 
На каждом ходе у игрока выбирается один солдат из армии. 
Атака отнимает определенное количество жизней. В конце у кого остались живые солдаты, тот и победил. 
"""

from random import randint

class Creature:
    def __init__(self, name, power, health):
        # переменная функции (не класса!), чтобы различать существ
        initnumber = randint(0, 10000)
        print("Creature", initnumber, "initialization")
        self.name = name + str(initnumber)
        self.power = power
        self.health = health
    
    def show(self):
        print(self.name, self.power, self.health)
        
    def beat(self, creature):
        pass
        
    def isAlive(self):
        return self.health > 0.01 # чтобы существа с десятыми долями здоровья умирали и цикл не был бесконечным
        
class Elf(Creature):
    def __init__(self, name, power, health, accuracy):
        print("Elf initialization")
        super().__init__(name, power, health)
        self.accuracy = accuracy
        
    def beat(self, creature):
            creature.health -= self.power * self.accuracy / 20

class Orc(Creature):
    def __init__(self, name, power, health, voice):
        print("Orc initialization")
        super().__init__(name, power, health)
        self.voice = voice
        
    def scream(self):
            print(self.voice * 5)
            
    def beat(self, creature):
        self.scream()
        creature.health -= self.power / 2
        
class Goblin(Creature):
    def __init__(self, name, power, health):
        print("Goblin initialization")
        super().__init__(name, power, health)
        
    def beatMace(self, creature):
        creature.health -= self.power / 5
        if creature.power > 1:
            creature.power -= 2
        else:
            creature.power = 0
        
    # добавила выбор функции для атаки - обычный удар палицей или особый - копьем
    def beat(self, creature):
        if randint(0, 2):
            self.beatMace(creature)
        else:
            creature.health -= self.power / 2
            
    # переопределим функцию: живой гоблин должен иметь не только жизнь > 0, но и силу > 0     
    def isAlive(self):
        return super().isAlive() and self.power > 0
    
class Player:
    def __init__(self, name):
        self.name = name
        self.army = []
        
    def show(self):
        print("Number of soliders:", len(self.army))
        
    def delete(self, index):
        self.army.pop(index)
        
player1 = Player("First")
player2 = Player("Second")

def generateArmy():
    result = []
    for i in range(10):
        choice = randint(0, 3)
        if choice == 0:
            result.append(Elf("elf", randint(0, 15), randint(0, 150), randint(0, 20)))
        elif choice == 1:
            result.append(Orc("orc", randint(0, 30), randint(0, 80), "AGGHRH"))
        else: 
            result.append(Goblin("goblin", randint(0, 20), randint(0, 100)))
            
    return result
        
player1.army = generateArmy()
player2.army = generateArmy()

def fight(creature1, creature2):
    creature1.show()
    creature2.show()
    
    creature1.beat(creature2)
    if creature2.isAlive():
        creature2.beat(creature1)

# счетчик раундов сражений
round = 1

while len(player1.army) and len(player2.army):
    # форматированный вывод: f перед строкой, в фигурных скобках - имена переменных
    print(f"Round {round}. {player1.name} creatures: {len(player1.army)}. {player2.name} creatures: {len(player2.army)}")
    fight(player1.army[0], player2.army[0])
    round += 1
    if not player1.army[0].isAlive():
        player1.delete(0)
    if not player2.army[0].isAlive():
        player2.delete(0)
    
    if len(player1.army) > 0 and len(player2.army) <= 0:
        print(f"{player1.name} win")
        break
    elif len(player1.army) <= 0 and len(player2.army) > 0:
        print(f"{player2.name} win")
        break
    