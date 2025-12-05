import pytest
from copy import deepcopy
from Utilisateurs.encodage_utilisateur import Utilisateur, generate_utilisateur_id
from Utilisateurs.fonctionnalites_utilisateur import FonctionnaliteUtilisateur
from Utilisateurs.data_utilisateur import data_utilisateur


@pytest.fixture
def adherent():
    #Retourne une instance fraîche avant chaque test.
    utilisateurs_test = deepcopy(data_utilisateur)
    return FonctionnaliteUtilisateur(utilisateurs=utilisateurs_test)


# FONCTION CREATION UTILISATEUR

def test_creation_utilisateur_nouveau(adherent):
    command = adherent.creation_utilisateur("Sarah Bar")
    nouvel_utilisateur = next(u for u in adherent.utilisateurs if u.nom == "Sarah Bar")

    assert command == f"M/Mme {nouvel_utilisateur.nom} a bien été enregistré(e) comme nouvel utilisateur. Son identifiant sera : {nouvel_utilisateur.ident}."
    assert nouvel_utilisateur in adherent.utilisateurs


def test_creation_utilisateur_existant(adherent):
    # On tente de créer un utilisateur déjà présent, par exemple, le premier de nos données.
    command = adherent.creation_utilisateur("Alice Martin")
    utilisateur_existant = next(u for u in adherent.utilisateurs if u.nom == "Alice Martin")

    assert command == f"M/Mme {utilisateur_existant.nom} est déjà enregistré(e)."


# FONCTION SUPPRESSION UTILISATEUR

def test_supprimer_utilisateur_sans_emprunt(adherent):
    # Nous prenons l'identifiant d'un utilisateur sans emprunt dans les données : U60FB3
    utilisateur = next(u for u in adherent.utilisateurs if u.ident == "U60FB3")
    command = adherent.suppression_utilisateur("U60FB3")

    assert command == f"M/Mme {utilisateur.nom} a bien été supprimé."
    assert utilisateur not in adherent.utilisateurs


def test_supprimer_utilisateur_avec_emprunt(adherent):
    # Nous prenons l'identifiant d'un utilisateur avec emprunt dans les données : U87F3C
    command = adherent.suppression_utilisateur("U87F3C")
    utilisateur = next(u for u in adherent.utilisateurs if u.ident == "U87F3C")

    assert command == f"M/Mme {utilisateur.nom} a des livres empruntés, il est donc impossible de le/la supprimer."
    assert utilisateur in adherent.utilisateurs


def test_suppression_utilisateur_inexistant(adherent):
    with pytest.raises(ValueError):
        adherent.suppression_utilisateur("ID_INEXISTANT")


# FONCTION LISTE UTILISATEUR

def test_liste_utilisateurs_enregistres_vide():
    liste_vide = FonctionnaliteUtilisateur(utilisateurs=[])
    command = liste_vide.liste_utilisateurs_enregistres()
    assert command == "Aucun utilisateur n'est enregistré pour le moment."


def test_liste_utilisateurs_enregistres_non_vide():
    # Nous créons une liste d'utilisateur test plus courte avec les deux premiers utilisateurs.
    utilisateurs_test = [
        Utilisateur("U1A3F9", "Alice Martin"),
        Utilisateur("U29C7A", "Bob Durand")
    ]

    command = FonctionnaliteUtilisateur(utilisateurs=utilisateurs_test).liste_utilisateurs_enregistres()

    expected = (
        "Les utilisateurs actuellement enregistrés sont :\n"
        "U1A3F9 - Alice Martin\n"
        "U29C7A - Bob Durand"
    )

    assert command == expected


# FONCTION GENERATEUR D'IDENTIFIANT

def test_generate_utilisateur_id():
    command = generate_utilisateur_id()

    assert command.startswith("U")
    assert len(command) == 6
    assert command[1:].isalnum()
    for c in command[1:]:
        assert c.isdigit() or c.isupper()