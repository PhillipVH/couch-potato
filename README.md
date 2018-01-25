# Couch Potato
An attempt at a simple movie library management tool, backed by Google Sheets.

## Getting Started
This project uses [pipenv](https://github.com/pypa/pipenv) to manage its dependencies. You will need to
obtain a `client_secret.json` file and place it in the root of the project directory. Steps
are outlined [here](https://github.com/nithinmurali/pygsheets) under "Basic Usage".

```bash
git clone https://github.com/PhillipVH/couch-potato.git && cd $_
pipenv install
pipenv shell
python src/couch_potato.py --help
```

