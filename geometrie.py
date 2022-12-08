#!/opt/homebrew/bin/python3 python3

from math import *
class carre:
	def __init__(self):
		self.cote = int(input("Entrez la longueur des côtés du carré : "))
	def perimetre(self):
		return self.cote *4
	def aire(self):
		return self.cote**2

carre = carre()
print(carre.perimetre())
print(carre.aire())

class rectangle:
    def __init__(self):
        self.longueure = int(input("Entrez la longueur du rectangle : "))
        self.largeur = int(input("Entrez la largeur du rectangle : "))

    def perimetre(self):
        return (self.longueure*2)+(self.largeur*2)

    def aire(self):
        return self.longueure*self.largeur


class cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        self.diametre = rayon*2


rectangle = rectangle()
print(rectangle.perimetre())
print(rectangle.aire())

class triangleEquilateral:
	def __init__(self):
		self.cote = int(input("Entrez la longueur des côtés du triangle équilatéral : "))
	def permimettre(self):
		return self.cote *3
	def aire(self):
		return (sqrt(3)/4)*(self.cote**2)

triangleE = triangleEquilateral()
print(triangleE.permimettre())
print(triangleE.aire())
=======
