from Livres.encodage_livre import Livre, Disponibilite
from Livres.fonctionnalites_livre import FonctionnaliteLivre
from Utilisateurs.encodage_utilisateur import Utilisateur

# Nous créons une classe qui s'occupe de la gestion des emprunts et des retours.
class EmpruntRetour:

    def __init__(self, livres: list[Livre], utilisateurs: list[Utilisateur]) -> None:
        self.livres = livres
        self.utilisateurs = utilisateurs


    def emprunt_livre(self, ident_user, ident_livre) -> str:
        """
        On permet à un utilisateur d'emprunter un livre, si celui qu'il souhaite est disponible.
        Si c'est le cas, son statut est mis à jour et on ajoute son identifiant à la liste des emprunts de l'utilisateur.

        :param ident_user: Identifiant de l'utilisateur souhaitant emprunter un livre.
        :param ident_livre: Identifiant du livre que l'utilisateur souhaite emprunter.
        :return: Message indiquant :
        - soit que le livre indiqué a bien été emprunté par l'utilisateur dont l'identifiant a été inséré,
        - soit qu'il est impossible pour l'utilisateur d'emprunté le livre, car celui-ci est déjà emprunté.
        :raises ValueError: Si aucun livre ne correspond à l'identifiant fourni.
        :raises ValueError: Si aucun utilisateur ne correspond à l'identifiant fourni.
        """
        utilisateur = next((u for u in self.utilisateurs if u.ident == ident_user), None)
        #Commande next trouvée sur internet qui crée un générateur qui parcourt self.utilisateurs et ne retient que l'utilisateur dont l'identifiant correspond s'il existe.
        if not utilisateur:
            raise ValueError(f"Aucun utilisateur enregistré sous l'identifiant {ident_user}.")

        livre = next((l for l in self.livres if l.ident == ident_livre), None)
        if not livre:
            raise ValueError(f"Aucun livre enregistré sous l'identifiant {ident_livre}.")

        if livre.statut == Disponibilite.DISPONIBLE:
            FonctionnaliteLivre(self.livres).modifier_statut(ident_livre)
            utilisateur.emprunts.append(ident_livre)
            return f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {ident_livre} a bien été emprunté."
        else:
            return f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {ident_livre} est déjà emprunté."


    def retour_livre(self, ident_user, ident_livre) -> str:
        """
        Permet à un utilisateur de rendre un livre qu'il a emprunté.
        Si le livre est bien actuellement emprunté par l'utilisateur, on modifie son statut et on retire son identifiant à la liste des emprunts de l'utilisateur.

        :param ident_user: Identifiant de l'utilisateur souhaitant rendre un livre.
        :param ident_livre: Identifiant du livre que l'utilisateur souhaite rendre.
        :return: Message indiquant :
        - soit que le livre indiqué a bien été rendu par l'utilisateur,
        - soit qu'il est impossible pour l'utilisateur de rendre le livre, car celui-ci n'a pas été emprunté par lui,
        - soit qu'il est impossible pour l'utilisateur de rendre le livre, car celui-ci est actuellement disponible.
        :raises ValueError: Si aucun livre ne correspond à l'identifiant fourni.
        :raises ValueError: Si aucun utilisateur ne correspond à l'identifiant fourni.
        """
        utilisateur = next((u for u in self.utilisateurs if u.ident == ident_user), None)
        if not utilisateur:
            raise ValueError(f"Aucun utilisateur enregistré sous l'identifiant {ident_user}.")

        livre = next((l for l in self.livres if l.ident == ident_livre), None)
        if not livre:
            raise ValueError(f"Aucun livre enregistré sous l'identifiant {ident_livre}.")

        if livre.statut == Disponibilite.DISPONIBLE:
            return f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {ident_livre} n'est pas emprunté. Vous ne pouvez le rendre."

        if ident_livre not in utilisateur.emprunts:
            return f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {ident_livre} n'est pas emprunté par l'utilisateur {ident_user}. Vous ne pouvez le rendre."

        FonctionnaliteLivre(self.livres).modifier_statut(ident_livre)
        utilisateur.emprunts.remove(ident_livre)
        return f"Le livre {livre.titre} de {livre.auteur} enregistré sous l'identifiant {ident_livre} a bien été rendu."