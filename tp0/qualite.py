"""Remise au propre d'une fonction"""
def cout_deplacement_propre(terrain, x1, y1, x2, y2):
    """Donne le cout du deplacement en fonction du deplacement et du type de terrain"""
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if terrain == "R":
        cout = dist
    elif terrain == "H":
        cout = dist * 1.5
    elif terrain == "S":
        cout = dist * 2.0
    else:
        cout = dist * 3.0
    return cout
