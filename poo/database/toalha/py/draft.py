class Towel:
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness = 0
    def __str__ (self):
        return f"color: {self.color}, tam: {self.size}, umi: {self.wetness}"

towel = Towel("green", "G") # A variável towel referencia Towel, que é um objeto
toalha = Towel("red", "P")

print (towel.color)
towel.color = "white"
print (towel.color)
print (towel.size)
print (towel.wetness)

print(towel)