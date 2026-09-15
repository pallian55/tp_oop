"""Inventaire de pièces détachées avec des dictionnaires"""
pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(dico, modele, piece) :
    """Retourne la quantité disponible d'une pièce pour un modèle donné"""
    return dico[modele][piece]

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10
