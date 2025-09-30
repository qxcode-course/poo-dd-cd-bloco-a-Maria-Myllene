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
    def sum (self, number1: int, number2):
        numero1: int = 0
        numero2: int = 0
        if self.battery > 0:
            self.display = number1 + number2
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
            amount: int = int(args[1])
            calculadora.charge(amount)
            calculadora.sum()
        else:
            print("fail: comando invalido")

main()