class Animal:
    def __init__ (self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0
    def __str__ (self):
        return f"{self.species}:{self.age}:{self.sound}"
    def grow (self):
        if self.species >= 4:
            self.species = 4
            print(f"warning: {self.species} morreu")
    def age (self, quantidade: int) -> None:
        self.age += quantidade

def main ():
    animal: Animal = Animal("", "")
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args [0] == "init":
            species = args [1]
            sound = args [2]
            animal = Animal (species, sound)
        elif args [0] == "grow":
            animal.grow()
        elif args [0] == "show":
            print(animal)
        else:
            print("fail: comando invalido")

main ()