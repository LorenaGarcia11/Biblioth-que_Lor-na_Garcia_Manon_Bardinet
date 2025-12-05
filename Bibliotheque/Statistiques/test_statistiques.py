# N'ayant jamais vu en cours comment tester une fonction composée d'un graphique,
# nous nous sommes aidées de ChatGPT pour trouver les commandes nécéssaires.

from unittest.mock import patch
from Livres.encodage_livre import Livre, Disponibilite
from Utilisateurs.encodage_utilisateur import Utilisateur
from Statistiques.stats import statistiques


def test_statistiques_affichage_et_graphique(capsys):
    # Données fictives pour plus de simplicité
    livres = [
        Livre("L1", "Livre A", "Auteur A", Disponibilite.DISPONIBLE),
        Livre("L2", "Livre B", "Auteur B", Disponibilite.EMPRUNTE),
    ]

    utilisateurs = [
        Utilisateur("U1", "Alice", emprunts=["L2"]),
        Utilisateur("U2", "Bob", emprunts=[]),
    ]

    # On empêche plt.show() de bloquer
    with patch("matplotlib.pyplot.show") as mock_show:

        statistiques(livres, utilisateurs)

        # Vérifie que le graphique a été tenté
        mock_show.assert_called_once()

    # On capture les prints
    captured = capsys.readouterr().out

    assert "La bibliothèque contient 2 livres." in captured
    assert "La bibliotheque a 2 utilisateurs." in captured
