from Livres.data_livre import data_livre
from Livres.fonctionnalites_livre import FonctionnaliteLivre
from Utilisateurs.data_utilisateur import data_utilisateur
from Utilisateurs.fonctionnalites_utilisateur import FonctionnaliteUtilisateur
from Gestion.emprunt_retour import EmpruntRetour
from Statistiques.stats import statistiques

# Voici une idée additionnelle pour une borne d'accueil de la bibliothèque qui permet d'effectuer toutes
# les fonctionnalités codées dans les dossiers.

bibliotheque = FonctionnaliteLivre(data_livre)
adherent = FonctionnaliteUtilisateur(data_utilisateur)
gestion = EmpruntRetour(data_livre, data_utilisateur)

def menu_principal():
    menu = """
    Bonjour, bienvenue sur la borne numérique de notre librairie.
    Veuillez sélectionner une option parmi :

    1. Créer votre profil d'utilisateur
    2. Ajouter un livre
    3. Supprimer un livre
    4. Emprunter un livre
    5. Rendre un livre
    6. Lister les livres
    7. Lister les utilisateurs
    8. Rechercher un livre
    9. Statistiques de la librairie
    10. Supprimer votre profil d'utilisateur

    Le numéro de votre choix : """

    option = input(menu)

    match option:
        case "1":
            nom = input("Nous allons créer votre profil d'utilisateur. Merci d'écrire votre nom : ")
            print(adherent.creation_utilisateur(nom))

        case "2":
            print("Nous allons ajouter un livre à la librairie, merci de renseigner :")
            titre = input("Le titre : ")
            auteur = input("L'auteur : ")
            print(bibliotheque.ajouter_livre(titre, auteur))

        case "3":
            print("Nous allons supprimer un livre de la librairie, merci de renseigner :")
            ident_livre = input("L'identifiant du livre : ")
            print(bibliotheque.supprimer_livre(ident_livre))

        case "4":
            print("Vous allez emprunter un livre, merci de renseigner :")
            ident_user = input("Votre identifiant d'utilisateur : ")
            ident_livre = input("L'identifiant du livre : ")
            print(gestion.emprunt_livre(ident_user, ident_livre))

        case "5":
            print("Vous allez rendre un livre, merci de renseigner :")
            ident_user = input("Votre identifiant d'utilisateur : ")
            ident_livre = input("L'identifiant du livre : ")
            print(gestion.retour_livre(ident_user, ident_livre))

        case "6":
            print("Voici la liste des livres disponibles :")
            print(bibliotheque.liste_livre_dispo())

        case "7":
            print("Voici la liste des utilisateurs :")
            print(adherent.liste_utilisateurs_enregistres())

        case "8":
            print("Vous souhaitez rechercher un livre. Souhaitez-vous procéder par titre, auteur ou mot clé ?")
            mode = input("Saisir Titre, Auteur ou Mot clé : ")

            if mode == "Titre":
                titre = input("Le titre : ")
                print(bibliotheque.recherche_titre(titre))

            elif mode == "Auteur":
                auteur = input("L'auteur : ")
                print(bibliotheque.recherche_auteur(auteur))

            elif mode == "Mot clé":
                mot = input("Le mot clé : ")
                print(bibliotheque.recherche_mot_cle(mot))

            else:
                print("Ce que vous avez saisi ne correspond pas à ce qui était demandé ! Recommencez.")

        case "9":
            print("Voici les statistiques de la librairie :")
            print(statistiques(data_livre, data_utilisateur))

        case "10":
            rep = input("Êtes-vous sûr de vouloir supprimer votre compte utilisateur ? Oui/Non : ")
            if rep == "Oui":
                ident_user = input("Votre identifiant d'utilisateur : ")
                print(adherent.suppression_utilisateur(ident_user))
            elif rep == "Non":
                print("D'accord, n'hésitez pas à emprunter un livre !")
            else:
                print("Ce que vous avez saisi ne correspond pas à ce qui était demandé ! Recommencez.")

        case _:
            print("Ce numéro n'est pas dans la liste ! Merci de recommencer.")

    print("Merci d'avoir utilisé la borne numérique ! À bientôt.")

#EXEMPLE DE LANCEMENT
menu_principal() #Si on veut se créer un profil par exemple
menu_principal() #Si on veut emprunter un livre, par exemple L3F9D2
