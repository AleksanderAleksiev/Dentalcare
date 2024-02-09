

def check_for_insufficient_props(data, props):
    return not all(data.get(key) is not None for key in props)