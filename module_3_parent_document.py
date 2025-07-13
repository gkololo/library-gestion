class Document:
    def __init__(self, titre, createur, identifiant):
        self.titre = titre
        self.createur = createur  # Générique : auteur, réalisateur, éditeur...
        self.identifiant = identifiant  # ISBN, code-barre, etc.
        self.disponible = True  # Tous les documents peuvent être empruntés

    def afficher_info(self):
        # Affichage de base - sera enrichi par les enfants
        return f"Titre: {self.titre}\nCréateur: {self.createur}\nID: {self.identifiant}\nDisponible: {self.disponible}"