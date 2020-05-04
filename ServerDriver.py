"""
Simple Database Server Driver
Jack Andersen
"""

# Server consists of a database component and web interface component
from Server import database, web_interface

db_instance = database.Database('simple.db')


def method_handler(parameters):
    mname = parameters["method"]
    if not hasattr(db_instance, mname):
        return {"result", "invalid_method"}
    method = getattr(db_instance, mname)
    return method({k: v for k, v in parameters.items() if k != "method"})


web_instance = web_interface.WebInterface(8080, method_handler)
web_instance.serve_forever()
