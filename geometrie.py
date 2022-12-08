#!/opt/homebrew/bin/python3 python3

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
	
rectangle = rectangle()
print(rectangle.perimetre())
print(rectangle.aire())