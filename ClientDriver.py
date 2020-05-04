"""
Simple Database Client Driver
Jack Andersen
"""

from Client import web_interface

interface = web_interface.WebInterface("localhost", 8080)

reply_data = interface.do_request({"method": "select"})
print(reply_data)
