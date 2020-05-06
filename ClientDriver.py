"""
Simple Database Client Driver
Team 3
"""

from Client import web_interface

# HTTP Connection to database server
interface = web_interface.WebInterface("localhost", 8080)

# Query for rows where the time series value == 10
reply_data = interface.do_request({"method": "select", "where": {"y":"10"}})
print(reply_data)
