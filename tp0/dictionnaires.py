"""Inventaire de pièces détachées avec des dictionnaires"""
pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(stock, modele, piece) :
    """Retourne la quantité disponible d'une pièce pour un modèle donné"""
    return stock[modele][piece]

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

def consommer_piece(stock, modele, piece, nombre) :
    """retire des pièces du stock aprés une réparation"""
    stock[modele][piece] -= nombre

def ajouter_modele(stock, modele, nb_moteurs, nb_capteurs, nb_roues) :
    """enregistre un nouveau modèle de robot avec son stock initial"""
    stock[modele] = {"moteurs" : nb_moteurs, "capteurs" : nb_capteurs, "roues" : nb_roues}

def total_pieces(stock) :
    """calcule le nombre total de pièces"""
    ret = {"moteurs" : 0, "capteurs" : 0, "roues" : 0}
    for dico in stock.values() :
        for clef, valeur in dico.items() :
            ret[clef] += valeur
    return ret

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7
ajouter_modele(pieces_stock, "ModeleC", 4, 10,16)
assert pieces_stock["ModeleC"] == \
{"moteurs": 4, "capteurs": 10, "roues": 16}
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}
