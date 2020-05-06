"""
Simple Database Server Driver
Team 3
"""

# Server consists of a database component and web interface component
from Server import database, web_interface

# Database adapter
db_instance = database.Database('simple.db')


def method_handler(parameters):
    """
    Adapt HTTP request into database RPC
    :param parameters: JSON-format dict with "method" selecting action and additional parameters
    :return: JSON-format result
    """
    mname = parameters["method"]
    if not hasattr(db_instance, mname):
        return {"result", "invalid_method"}
    method = getattr(db_instance, mname)
    return method({k: v for k, v in parameters.items() if k != "method"})


# Serve HTTP RPC
web_instance = web_interface.WebInterface(8080, method_handler)
web_instance.serve_forever()
