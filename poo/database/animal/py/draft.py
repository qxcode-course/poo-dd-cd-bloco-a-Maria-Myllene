class Animal:
    def __init__ (self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __str__ (self):
        return f"{self.species}:{self.age}:{self.sound}"
    
    def grow (self, quantidade: int) -> None:
        self.age += quantidade
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            self.age = 4
    
    def noise (self):
        if self.age == 0:
            print("---")
        elif self.age >= 4:
            print("RIP")
        else:
            print(self.sound)

def main ():
    animal: Animal = Animal("", "")
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)
        if args[0] == "end":
            break
        elif args [0] == "init":
            species = args [1]
            sound = args [2]
            animal = Animal (species, sound)
        elif args [0] == "show":
            print(animal)
        elif args [0] == "grow":
            amount: int = int(args[1])
            animal.grow(amount)
        elif args[0] == "noise":
            animal.noise()
        else:
            print("fail: comando invalido")

main ()