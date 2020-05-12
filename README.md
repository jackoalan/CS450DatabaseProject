# Simple Remote-Access Database for Time-series Data

Repository containing Group 3's final project code and data.

Contains three Python programs for running various aspects of the project.

## ServerDriver.py

This program hosts an HTTP service on port 8080. The root URL accepts
POST requests containing JSON-formatted database queries of the form

```
{"method": "(select|insert|update|delete)", <method-parameters>...}
```

The JSON response is

```
{"result": "(success|<exception details>)", ["rows": [<row1> ... <rowN>]]}
```

All operations are performed on the working-directory file `simple.db` within
the `simple` table. There is currently no application-provided way to
modify the table structure. The `sqlite` command-line tool or any SQLite GUI
can provide this functionality.

The server program must be running to service the following two programs.

## ClientDriver.py

This program contains a minimal example of a select statement with value
filtering. It will dump all rows from the database where y == 10.

## DelhiIngest.py

This program is used to bootstrap the database with Delhi dewpoint data
contained in `testset.csv`. 

## Delhi Data Source

The CSV is directly obtained from Kaggle:

https://www.kaggle.com/mahirkukreja/delhi-weather-data