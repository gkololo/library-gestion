# TEST COMPLET DU SYSTÈME DE BIBLIOTHÈQUE
from module_1_Livre import Livre
from module_2 import Membre

print("=" * 60)
print("🏛️  SYSTÈME DE GESTION DE BIBLIOTHÈQUE")
print("=" * 60)

# ===== CRÉATION D'UNE COLLECTION DE LIVRES =====
print("\n📚 CRÉATION DE LA COLLECTION DE LIVRES")
print("-" * 40)

livres = {
    'hp1': Livre('Harry Potter à l\'école des sorciers', 'J.K. Rowling', '9782070584623'),
    'hp2': Livre('Harry Potter et la Chambre des secrets', 'J.K. Rowling', '9782070585205'),
    'lotr': Livre('Le Seigneur des Anneaux', 'J.R.R. Tolkien', '9782266154345'),
    '1984': Livre('1984', 'George Orwell', '9782070368228'),
    'dune': Livre('Dune', 'Frank Herbert', '9782266320580'),
    'gatsby': Livre('Gatsby le Magnifique', 'F. Scott Fitzgerald', '9782070379347'),
    'pride': Livre('Orgueil et Préjugés', 'Jane Austen', '9782070417742'),
    'hitchhiker': Livre('Le Guide du voyageur galactique', 'Douglas Adams', '9782070423286')
}

print(f"✅ {len(livres)} livres ajoutés à la collection")
print(f"📊 {Livre.obtenir_nombre_total()}")

# ===== CRÉATION DES MEMBRES =====
print("\n👥 CRÉATION DES MEMBRES")
print("-" * 40)

membres = {
    'alice': Membre('MARTIN', 'Alice', 1001),
    'bob': Membre('DURAND', 'Bob', 1002),
    'charlie': Membre('BERNARD', 'Charlie', 1003)
}

for nom, membre in membres.items():
    print(f"✅ {membre}")

print(f"📊 {Membre.obtenir_nombre_total()}")

# ===== SCÉNARIO DE TEST COMPLET =====
print("\n" + "=" * 60)
print("🎭 SCÉNARIOS DE TEST")
print("=" * 60)

# --- Scénario 1: Alice emprunte plusieurs livres ---
print("\n📖 SCÉNARIO 1: Alice découvre la fantasy")
print("-" * 45)

alice = membres['alice']

# Alice emprunte Harry Potter 1
print(f"🔄 {alice.emprunter_livre(livres['hp1'])}")
print(f"📋 {alice.afficher_emprunts()}")

# Alice emprunte Le Seigneur des Anneaux
print(f"\n🔄 {alice.emprunter_livre(livres['lotr'])}")
print(f"📋 {alice.afficher_emprunts()}")

# Alice essaie d'emprunter Harry Potter 1 à nouveau
print(f"\n❌ Tentative de double emprunt:")
print(f"🔄 {alice.emprunter_livre(livres['hp1'])}")

# --- Scénario 2: Bob essaie d'emprunter un livre déjà pris ---
print("\n📖 SCÉNARIO 2: Bob veut le même livre qu'Alice")
print("-" * 50)

bob = membres['bob']
print(f"❌ {bob.emprunter_livre(livres['hp1'])}")
print(f"✅ {bob.emprunter_livre(livres['hp2'])}")
print(f"✅ {bob.emprunter_livre(livres['1984'])}")
print(f"📋 {bob.afficher_emprunts()}")

# --- Scénario 3: Charlie teste la limite d'emprunts ---
print("\n📖 SCÉNARIO 3: Charlie teste ses limites")
print("-" * 45)

charlie = membres['charlie']
livres_pour_charlie = ['dune', 'gatsby', 'pride', 'hitchhiker']

for livre_key in livres_pour_charlie:
    resultat = charlie.emprunter_livre(livres[livre_key])
    print(f"🔄 {resultat}")

print(f"📋 {charlie.afficher_emprunts()}")

# Charlie essaie d'emprunter un 5ème livre (limite atteinte)
print(f"\n❌ Tentative de dépassement de limite:")
# Créons un nouveau livre pour le test
livre_extra = Livre('Les Misérables', 'Victor Hugo', '9782070409228')
print(f"🔄 {charlie.emprunter_livre(livre_extra)}")

# --- Scénario 4: Retours de livres ---
print("\n📖 SCÉNARIO 4: Retours et nouveaux emprunts")
print("-" * 50)

# Alice rend Harry Potter 1
print(f"📤 {alice.retourner_livre(livres['hp1'])}")
print(f"📋 État actuel d'Alice: {alice.afficher_emprunts()}")

# Maintenant Bob peut l'emprunter
print(f"\n🔄 {bob.emprunter_livre(livres['hp1'])}")
print(f"📋 {bob.afficher_emprunts()}")

# Charlie rend un livre et en emprunte un nouveau
print(f"\n📤 {charlie.retourner_livre(livres['dune'])}")
print(f"🔄 {charlie.emprunter_livre(livre_extra)}")
print(f"📋 {charlie.afficher_emprunts()}")

# --- Scénario 5: Tentatives de retour invalides ---
print("\n📖 SCÉNARIO 5: Tests d'erreurs de retour")
print("-" * 45)

# Alice essaie de rendre un livre qu'elle n'a pas
print(f"❌ {alice.retourner_livre(livres['1984'])}")

# Bob essaie de rendre un livre qu'il a déjà rendu
livre_bidon = Livre('Livre Inexistant', 'Auteur Inconnu', '1111111111')
print(f"❌ {bob.retourner_livre(livre_bidon)}")

# ===== ÉTAT FINAL =====
print("\n" + "=" * 60)
print("📊 ÉTAT FINAL DE LA BIBLIOTHÈQUE")
print("=" * 60)

print(f"📚 {Livre.obtenir_nombre_total()}")
print(f"👥 {Membre.obtenir_nombre_total()}")

print("\n📋 EMPRUNTS ACTUELS:")
print("-" * 25)
for nom, membre in membres.items():
    print(f"{membre.afficher_emprunts()}")

print("\n📖 DISPONIBILITÉ DES LIVRES:")
print("-" * 30)
for nom, livre in livres.items():
    statut = "🟢 Disponible" if livre.disponible else "🔴 Emprunté"
    print(f"{statut} - {livre.titre}")

print(f"{livre_extra.disponibilite} - {livre_extra.titre}")

print("\n🎉 Tests terminés avec succès!")
print("=" * 60)