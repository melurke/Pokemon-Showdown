types = ["BUG", "DARK", "DRAGON", "ELECTRIC", "FAIRY", "FIGHTING", "FIRE", "FLYING", "GHOST", "GRASS", "GROUND", "ICE", "NORMAL", "POISON", "PSYCHIC", "ROCK", "STEEL", "WATER", "KRASS"]
bug = [1, 2, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 0]
dark = [1, 0.5, 1, 1, 0.5, 0.5, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2]
dragon = [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 0]
electric = [1, 1, 0.5, 0.5, 1, 1, 1, 2, 1, 0.5, 0, 1, 1, 1, 1, 1, 1, 2, 0]
fairy = [1, 2, 2, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 0.5, 1, 0]
fighting = [0.5, 2, 1, 1, 0.5, 1, 1, 0.5, 0, 1, 1, 2, 2, 0.5, 0.5, 2, 2, 1, 0]
fire = [2, 1, 0.5, 1, 1, 1, 0.5, 1, 1, 2, 1, 2, 1, 1, 1, 0.5, 2, 0.5, 2]
flying = [2, 1, 1, 0.5, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0.5, 0.5, 1, 2]
ghost = [1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 1, 2]
grass = [0.5, 1, 0.5, 1, 1, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 2, 0]
ground = [0.5, 1, 1, 2, 1, 1, 2, 0, 1, 0.5, 1, 1, 1, 2, 1, 2, 2, 1, 0]
ice = [1, 1, 2, 1, 1, 1, 0.5, 2, 1, 2, 2, 0.5, 1, 1, 1, 1, 0.5, 0.5, 0]
normal = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 1, 0]
poison = [1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2, 0.5, 1, 1, 0.5, 1, 0.5, 0, 1, 0]
psychic = [1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 0]
rock = [2, 1, 1, 1, 1, 0.5, 2, 2, 1, 1, 0.5, 2, 1, 1, 1, 1, 0.5, 1, 2]
steel = [1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0.5, 0.5, 0]
water = [1, 1, 0.5, 1, 1, 1, 2, 1, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 0.5, 0]

def damage(attack, defense, stab, type, others, move_power):
    base = (22*move_power*(attack/defense))/50 + 2

    damage = base * stab * type * others * 0.925
    min_damage = base * stab * type * others * 0.85
    max_damage = base * stab * type * others

    # others = burn, screens, effects, terrain

    return [damage, min_damage, max_damage]

def defense(damage, attack, stab, type, others, move_power):
    defense = attack/((((damage/(stab*type*others))-2)*50)/(move_power*22))
    return defense

def attack(damage, defense, stab, type, others, move_power):
    attack = defense*((((damage/(stab*type*others))-2)*50)/(move_power*22))
    return attack

def base_hp(base):
    hp = int(((2*base+31)/2)+60)
    return hp

def base_ev(base, ev):
    level = int(((2*base+31)/2)+5)
    level += ev/4
    return level

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

def lost(our_damage):
    for damage in our_damage:
        if damage < 1:
            return False
    return True

def won(damages):
    for damage in damages:
        if damage < 1:
            return False
    return True

def end_game(our_damages, enemy_damages):
    if lost(our_damages) or won(enemy_damages):
        return True
    else:
        return False

def can_do_move(used_pokemon, move):
    for pokemon in used_pokemon:
        if pokemon in move[-1]:
            return True
    return False
