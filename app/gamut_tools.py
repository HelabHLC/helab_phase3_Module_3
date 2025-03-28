def hlc_to_lab(h, l, c):
    # Platzhalterfunktion – reale Umrechnung später einbauen
    return [l, c, h]

def is_in_gamut(lab):
    # Dummy-Gamutprüfung: alles innerhalb 0–100
    return all(0 <= v <= 100 for v in lab)