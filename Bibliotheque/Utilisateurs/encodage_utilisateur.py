from dataclasses import dataclass, field
from typing import List
import uuid

# Nous créons une dataclass pour gérer la structure de l'utilisateur.
@dataclass
class Utilisateur:
    ident: str
    nom: str
    emprunts: List[str] = field(default_factory=list) #Commande trouvée sur internet, non vue en cours : on crée une nouvelle liste vide pour chaque instance de la dataclass, afin d’éviter qu’elles partagent la même liste par défaut.


def generate_utilisateur_id() -> str:
    """
    Cette fonction génère un identifiant unique de six caractères commençant par 'U', pour utilisateur
    :return : l'identifiant créé, par exemple 'U1A3F9'
    """
    random_part = uuid.uuid4().hex[:5].upper()  # 5 caractères aléatoires
    return f"U{random_part}"