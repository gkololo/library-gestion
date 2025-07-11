class Livre:
    nombre_total_livres = 0

    def __init__(self, titre: str, auteur: str, isbn: str):
        Livre.valider_isbn(isbn)   #appel à @staticmethod pour vérifier isbn
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True
        Livre.nombre_total_livres += 1  # fait appel à l'attrivut de classe depuis l'intérieur de la classe.


    @staticmethod
    def valider_isbn(isbn:str):
        if isbn.isdigit():              # test ISBN
            if len(isbn) in [10,13]:            #test ISBN entre 11 et 13
               return True
            else:
                print('Erreur de format de votre ISBN doit être compris en 10 et 13')
                raise ValueError
        else:
            print(' Erreur de format (lettres) de votre ISBN')
            raise ValueError

    @property
    def disponibilite(self):
        return 'Disponible' if self.disponible else 'Indisponible'

    def __str__(self):
        return f"{self.titre} de {self.auteur} : {self.isbn} \n STATUT : {self.disponibilite}"

    def emprunter(self):
        if self.disponible:
            self.disponible = False  # Changer le statut
            # Retourner True pour "succès" ?
            return f'vous empruntez {self.titre} de {self.auteur} : {self.isbn}'
        else:
            # Livre déjà emprunté
            # Retourner False ?
            return f'{self.titre} de {self.auteur} : {self.isbn} n\'est PAS disponible'


    def retourner(self):
        if not self.disponible:  # Si emprunté
            self.disponible = True
            # Retourner True
            return f'vous retournez {self.titre} de {self.auteur} : {self.isbn}'
        else:
            # Déjà disponible
            return f'{self.titre} de {self.auteur} : {self.isbn} n\'était PAS sorti'

    @classmethod
    def obtenir_nombre_total(cls):
    # Comment retourner le nombre total de livres ?
        return f'Nombre total de livres: {Livre.nombre_total_livres}'


# Usage :
livre_1 = Livre('Harry Potter', 'J.K. Rowling', '1234567891')
print(livre_1)  # Appelle automatiquement __str__
livre_2 = Livre('Harry Potter vol 2', 'J.K. Rowling', '1234567890')
print(livre_2)  # Appelle automatiquement __str__

print(Livre.obtenir_nombre_total)

# Usage :
""" livre_1 = Livre('Harry Potter', 'J.K. Rowling', '1234567890')  # ISBN-10
print(livre_1)  # Statut initial
print(livre_1.emprunter())  # Premier emprunt
print(livre_1)  # Vérifier le changement de statut
print(livre_1.emprunter())  # Tentative de re-emprunt
print(livre_1.retourner())  # Retour
print(livre_1)  # Vérifier le statut final """



