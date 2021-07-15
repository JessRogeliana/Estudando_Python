def main():
    t = Triangulo(1, 3, 5)
    u = Triangulo(3, 4, 5)
    print(t.retangulo())
    print(u.retangulo())

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 

    def retangulo(self):
        if ((self.a**2) == (self.b**2) + (self.c**2)) or ((self.b**2) == (self.a**2) + (self.c**2)) or ((self.c**2) == (self.a**2) + (self.b**2)):
            return True
        else:
            return False 
main()        