class Carro:
    def __init__ (self, passager: int, gas: int, km: int):
        self.passager: int = 0
        self.gas: int = gas
        self.km: int = 0
        self.gasMax: int = 100
    
    def __str__ (self):
        return f"pass: {self.passager}, gas: {self.gas}, km: {self.km}"
    
    def enter (self):
        self.passager += 1
        if self.passager > 2:
            print("fail: limite de pessoas atingido")
            self.passager = 2

    def leave (self):
        self.passager -= 1
        if self.passager < 0:
            print("fail: nao ha ninguem no carro")
            self.passager = 0
    
    def fuel (self, increment: int):
        if increment > self.gasMax:
            self.gas = self.gasMax
        else:
            self.gas += increment
     
    def drive (self, distance: int):
        if self.passager == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        elif distance > self.gas:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
        else:
            self.km += distance
            self.gas = self.gas - self.km

def main ():
    carro: Carro = Carro(0, 0, 0)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break
        elif args [0] == "show":
            print(carro)
        elif args [0] == "enter":
            carro.enter()
        elif args [0] == "leave":
            carro.leave()
        elif args [0] == "fuel":
            increment: int = int(args[1])
            carro.fuel(increment)
        elif args [0] == "drive":
            distance: int = int(args[1])
            carro.drive(distance)
        else:
            print("fail: comando invalido")
 
main()