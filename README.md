# fyle-project

Application is hosted on heroku and can be accessed here,
https://fyle-bank-data.herokuapp.com/

List of endpoints:

1: Auto complete search on bank branch innformations

URL: https://fyle-bank-data.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=10&offset=0

2: API to perform search operation on bank branches from database

URL: https://fyle-bank-data.herokuapp.com/api/branches?q=Bangalore&limit=4&offset=0

The shell script to test the above mentioned endpoints can be found under root directory, `test-script.sh`

Command to run: `sh test-script.sh`

