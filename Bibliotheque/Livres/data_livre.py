from Livres.encodage_livre import Livre, Disponibilite

# Nous demandons à chatGPT de nous fournir une liste de 20 livres qui nous servira pour les tests.
# Nous laissons 5 livres disponibles à l'emprunt.

data_livre = [
    Livre("L3F9D2", "Le Petit Prince", "Antoine de Saint-Exupéry", Disponibilite.DISPONIBLE),
    Livre("L9C7A1", "1984", "George Orwell", Disponibilite.EMPRUNTE),
    Livre("LF12B8", "Les Misérables", "Victor Hugo", Disponibilite.DISPONIBLE),
    Livre("L7AB3F", "Le Comte de Monte-Cristo", "Alexandre Dumas", Disponibilite.EMPRUNTE),
    Livre("L3E9BD", "Harry Potter à l'école des sorciers", "J.K. Rowling", Disponibilite.DISPONIBLE),
    Livre("LDF4A9", "Le Seigneur des Anneaux", "J.R.R. Tolkien", Disponibilite.EMPRUNTE),
    Livre("L5C1E7", "Madame Bovary", "Gustave Flaubert", Disponibilite.DISPONIBLE),
    Livre("L0FB3C", "Le Rouge et le Noir", "Stendhal", Disponibilite.EMPRUNTE),
    Livre("LA19E4", "L'Étranger", "Albert Camus", Disponibilite.EMPRUNTE),
    Livre("L4D7E9", "Les Fleurs du mal", "Charles Baudelaire", Disponibilite.DISPONIBLE),
    Livre("LC1A9F", "Le Nom de la Rose", "Umberto Eco", Disponibilite.EMPRUNTE),
    Livre("L7F3C0", "Bel-Ami", "Guy de Maupassant", Disponibilite.EMPRUNTE),
    Livre("L2A7D6", "La Peste", "Albert Camus", Disponibilite.EMPRUNTE),
    Livre("L8B5E1", "Candide", "Voltaire", Disponibilite.EMPRUNTE),
    Livre("LF7A11", "La Chartreuse de Parme", "Stendhal", Disponibilite.EMPRUNTE),
    Livre("LB2C98", "Le Père Goriot", "Honoré de Balzac", Disponibilite.EMPRUNTE),
    Livre("L9E014", "Le Journal d'Anne Frank", "Anne Frank", Disponibilite.EMPRUNTE),
    Livre("L6AF9D", "Le Vieil Homme et la Mer", "Ernest Hemingway", Disponibilite.EMPRUNTE),
    Livre("LED129", "Notre-Dame de Paris", "Victor Hugo", Disponibilite.EMPRUNTE),
    Livre("L3F81A", "Le Grand Meaulnes", "Alain-Fournier", Disponibilite.EMPRUNTE),
]



