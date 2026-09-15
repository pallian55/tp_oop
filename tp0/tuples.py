"""Manipulation du journal de bord d'un robot"""
releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]
assert len(releves) == 3
assert releves[0][0] == "laser_avant"

def afficher_releve(releve):
    """retourne une chaine de caractère correspondant au relevé du capteur"""
    return "Capteur"+" "+releve[0]+" : "+str(releve[1])+" "+releve[2]


assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"


