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


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)

    # Option to add a new movie to the library
    parser.add_option("-a", "--add-movie", dest="movie_name",
                      help="Add a new movie with the given title")

    (options, args) = parser.parse_args()

    # Obtain a handle to the sheet
    movie_sheet = authorize_and_get_sheet()

    # Insert the movie into the library
    movie_sheet.insert_rows(row=1, number=1, values=[options.movie_name, 0, 0, 0])
    print(f"Inserted {options.movie_name}! Get to watching!")


if __name__ == "__main__":
    main()
