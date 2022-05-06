types = ["BUG", "DARK", "DRAGON", "ELECTRIC", "FAIRY", "FIGHTING", "FIRE", "FLYING", "GHOST", "GRASS", "GROUND", "ICE", "NORMAL", "POISON", "PSYCHIC", "ROCK", "STEEL", "WATER"]
bug = [1, 2, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1]
dark = [1, 0.5, 1, 1, 0.5, 0.5, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1]
dragon = [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1]
electric = [1, 1, 0.5, 0.5, 1, 1, 1, 2, 1, 0.5, 0, 1, 1, 1, 1, 1, 1, 2]
fairy = [1, 2, 2, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 0.5, 1]
fighting = [0.5, 2, 1, 1, 0.5, 1, 1, 0.5, 0, 1, 1, 2, 2, 0.5, 0.5, 2, 2, 1]
fire = [2, 1, 0.5, 1, 1, 1, 0.5, 1, 1, 2, 1, 2, 1, 1, 1, 0.5, 2, 0.5]
flying = [2, 1, 1, 0.5, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0.5, 0.5, 1]
ghost = [1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 1]
grass = [0.5, 1, 0.5, 1, 1, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 2]
ground = [0.5, 1, 1, 2, 1, 1, 2, 0, 1, 0.5, 1, 1, 1, 2, 1, 2, 2, 1]
ice = [1, 1, 2, 1, 1, 1, 0.5, 2, 1, 2, 2, 0.5, 1, 1, 1, 1, 0.5, 0.5]
normal = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 1]
poison = [1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2, 0.5, 1, 1, 0.5, 1, 0.5, 0, 1]
psychic = [1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1]
rock = [2, 1, 1, 1, 1, 0.5, 2, 2, 1, 1, 0.5, 2, 1, 1, 1, 1, 0.5, 1]
steel = [1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0.5, 0.5]
water = [1, 1, 0.5, 1, 1, 1, 2, 1, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 0.5]

def damage(attack, defense, stab, type, others, move_power):
    base = (22*move_power*(attack/defense))/50 + 2

    damage = base * stab * type * others * 0.925
    min_damage = base * stab * type * others * 0.85
    max_damage = base * stab * type * others

    # others = weather, critical, burn, screens, effects, terrain

    return [damage, min_damage, max_damage]

def effective(defender):
    defender_index = []

    for type in defender:
        defender_index.append(types.index(type))

    S = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for type in defender_index:
        S[0] *= bug[type]
        S[1] *= dark[type]
        S[2] *= dragon[type]
        S[3] *= electric[type]
        S[4] *= fairy[type]
        S[5] *= fighting[type]
        S[6] *= fire[type]
        S[7] *= flying[type]
        S[8] *= ghost[type]
        S[9] *= grass[type]
        S[10] *= ground[type]
        S[11] *= ice[type]
        S[12] *= normal[type]
        S[13] *= poison[type]
        S[14] *= psychic[type]
        S[15] *= rock[type]
        S[16] *= steel[type]
        S[17] *= water[type]

    super_effective = []
    very_effective = []
    effective = []
    not_effective = []
    not_not_effective = []
    immune = []

    for s in range(0, len(S)):
        if S[s] == 0:
            immune.append(types[s])
        elif S[s] == 1:
            effective.append(types[s])
        elif S[s] == 0.5:
            not_effective.append(types[s])
        elif S[s] == 0.25:
            not_not_effective.append(types[s])
        elif S[s] == 2:
            very_effective.append(types[s])
        elif S[s] == 4:
            super_effective.append(types[s])

    super_effective = list(dict.fromkeys(super_effective))
    very_effective = list(dict.fromkeys(very_effective))
    effective = list(dict.fromkeys(effective))
    not_effective = list(dict.fromkeys(not_effective))
    not_not_effective = list(dict.fromkeys(not_not_effective))
    immune = list(dict.fromkeys(immune))

    return [super_effective, very_effective, effective, not_effective, not_not_effective, immune]
