class Calculadora:
    def __init__ (self, batteryMax: int):
        self.display: float = 0.00
        self.battery: int = 0
        self.batteryMax: int = batteryMax

    def __str__ (self):
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge (self, amount: int) -> None:
        self.battery += amount
        if self.battery >= self.batteryMax:
            self.battery = self.batteryMax

    def sum (self, number1: float, number2: float):
        numero1: float = 0.00
        numero2: float = 0.00
        if self.battery > 0:
            self.display = number1 + number2
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")

    def div (self, number3: float, number4: float):
        numero3: float = 0.00
        numero4: float = 0.00
        if self.battery > 0:
            if number3 == 0 or number4 == 0:
                print("fail: divisao por zero")
                self.battery -= 1
            else:
                self.display = number3 / number4
                self.battery -= 1
        else:
            print("fail: bateria insuficiente")
        

def main():
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)
        if args [0] == "end":
            break
        elif args[0] == "init":
            batteryMax = int(args[1])
            calculadora: Calculadora = Calculadora(batteryMax)
        elif args [0] == "show":   
            print (calculadora)
        elif args [0] == "charge":
            amount: int = int(args[1])
            calculadora.charge(amount)
        elif args[0] == "sum":
            number1: float = float(args[1])
            number2: float = float(args[2])
            calculadora.sum(number1, number2)
        elif args[0] == "div":
            number3: float = float(args[1])
            number4: float = float(args[2])
            calculadora.div(number3, number4)
        else:
            print("fail: comando invalido")

main()