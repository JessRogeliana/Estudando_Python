def main():
    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(4, 6, 10)
    print(t1.semelhantes(t2))

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 

    def semelhantes(self, triangulo):
        t_self = [self.a, self.b, self.c]
        t_parametro = [triangulo.a, triangulo.b, triangulo.c]
        t_self.sort()
        t_parametro.sort()
        if ((t_self[0] // t_parametro[0]) == (t_self[1] // t_parametro[1]) and (t_self[1] // t_parametro[1]) == (t_self[2] // t_parametro[2])):
            return True
        else:
            return False 

#        for i in range(len(t_self)):
#            if int(t_self[i]) // int(t_parametro[i]):
#                return True
#            else:
#                return False 


main()        