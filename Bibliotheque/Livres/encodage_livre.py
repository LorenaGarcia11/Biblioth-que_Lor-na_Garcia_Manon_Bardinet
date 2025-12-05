import uuid
from dataclasses import dataclass
from enum import Enum, auto


class Disponibilite(Enum) :
    DISPONIBLE = auto()
    EMPRUNTE = auto()

# Nous créons une dataclass pour gérer la structure d'un livre.
@dataclass
class Livre:
    ident:str
    titre:str
    auteur: str
    statut: Disponibilite


def generate_livre_id() -> str:
    """
    Cette fonction génère un identifiant unique de six caractères commençant par 'L', pour livre
    :return : l'identifiant créé, par exemple 'L3F9D2'
    """
    random_part = uuid.uuid4().hex[:5].upper()  # 5 caractères aléatoires
    return f"L{random_part}"
