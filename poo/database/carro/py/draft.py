class Carro:
    def __init__ (self, passager: int, gas: int, km: int):
        self.passager: int = 0
        self.gas: int = 0
        self.km: int = 0
    
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
        else:
            print("fail: comando invalido")
 
main()