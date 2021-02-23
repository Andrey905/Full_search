def spn_p(upp, low):
    upp_x, upp_y = upp.split(' ')
    low_x, low_y = low.split(' ')
    x = float(low_x) - float(upp_x)
    if float(low_x) - float(upp_x) < 0:
        x = (float(low_x) - float(upp_x)) * -1
    return str(x), str(float(upp_y) - float(low_y))