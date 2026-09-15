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

def recalibrer(liste_releve, capteur, valeur):
    """reconstruit la liste des relevés avec la nouvelle valeur pour le capteur concerné"""
    new_liste = []
    for i in liste_releve :
        if i[0] == capteur :
            new_tuple = (capteur,valeur,i[2])
            new_liste.append(new_tuple)
        else :
            new_liste.append(i)
    return new_liste

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3
