import pytest
from copy import deepcopy
from Livres.fonctionnalites_livre import FonctionnaliteLivre
from Livres.data_livre import data_livre
from Livres.encodage_livre import generate_livre_id, Disponibilite


@pytest.fixture
def bibliotheque():
    #Retourne une instance fraîche avant chaque test.
    livres_test = deepcopy(data_livre)
    return FonctionnaliteLivre(livres=livres_test)


# TEST AJOUT LIVRE

def test_ajouter_livre_nouveau(bibliotheque):
    command = bibliotheque.ajouter_livre("Nouveau livre", "Quelqu'un")
    nouveau_livre = next(l for l in bibliotheque.livres if l.titre == "Nouveau livre" and l.auteur == "Quelqu'un")

    assert command == f"Le livre « {nouveau_livre.titre} » de {nouveau_livre.auteur} a bien été ajouté à la bibliothèque sous l'identifiant {nouveau_livre.ident}."
    assert nouveau_livre in bibliotheque.livres


def test_ajouter_livre_existant(bibliotheque):
    # Nous prenons un livre appartenant déjà à la bibliothèque
    livre_existant = next(l for l in bibliotheque.livres if l.titre == "Les Misérables" and l.auteur == "Victor Hugo")
    command = bibliotheque.ajouter_livre("Les Misérables", "Victor Hugo")

    assert command == f"Le livre {livre_existant.titre} de {livre_existant.auteur} appartient déjà à la bibliothèque sous l'identifiant {livre_existant.ident}."


# TEST SUPPRIMER LIVRE

def test_supprimer_livre_emprunte(bibliotheque):
    # Nous prenons un livre en cours d'emprunt dans les données, par exemple : LDF4A9
    command = bibliotheque.supprimer_livre("LDF4A9")
    livre = next(l for l in bibliotheque.livres if l.ident == "LDF4A9")

    assert command == f"Le livre « {livre.titre} » de {livre.auteur} avec pour identifiant {livre.ident} est en cours d'emprunt. La suppression est temporairement impossible."
    assert livre in bibliotheque.livres


def test_supprimer_livre_disponible(bibliotheque):
    # Nous prenons un livre disponible dans les données, par exemple : L5C1E7
    livre = next(l for l in bibliotheque.livres if l.ident == "L5C1E7")
    command = bibliotheque.supprimer_livre("L5C1E7")

    assert command == f"Le livre « {livre.titre} » de {livre.auteur} avec pour identifiant {livre.ident} a été supprimé de la bibliothèque."
    assert livre not in bibliotheque.livres


def test_supprimer_livre_inexistant(bibliotheque):
    with pytest.raises(ValueError):
        bibliotheque.supprimer_livre("ID_INEXISTANT")


# TEST MODIFIER STATUT

def test_modifier_statut_livre_existant_disponible(bibliotheque):
    # Nous prenons un livre disponible dans les données, par exemple : L4D7E9
    command = bibliotheque.modifier_statut("L4D7E9")
    livre = next(l for l in bibliotheque.livres if l.ident == "L4D7E9")

    assert command == f"Le livre « {livre.titre} » est maintenant emprunté."
    assert livre.statut == Disponibilite.EMPRUNTE


def test_modifier_statut_livre_existant_emprunte(bibliotheque):
    # Nous prenons un livre emprunté dans les données, par exemple : L8B5E1
    command = bibliotheque.modifier_statut("L8B5E1")
    livre = next(l for l in bibliotheque.livres if l.ident == "L8B5E1")

    assert command == f"Le livre « {livre.titre} » est maintenant disponible."
    assert livre.statut == Disponibilite.DISPONIBLE


def test_modifier_statut_livre_non_existant(bibliotheque):
    with pytest.raises(ValueError):
        bibliotheque.modifier_statut("ID_INEXISTANT")


# TEST LISTE LIVRE DISPONIBLE

def test_liste_livre_dispo_pas_vide(bibliotheque):
    # Nous affichons les livres disponibles dans la bibliothèque (au nombre de 5).
    command = bibliotheque.liste_livre_dispo()
    expected = (
        "Les livres actuellement disponibles sont :\n"
        "L3F9D2 - Le Petit Prince (Antoine de Saint-Exupéry)\n"
        "LF12B8 - Les Misérables (Victor Hugo)\n"
        "L3E9BD - Harry Potter à l'école des sorciers (J.K. Rowling)\n"
        "L5C1E7 - Madame Bovary (Gustave Flaubert)\n"
        "L4D7E9 - Les Fleurs du mal (Charles Baudelaire)"
    )

    assert command == expected


def test_liste_livre_dispo_vide():
    # Nous créons une liste vide
    bibliotheque_test = FonctionnaliteLivre([])
    command = bibliotheque_test.liste_livre_dispo()

    assert command == "Aucun livre n'est actuellement disponible."


# TEST RECHERCHE TITRE

def test_recherche_livre_titre_existant(bibliotheque):
    # Nous prenons un titre de notre bibliothèque, par exemple : La Peste
    command = bibliotheque.recherche_titre("La Peste")
    livre = next(l for l in bibliotheque.livres if l.titre == "La Peste")

    assert command == f"{livre.titre} par {livre.auteur} (ID: {livre.ident}) - {livre.statut.name}"


def test_recherche_livre_non_existant(bibliotheque):
    titre = "Titre Inexistant"
    command = bibliotheque.recherche_titre(titre)

    assert command == f"Aucun livre trouvé avec le titre '{titre}'."


# TEST RECHERCHE AUTEUR

def test_recherche_livre_auteur_existant(bibliotheque):
    # Nous prenons un auteur présent dans les données, par exemple : Albert Camus
    command = bibliotheque.recherche_auteur("Albert Camus")
    expected = ("L'Étranger par Albert Camus (ID: LA19E4) - EMPRUNTE\n"
        "La Peste par Albert Camus (ID: L2A7D6) - EMPRUNTE")

    assert command == expected


def test_recherche_auteur_inexistant(bibliotheque):
    auteur = "Auteur Inexistant"
    command = bibliotheque.recherche_auteur(auteur)

    assert command == f"Aucun livre trouvé pour l'auteur '{auteur}'."


# TEST RECHERCHE MOT CLE

def test_recherche_mot_cle_existant(bibliotheque):
    # Nous prenons des mots clés présents dans les titres de nos données, par exemple : des
    command = bibliotheque.recherche_mot_cle("des")
    expected = ("Harry Potter à l'école des sorciers par J.K. Rowling (ID: L3E9BD) - DISPONIBLE\n"
        "Le Seigneur des Anneaux par J.R.R. Tolkien (ID: LDF4A9) - EMPRUNTE")

    assert command == expected


def test_recherche_mot_cle_inexistant(bibliotheque):
    mot = "Mot Inexistant"
    command = bibliotheque.recherche_mot_cle(mot)

    assert command == f"Aucun livre trouvé contenant le mot-clé '{mot}'."


# FONCTION GENERATEUR D'IDENTIFIANT

def test_generate_livre_id():
    command = generate_livre_id()
    assert command.startswith("L")
    assert len(command) == 6
    assert command[1:].isalnum()
    for c in command[1:]:
        assert c.isdigit() or c.isupper()