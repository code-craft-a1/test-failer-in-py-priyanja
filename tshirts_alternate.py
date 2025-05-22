def size(cms):
    if type(cms) != float and type(cms) != int:
        return "Invalid"
    if cms<30 or cms>50:
        return "Invalid" 
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms < 42:
        return 'M'
    else:
        return 'L'
