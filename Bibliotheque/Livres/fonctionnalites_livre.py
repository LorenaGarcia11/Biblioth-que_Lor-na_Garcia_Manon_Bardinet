from Livres.encodage_livre import Livre, Disponibilite, generate_livre_id

# Nous créons une classe qui contient toutes les fonctionnalités relatives aux livres.
class FonctionnaliteLivre:

    def __init__(self, livres: list[Livre]) -> None:
        self.livres = livres


    def ajouter_livre(self, titre: str, auteur: str) -> str:
        """
        On ajoute un nouveau livre à la bibliothèque, en vérifiant au préalable qu'il n'existe pas déjà.

        :param titre: Titre du livre que l'on souhaite ajouter.
        :param auteur: Auteur du livre que l'on souhaite ajouter.
        :return: Message indiquant :
        - soit que le livre est déjà présent dans la bibliothèque en rappelant son identifiant.
        - soit que le livre a bien été ajouté avec un identifiant associé.
        """
        livre_existant = next((l for l in self.livres if l.titre == titre and l.auteur == auteur), None)
        #Commande next trouvée sur internet qui crée un générateur qui parcourt self.livres et ne retient que le livre dont le titre et l’auteur correspondent s'il existe.
        if livre_existant:
            return f"Le livre {titre} de {auteur} appartient déjà à la bibliothèque sous l'identifiant {livre_existant.ident}."

        nouveau_livre = Livre(generate_livre_id(), titre=titre, auteur=auteur, statut=Disponibilite.DISPONIBLE)
        self.livres.append(nouveau_livre)
        return f"Le livre « {titre} » de {auteur} a bien été ajouté à la bibliothèque sous l'identifiant {nouveau_livre.ident}."


    def supprimer_livre(self, ident: str) -> str:
        """
        On supprime un livre à partir de son identifiant, s'il n'est pas actuellement emprunté.

        :param ident: Identifiant du livre que l'on souhaite supprimer.
        :return: Message indiquant :
        - soit que le livre a bien été supprimé,
        - soit qu'il est impossible de supprimer le livre, car il est en cours d'emprunt.
        :raises ValueError: Si aucun livre ne correspond à l'identifiant fourni.
        """
        livre = next((l for l in self.livres if l.ident == ident), None)
        if not livre:
            raise ValueError(f"Aucun livre d'identifiant {ident} n'a été trouvé dans la bibliothèque.")

        if livre.statut == Disponibilite.EMPRUNTE:
            return f"Le livre « {livre.titre} » de {livre.auteur} avec pour identifiant {ident} est en cours d'emprunt. La suppression est temporairement impossible."

        self.livres.remove(livre)
        return f"Le livre « {livre.titre} » de {livre.auteur} avec pour identifiant {ident} a été supprimé de la bibliothèque."


    def modifier_statut(self, ident: str) -> str:
        """
        On modifie le statut du livre dont l'identifiant nous est fourni.
        S'il est actuellement disponible, on le marque comme emprunté, et vice versa.

        :param ident: Identifiant du livre dont on souhaite modifier le statut.
        :return: Message confirmant le nouveau statut du livre.
        :raises ValueError : Si aucun livre ne correspond à l'identifiant fourni.
        """
        livre = next((l for l in self.livres if l.ident == ident), None)
        if not livre:
            raise ValueError(f"Aucun livre enregistré sous l'identifiant {ident}.")

        if livre.statut == Disponibilite.EMPRUNTE:
            livre.statut = Disponibilite.DISPONIBLE
            return f"Le livre « {livre.titre} » est maintenant disponible."
        else:
            livre.statut = Disponibilite.EMPRUNTE
            return f"Le livre « {livre.titre} » est maintenant emprunté."


    def liste_livre_dispo(self) -> str:
        """
        On affiche la liste de tous les livres disponibles (ie : non empruntés).

        :return: Soit
        - Un message indiquant qu'aucun livre n'est actuellement disponible
        - Une liste indiquant pour chaque livre son identifiant, son titre et son auteur.
        """
        disponible = [l for l in self.livres if l.statut == Disponibilite.DISPONIBLE]

        if disponible:
            livres_str = [f"{l.ident} - {l.titre} ({l.auteur})" for l in disponible]
            return f"Les livres actuellement disponibles sont :\n" + "\n".join(livres_str)
        else:
            return "Aucun livre n'est actuellement disponible."


    def recherche_titre(self, titre: str) -> str:
        """
        On affiche les informations du ou des livres correspondant au titre recherché.

        :param titre: Titre du ou des livres que l'on recherche
        :return: Soit :
        - Un message indiquant qu'aucun livre ne correspond au titre recherché,
        - Une liste indiquant le(s) livre(s) correspondant au titre recherché, avec leur auteur, leur identifiant
        et leur statut (disponible ou emprunté).
        """
        resultats = [l for l in self.livres if l.titre.lower() == titre.lower()]

        if not resultats:
            return f"Aucun livre trouvé avec le titre '{titre}'."

        livres_str = [f"{l.titre} par {l.auteur} (ID: {l.ident}) - {l.statut.name}" for l in resultats]
        return "\n".join(livres_str)


    def recherche_auteur(self, auteur: str) -> str:
        """
        On affiche les informations du ou des livres écrits par l'auteur recherché.

        :param auteur: Auteur du ou des livres que l'on recherche
        :return: Soit :
        - Un message indiquant qu'aucun livre de l'auteur recherché n'est présent dans la bibliothèque.
        - Une liste de résultat indiquant le(s) livre(s) de l'auteur recherché, avec leur titre, leur identifiant
        et leur statut (disponible ou emprunté)
        """
        resultats = [l for l in self.livres if l.auteur.lower() == auteur.lower()]

        if not resultats:
            return f"Aucun livre trouvé pour l'auteur '{auteur}'."

        livres_str = [f"{l.titre} par {l.auteur} (ID: {l.ident}) - {l.statut.name}" for l in resultats]
        return "\n".join(livres_str)


    def recherche_mot_cle(self, mot: str) -> str:
        """
        On affiche les informations du ou des livres contentant, dans leur titre, le mot-clé fourni.

        :param mot: Mot-clé du ou des livres que l'on recherche
        :return: Soit :
        - Un message indiquant qu'aucun livre de la bibliothèque ne contient ce mot-clé dans son titre.
        - Une liste indiquant le(s) livre(s) contenant le mot-clé fourni dans leur titre, avec leur titre, leur auteur, leur identifiant
        et leur statut (disponible ou emprunté).
        """
        resultats = [livre for livre in self.livres if mot.lower() in livre.titre.lower()]

        if not resultats:
            return f"Aucun livre trouvé contenant le mot-clé '{mot}'."

        livres_str = [f"{l.titre} par {l.auteur} (ID: {l.ident}) - {l.statut.name}" for l in resultats]
        return "\n".join(livres_str)