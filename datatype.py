def is_int(value):
    try:
        value = int(value)
        return True
    except:
        return False

def is_float(value):
    try:
        value = float(value)
        return True
    except:
        return False

def is_string(value):
    try:
        value = str(value)
        return True
    except:
        return False

def is_bool(value):
    try:
        value = bool(value)
        return True
    except:
        return False

def is_list(value):
    try:
        value = list(value)
        return True
    except:
        return False

def is_tuple(value):
    try:
        value = tuple(value)
        return True
    except:
        return False

def is_dict(value):
    try:
        value = dict(value)
        return True
    except:
        return False

