import matplotlib.pyplot as plt
import seaborn as sns
from Livres.encodage_livre import Livre
from Utilisateurs.data_utilisateur import Utilisateur


def statistiques(livres: list[Livre], utilisateurs: list[Utilisateur]) -> None:
    """
    Affiche les statistiques de la bibliothèque et de ses utilisateurs : ie le nombre total de livres, le nombre
    d'utilisateurs, ainsi qu'un graphique représentant le nombre d'emprunts par utilisateur.
    :param livres: Liste des livres présents dans la bibliothèque.
    :param utilisateurs: Liste des utilisateurs inscrits à la bibliothèque.
    :return: Message sur les statistiques dans la console et affiche le graphique.
    """
    # Calcul du nombre de livres dans la bibliothèque
    nb_livres = len(livres)
    print(f"La bibliothèque contient {nb_livres} livres.")

    # Calcul du nombre d'utilisateurs de la bibliothèque
    nb_util = len(utilisateurs)
    print(f"La bibliotheque a {nb_util} utilisateurs.")

    # Récupération des données pour le graph
    noms = [u.nom for u in utilisateurs]
    nb_emprunts = [len(u.emprunts) for u in utilisateurs]

    # Graphique suivant la méthode vue en cours
    sns.set_style(style="darkgrid")
    plt.figure(figsize=(12, 8))
    plt.plot(noms, nb_emprunts, color="#2a9d8f", marker="o", label="Emprunts par utilisateur")
    plt.title("Distribution des emprunts par utilisateurs", fontweight="bold")
    plt.xlabel("Utilisateurs", fontweight="bold")
    plt.ylabel("Nombre d'emprunts", fontweight="bold")
    plt.grid(True)
    plt.xticks(rotation=25, ha="right")
    plt.legend()
    plt.show()

    return None