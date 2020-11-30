#Ejercicio 1: Python --- Iñaki

class Coordenada_Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Forma(Coordenada_Punto):
    def __init__(self,x, y, color, nombre):
        super().__init__(x, y)
        self.color=color
        self.nombre=nombre
    def print(self):
        print("Coordenada del punto x " + str(self.x) + " Coordenada del punto y " + str(self.y) + " Color de la forma -> " + self.color +" Nombre de la forma -> "+self.nombre)
    def obtener(self):
        return self.nombre,self.punto.x, self.punto.y
    def cambiarForma(self,x,y):
        self.x=x
        self.y=y

Forma1 = Forma( 6, 12,"Azul","Triangulo")
Forma1.print()


class Rectangulo(Forma):
    def __init__(self, x, y, color, nombre, Mayorlado, Menorlado):
        super().__init__(x, y, color,nombre)
        self.Menorlado=Menorlado
        self.Mayorlado=Mayorlado
    def Area(self):
        area=self.Menorlado*self.Mayorlado
        print("El area es igual a: "+str(area))
    def perimetro(self):
        perimetro=2*self.Menorlado+2*self.Mayorlado
        print("Perimetro: "+str(perimetro))

Rectangulo1=Rectangulo(2, 8, "Amarillo", "Rectangulo", 13, 10)
Rectangulo1.print()

class Elipse(Forma):
    def __init__(self, x, y, color, nombre, RadioMayor, RadioMenor):
        super().__init__(x,y,color,nombre)
        self.RadioMayor=RadioMayor
        self.RadioMenor=RadioMenor
    def areaElipse(self):
        area=math.pi*(self.RadioMayor*self.RadioMenor)
        print("Area de Elipse: "+str(area))

Elipse1=Elipse(3,7,"Amarillo","Elipse", 7,4)
Elipse1.print()


class Cuadrado(Rectangulo):
    def __init__(self,x,y,color,nombre, Mayorlado, Menorlado):
        super().__init__(x,y, color, nombre, Mayorlado, Menorlado)
    def print(self):
        super().print()

class Circulo(Elipse):
    def __init__(self, x, y, color, nombre, RadioMayor, RadioMenor):
        super().__init__(x,y, color,nombre,RadioMayor, RadioMenor)
    def print(self):
        super().print()

ImprRectangulo=Rectangulo(9, 1, "Morado", "Rectangulo", 8, 2)
ImprElipse=Elipse(2,9,"Blanco","Elipse", 6,10)
ImprCuadrado=Cuadrado(0,7,"Verde","Cuadrado",9,5)
ImprCirculo=Circulo(2,3,"Amarillo","Circulo",4,1)

tupla=(ImprRectangulo,ImprElipse,ImprCuadrado,ImprCirculo)
for Forma in tupla:
    print(Forma.print())