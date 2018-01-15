import random

import pygsheets

from optparse import OptionParser


def authorize_and_get_sheet():
    '''
    Authorize and obtain a handle to the Google Sheet storing the
    movie data.
    :return: The sheet object representing the library
    '''

    # This line prints out your service email. This is caused by
    # code in the 1.1.3 release of pygsheets and a pull request
    # has already been merged that changes this behavior.
    # TODO Update to 1.1.4 of pygsheets when it gets released
    gc = pygsheets.authorize(service_file="client_secret.json")

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = gc.open("Copy of Couch Potato").sheet1

    # Return the sheet object to the caller
    return sheet


def get_entire_library():
    # Obtain a handle to the sheet
    movie_sheet = authorize_and_get_sheet()

    # Return all rows except the first "header" row
    return movie_sheet.get_all_values(returnas="matrix")[1:]


def add_movie_callback(option, opt, value, parser):
    # Obtain a handle to the sheet
    movie_sheet = authorize_and_get_sheet()

    # Insert the movie into the library
    movie_sheet.insert_rows(row=1, number=1, values=[value, 0, 0, 0])

    print(f"Inserted \"{value}\"! Get to watching!")


def get_random_movie_callback(option, opt, value, parser):
    print("Random movie, coming right up!")

    # Grab the library
    library = get_entire_library()

    # Sample a random movie...
    random_index = random.randint(0, len(library) - 1)

    print(f"How do you feel about \"{library[random_index][0]}\"?")


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)

    # Option to add a new movie to the library
    parser.add_option("-a", "--add-movie",
                      action="callback",
                      callback=add_movie_callback,
                      type="str", nargs=1, dest="movie_name",
                      help="Add a new movie with the given title")

    # Option to select a random movie from the library
    parser.add_option("-r", "--random",
                      action="callback",
                      callback=get_random_movie_callback,
                      help="Selects a random movie")

    (options, args) = parser.parse_args()


if __name__ == "__main__":
    main()
