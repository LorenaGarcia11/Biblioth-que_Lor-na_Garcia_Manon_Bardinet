from Utilisateurs.encodage_utilisateur import Utilisateur, generate_utilisateur_id

# Nous créons une classe qui contient toutes les fonctionnalités relatives aux utilisateurs.
class FonctionnaliteUtilisateur:

    def __init__(self, utilisateurs: list[Utilisateur]) -> None:
        self.utilisateurs = utilisateurs


    def creation_utilisateur(self, nom: str) -> str:
        """
        On crée un nouvel utilisateur, en vérifiant au préalable qu'il n'existe pas déjà.

        :param nom: Nom du nouvel utilisateur que l'on souhaite enregistrer.
        :return: Message indiquant :
         - soit que l'utilisateur est déjà enregistré,
         - soit que l'utilisateur a bien été enregistré en indiquant son identifiant.
        """
        if any(u.nom == nom for u in self.utilisateurs):
                return f"M/Mme {nom} est déjà enregistré(e)."

        nouvel_adherent = Utilisateur(generate_utilisateur_id(), nom=nom)
        self.utilisateurs.append(nouvel_adherent)
        return f"M/Mme {nom} a bien été enregistré(e) comme nouvel utilisateur. Son identifiant sera : {nouvel_adherent.ident}."


    def suppression_utilisateur(self, ident: str) -> str | None:
        """
        On supprime un utilisateur à partir de son identifiant, s'il n'a pas de livre emprunté.

        :param ident: Identifiant de l'utilisateur que l'on souhaite supprimer.
        :return: Message indiquant :
        - soit que l'utilisateur a bien été supprimé,
        - soit qu'il est impossible de supprimer l'utilisateur car il possède livres empruntés.
        :raises ValueError: Si aucun utilisateur ne correspond à l'identifiant fourni.
        """
        utilisateur = next((u for u in self.utilisateurs if u.ident == ident), None)
        #Commande next trouvée sur internet qui crée un générateur qui parcourt self.utilisateurs et ne retient que l'utilisateur dont l'identifiant correspond s'il existe.
        if not utilisateur:
            raise ValueError(f"L'utilisateur ayant l'identifiant {ident} est introuvable. Il est donc impossible de le/la supprimer.")

        if utilisateur.emprunts:
            return f"M/Mme {utilisateur.nom} a des livres empruntés, il est donc impossible de le/la supprimer."

        self.utilisateurs.remove(utilisateur)
        return f"M/Mme {utilisateur.nom} a bien été supprimé."


    def liste_utilisateurs_enregistres(self) -> str:
        """
        Retourne la liste des utilisateurs enregistrés.

        :return: Soit :
        - un message indiquant qu'aucun utilisateur n'est enregistré.
        - une liste indiquant pour chaque utilisateur son nom et son identifiant
        """
        if len(self.utilisateurs) == 0:
            return "Aucun utilisateur n'est enregistré pour le moment."

        liste_str = [f"{u.ident} - {u.nom}" for u in self.utilisateurs]
        return f"Les utilisateurs actuellement enregistrés sont :\n" + "\n".join(liste_str)