"""
Simple Database Client Driver
Jack Andersen
"""

from Client import web_interface

interface = web_interface.WebInterface("localhost", 8080)

#reply_data = interface.do_request({"method": "select"})
reply_data = interface.do_request({"method":"insert", "set":{"x":10, "y":20, "class":1}})
print(reply_data)
