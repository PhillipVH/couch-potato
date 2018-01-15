import gspread

from oauth2client.service_account import ServiceAccountCredentials
from optparse import OptionParser


def authorize_and_get_sheet():
    '''
    Authorize and obtain a handle to the Google Sheet storing the
    movie data.
    :return: The sheet object representing the library
    '''
    # Use credentials to create a client to interact with the Google Drive API
    scope = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    client = gspread.authorize(credentials)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Copy of Couch Potato").sheet1

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
    movie_sheet.insert_row([options.movie_name, 0, 0, 0], 2)
    print(f"Inserted {options.movie_name}! Get to watching!")


if __name__ == "__main__":
    main()
