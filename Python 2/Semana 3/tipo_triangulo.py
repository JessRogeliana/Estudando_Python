def main():
    t = Triangulo(4,4,4)
    u = Triangulo(3,4,5)
    print(t.tipo_lado())
    print(u.tipo_lado())

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if (self.a == self.b) and (self.a == self.c) and (self.b == self.c):
            return "equilátero" 
        elif (self.a != self.b) and (self.a != self.c) and (self.b != self.c):
            return "escaleno"
        else:
            return "isósceles"

main()