import pytest
from copy import deepcopy
from Livres.data_livre import data_livre
from Livres.encodage_livre import Disponibilite
from Utilisateurs.data_utilisateur import data_utilisateur
from Gestion.emprunt_retour import EmpruntRetour

@pytest.fixture
def gestion():
    #Retourne une instance fraîche avant chaque test.
    utilisateurs_test = deepcopy(data_utilisateur)
    livres_test = deepcopy(data_livre)
    return EmpruntRetour(livres= livres_test, utilisateurs=utilisateurs_test)


# TEST EMPRUNT LIVRE

def test_emprunt_livre_disponible(gestion):
    # Nous prenons un livre disponible et un utilisateur existant dans nos données, par exemple : le livre L3F9D2 et l'utilisateur U47AB3.
    command = gestion.emprunt_livre("U47AB3", "L3F9D2")

    livre = next(l for l in gestion.livres if l.ident == "L3F9D2")
    utilisateur = next(u for u in gestion.utilisateurs if u.ident == "U47AB3")

    assert command == f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {livre.ident} a bien été emprunté."
    assert livre.ident in utilisateur.emprunts
    assert livre.statut == Disponibilite.EMPRUNTE


def test_emprunt_livre_deja_emprunte(gestion):
    # Nous prenons un livre déjà emprunté et un utilisateur existant de nos données, par exemple : le livre L9C7A1 et l'utilisateur U47AB3.
    command = gestion.emprunt_livre("U47AB3", "L9C7A1")

    livre = next(l for l in gestion.livres if l.ident == "L9C7A1")
    utilisateur = next(u for u in gestion.utilisateurs if u.ident == "U47AB3")

    assert command == f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {livre.ident} est déjà emprunté."
    assert livre.statut == Disponibilite.EMPRUNTE
    assert livre.ident not in utilisateur.emprunts


def test_emprunt_livre_inexistant(gestion):
    with pytest.raises(ValueError):
        gestion.emprunt_livre("U1A3F9", "ID_INEXISTANT")


def test_emprunt_utilisateur_inexistant(gestion):
    with pytest.raises(ValueError):
        gestion.emprunt_livre("ID_INEXISTANT", "L9C7A1")


# TEST RETOUR LIVRE

def test_retour_livre_correct(gestion):
    # Nous prenons un livre emprunté et l'utilisateur l'ayant emprunté, existant dans nos données, par exemple : le livre L8B5E1 et l'utilisateur U6A19E.
    command = gestion.retour_livre("U6A19E", "L8B5E1")

    livre = next(l for l in gestion.livres if l.ident == "L8B5E1")
    utilisateur = next(u for u in gestion.utilisateurs if u.ident == "U6A19E")

    assert command == f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {livre.ident} a bien été rendu."
    assert livre.ident not in utilisateur.emprunts
    assert livre.statut == Disponibilite.DISPONIBLE


def test_retour_livre_non_emprunte_par_user(gestion):
    # Nous prenons un livre emprunté et un utilisateur ne l'ayant pas emprunté, existant dans nos données, par exemple : le livre LDF4A9 et l'utilisateur U92A7D.
    command = gestion.retour_livre("U92A7D", "L8B5E1")

    livre = next(l for l in gestion.livres if l.ident == "L8B5E1")
    utilisateur = next(u for u in gestion.utilisateurs if u.ident == "U92A7D")

    assert command == f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {livre.ident} n'est pas emprunté par l'utilisateur {utilisateur.ident}. Vous ne pouvez le rendre."
    assert livre.ident not in utilisateur.emprunts
    assert livre.statut == Disponibilite.EMPRUNTE


def test_retour_livre_disponible(gestion):
    # Nous prenons un livre disponible dans nos données et un utilisateur qui ne l'a donc pas emprunté, par exemple : L4D7E9 et U92A7D.
    command = gestion.retour_livre("U92A7D", "L4D7E9")
    livre = next(l for l in gestion.livres if l.ident == "L4D7E9")

    assert command == f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {livre.ident} n'est pas emprunté. Vous ne pouvez le rendre."
    assert livre.statut == Disponibilite.DISPONIBLE


def test_retour_livre_inexistant(gestion):
    with pytest.raises(ValueError):
        gestion.emprunt_livre("U1A3F9", "ID_INEXISTANT")


def test_retour_utilisateur_inexistant(gestion):
    with pytest.raises(ValueError):
        gestion.emprunt_livre("ID_INEXISTANT", "L9C7A1")