def main():
    t = Triangulo(1,1,1)
    print(t.a)
    print(t.b)
    print(t.c)
    print(t.perimetro())

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        soma = self.a + self.b + self.c 
        return soma 

#t = Triangulo(1,1,1) 

main()