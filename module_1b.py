class Livre:
    # ATTRIBUT DE CLASSE (partagé par toutes les instances)
    nombre_total_livres = 0

    def __init__(self, titre: str, auteur: str, isbn: str):
        # VALIDATION avec méthode statique
        Livre.valider_isbn(isbn)

        # ATTRIBUTS D'INSTANCE
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True

        # INCRÉMENTER l'attribut de classe
        Livre.nombre_total_livres += 1

    @property
    def disponibilite(self):
        """Propriété calculée - lecture seule"""
        return 'Disponible' if self.disponible else 'Indisponible'

    def __str__(self):
        """Représentation string de l'objet"""
        return f"{self.titre} de {self.auteur} : {self.isbn} \n STATUT : {self.disponibilite}"

    def emprunter(self):
        """Méthode d'instance - change l'état"""
        if self.disponible:
            self.disponible = False
            return f'Vous empruntez {self.titre}'
        else:
            return f'{self.titre} n\'est PAS disponible'

    def retourner(self):
        """Méthode d'instance - change l'état"""
        if not self.disponible:
            self.disponible = True
            return f'Vous retournez {self.titre}'
        else:
            return f'{self.titre} n\'était PAS emprunté'

    @staticmethod
    def valider_isbn(isbn: str):
        """Méthode statique - fonction utilitaire"""
        if isbn.isdigit():
            if len(isbn) in [10, 13]:
                return True
            else:
                print('Erreur : ISBN doit avoir 10 ou 13 chiffres')
                raise ValueError
        else:
            print('Erreur : ISBN doit contenir uniquement des chiffres')
            raise ValueError

    @classmethod
    def obtenir_nombre_total(cls):
        """Méthode de classe - accède aux attributs de classe"""
        return f'Nombre total de livres: {cls.nombre_total_livres}'


# Usage :
livre_1 = Livre('Harry Potter', 'J.K. Rowling', '1234567891')
print(livre_1)  # Appelle automatiquement __str__
livre_2 = Livre('Harry Potter vol 2', 'J.K. Rowling', '1234567890')
print(livre_2)  # Appelle automatiquement __str__

print(Livre.obtenir_nombre_total())