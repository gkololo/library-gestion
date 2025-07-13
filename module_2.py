from module_1_Livre import Livre

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


    def emprunter_livre(self, livre):
        if len(self.livres_empruntes) < self.limite_emprunts:       # Vérification 1 : Le membre a-t-il atteint sa limite ?
            if not livre.isbn in self.livres_empruntes:                  # Vérification  2 : le membre a-t-il déjà emprunté ce livre ?
                if livre.disponible:                                # Disponibilité de CET objet livre par l'isbn : un autre membre l'a peut-être emprunté ?
                    livre.emprunter()
                    self.livres_empruntes.append(livre.isbn)  # L'ISBN de cet objet
                    return f"Emprunt réussi : {livre.titre}"
                else:
                    return f'Ce livre n\'est PAS disponible'
            else:
                return f'Vous avez déjà emprunté ce livre'
        else:
            return f'Nombre maximal de livres empruntés atteint'


    def retourner_livre(self, livre):
        if livre.isbn in self.livres_empruntes:             # Vérification   : le membre a-t-il emprunté ce livre ?
            self.livres_empruntes.remove(livre.isbn)        # enlever de la liste
            livre.retourner()
            return f'{self.prenom} {self.nom} a rendu {livre.titre}'
        else:
            return f'{self.prenom} {self.nom} n\'avait pas emprunté ce livre: {livre.titre}'


    def afficher_emprunts(self):
        if not self.livres_empruntes:  # Liste vide
            return f"{self.prenom} {self.nom} n'a aucun livre emprunté"
        else:
            nombre = len(self.livres_empruntes)
            header = f"{self.prenom} {self.nom} a emprunté {nombre} livre(s) :"

            # Créer une liste avec des retours à la ligne
            livres_formates = []
            for i, isbn in enumerate(self.livres_empruntes, 1):
                titre_complet = Livre.afficher_livre_par_isbn(isbn)
                livres_formates.append(f"  {i}. {titre_complet}")

            return header + "\n" + "\n".join(livres_formates)




# TESTS
""" membre_1 = Membre('Jean', 'DUPONT', 1)
membre_2 = Membre('Albert', 'EISNTEIN', 2)
print(membre_1)
print(membre_2)
print(Membre.obtenir_nombre_total())

print("\n=== TEST EMPRUNTS ===")
print(f"Livre 1 avant : {livre_1.disponible}")
print(f"Emprunts par {membre_1.prenom} {membre_1.nom}: {membre_1.livres_empruntes}")
resultat = membre_1.emprunter_livre(livre_1)
print(f"Résultat : {resultat}")

print(f"Livre 1 après emprunt : {livre_1.disponible}")
print(f"Emprunts membre 1 : {membre_1.livres_empruntes}")

print(f'Livres empruntés:\n{membre_1.afficher_emprunts()}')  # ✅ Avec \n pour plus de clarté """






