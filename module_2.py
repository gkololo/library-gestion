
class Membre:
    # Attribut de classe pour le compteur
    # Attribut de classe pour les numéros déjà utilisés
    nombre_total_membres = 0
    liste_membres =[]

    def __init__(self, nom: str, prenom: str, numero_membre: int):
        # Validation du numéro unique
        Membre.validation_numero_membre(numero_membre)
        self.nom = nom
        self.prenom = prenom
        self.numero_membre = numero_membre
        self.livres_empruntes = []  # Liste d'ISBN (strings)
        self.limite_emprunts = 5    # Limite raisonnable
        Membre.liste_membres.append(numero_membre)
        Membre.nombre_total_membres +=1

    @staticmethod
    def validation_numero_membre(numero_membre):
        if isinstance(numero_membre, int) and numero_membre > 0:
            if numero_membre not in Membre.liste_membres:
                return True
            else:
                print('Numéro de membre déjà existant')
                raise ValueError
        else:
            print('Format du numéro de membre invalide (doit être un entier positif)')
            raise ValueError

    def __str__(self):
        return f'Nouveau Membre : {self.prenom} {self.nom}, membre ID n°{self.numero_membre}'

    @classmethod
    def obtenir_nombre_total(cls):
        return f'Nombre total de membres: {cls.nombre_total_membres}'

# TESTS
membre_1 = Membre('Jean', 'DUPONT', 1)
membre_2 = Membre('Albert', 'EISNTEIN', 2)
print(membre_1)
print(membre_2)
print(Membre.obtenir_nombre_total())
