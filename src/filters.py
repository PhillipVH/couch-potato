def is_downloaded(movie) -> bool:
    if movie['Downloaded'] == 1:
        return True
    else:
        return False
