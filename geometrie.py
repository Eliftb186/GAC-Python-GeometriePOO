from math import *


# une classe carré
class carre:
    def __init__(self):
        self.cote = int(input("Entrez la longueur des côtés du carré : "))

    def perimetre(self):
        return self.cote * 4

    def aire(self):
        return self.cote**2


# carre = carre()
# print(carre.perimetre())
# print(carre.aire())


# une classe rectangle
class rectangle:
    def __init__(self):
        self.longueure = int(input("Entrez la longueur du rectangle : "))
        self.largeur = int(input("Entrez la largeur du rectangle : "))

    def perimetre(self):
        return (self.longueure*2)+(self.largeur*2)

    def aire(self):
        return self.longueure*self.largeur


# rectangle = rectangle()
# print(rectangle.perimetre())
# print(rectangle.aire())


# une classe cercle
class cercle:
    def __init__(self):
        self.rayon = int(input("Entrez le rayon du cercle : "))
        self.diametre = self.rayon*2

    def perimetre(self):
        return 2*pi*self.rayon

    def aire(self):
        return pi*(self.rayon**2)


# cercle = cercle()
# print(cercle.diametre)
# print(cercle.perimetre())
# print(cercle.aire())


# une classe triangle Equilateral
class triangleEquilateral:
    def __init__(self):
        self.cote = int(
            input("Entrez la longueur des côtés du triangle équilatéral : "))

    def permimettre(self):
        return self.cote * 3

    def aire(self):
        return (sqrt(3)/4)*(self.cote**2)


# triangleE = triangleEquilateral()
# print(triangleE.permimettre())
# print(triangleE.aire())

# une classe triangle rectangle
class triangleRectangle:
    def __init__(self):
        self.cote1 = int(input("Entrez la longueur du premier côté : "))
        self.cote2 = int(input("Entrez la longueur du deuxième côté : "))
        self.cote3 = int(input("Entrez la longueur du troisième côté : "))

    def perimetre(self):
        return self.cote1+self.cote2+self.cote3

    def aire(self):
        return (self.cote1*self.cote2)/2


# triangleRectangle = triangleRectangle()
# print(triangleRectangle.perimetre())
# print(triangleRectangle.aire())
