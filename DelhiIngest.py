"""
Client for ingesting delhi weather data
Team 3
"""

from Client import web_interface
import csv

# HTTP Connection to database server
interface = web_interface.WebInterface("localhost", 8080)

with open('testset.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Only accept daily readings from around 12 noon
        if row["datetime_utc"][-5:-3] == "12" and row[" _dewptm"]:
            interface.do_request(
                {"method": "insert", "set": {"x": row["datetime_utc"], "y": row[" _dewptm"], "class": "Dew Point"}})
