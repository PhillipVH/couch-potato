from filters import is_downloaded


def test_is_downloaded_false():

    movie = {'Name': 'A Movie', 'Downloaded': 0, 'Favorite': 0, 'Watched': 0}

    assert is_downloaded(movie) == False


def test_is_downloaded_true():

    movie = {'Name': 'Another Movie', 'Downloaded': 1, 'Favorite': 0, 'Watched': 0}

    assert is_downloaded(movie) == True


def test_is_downloaded_bogus():

    movie = {'Name': 'Yet Another Movie', 'Downloaded': -1, 'Favorite': 0, 'Watched': 0}

    assert is_downloaded(movie) == False



