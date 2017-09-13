class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self, triangulo):
        return (triangulo.a+triangulo.b+triangulo.c)

    def tipo_lado(self, triangulo):
        if (triangulo.a==triangulo.b==triangulo.c):
            return ("equilátero")
        elif (triangulo.a==self.b or triangulo.b==triangulo.c or triangulo.a==triangulo.c):
            return ("isósceles")
        else:
            return ("escaleno")

    def retangulo(self, triangulo):
        if (triangulo.a>triangulo.b and triangulo.a>triangulo.c): # a é hipotenusa
            if ((triangulo.b**2) + (triangulo.c**2) ==(triangulo.a**2)): #Teorema de Pitágoras
                return True
            else:
                return False
        elif (triangulo.b>triangulo.a and triangulo.b>triangulo.c): # b é hipotenusa
            if ((triangulo.a**2) + (triangulo.c**2) == (triangulo.b**2)): #Teorema de Pitágoras
                return True
            else:
                return False
        elif (triangulo.c>triangulo.a and triangulo.c>triangulo.b): # c é hipotenusa
            if ((triangulo.a**2) + (triangulo.b**2) == (triangulo.c**2)): #Teorema de Pitágoras
                return True
            else:
                return False
        else:
            return False

    def semelhantes(self, triangulo):
        x = triangulo.a / self.a
        y = triangulo.b / self.b
        z = triangulo.c / self.c
        if (x==y and x==z):
            return True
        else:
            return False

def main():
    t1 = Triangulo(5, 4, 3)
    t2 = Triangulo(10, 8, 6)
    print ("Triângulo 1")
    print ("Lado a =", t1.a)
    print ("Lado b =", t1.b)
    print ("Lado a =", t1.c)
    print ("Perímetro =", t1.perimetro(t1))
    print ("Tipo do triângulo: ", t1.tipo_lado(t1))
    print ("É retângulo? ",t1.retangulo(t1))
    print ()
    print ("Triângulo 2")
    print ("Lado a =", t2.a)
    print ("Lado b =", t2.b)
    print ("Lado a =", t2.c)
    print ("Perímetro =", t2.perimetro(t2))
    print ("Tipo do triângulo: ", t2.tipo_lado(t2))
    print ("É retângulo? ",t2.retangulo(t2))
    print ()
    print ("Os triângulos 1 e 2 são semelhantes? ", t1.semelhantes(t2))

main()
