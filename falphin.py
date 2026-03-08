def evolve_falphin(completed):

    if completed == 0:
        return "sad"
    elif completed <= 2:
        return "egg"
    elif completed <= 4:
        return "baby"
    elif completed <= 6:
        return "winged"
    else:
        return "legendary"