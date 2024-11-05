class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Predator(Animal):

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True



animal1 = Predator('Grampus')
animal2 = Mammal('Cow')
plant1 = Plant('Philodendron')
plant2 = Fruit('Peach')

print(animal1.name)
print(plant1.name)

print(animal1.alive, f'- {animal1.name} плавает')
print(animal2.fed, f'- {animal2.name} голодный')

animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive, f'- {animal1.name} самоуничтожился')
print(animal2.fed, f'- {animal2.name} наелась')