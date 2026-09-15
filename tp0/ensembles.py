"""Coordination d'une flotte de robot avec des ensembles"""
robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

def robots_double_mission(set_explo, set_trans) :
    """Permet de savoir quels robots peuvent faire les deux missions"""
    ret = set()
    len_explo = len(set_explo)
    len_trans = len(set_trans)
    if len_explo>=len_trans :
        for i in set_explo :
            if i in set_trans :
                ret.add(i)
    else :
        for i in set_trans :
            if i in set_explo :
                ret.add(i)
    return ret

def robots_toutes_missions(set_explo, set_trans) :
    """Permet d'avoir l'ensemble de tous les robots"""
    ret = set()
    for i in set_explo :
        ret.add(i)
    for i in set_trans :
        ret.add(i)
    return ret

def robots_exploration_seulement(set_explo, set_trans) :
    """Permet d'avoir l'ensemble des robots qui ne peuvent faire que l'exploration"""
    ret = set()
    for i in set_explo :
        if i not in set_trans :
            ret.add(i)
    return ret

double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}
