"""
Server-side HTTP endpoint
Team 3
Jack Andersen
"""


import http.server
import json
import os.path


class Handler(http.server.SimpleHTTPRequestHandler):
    server_version = "SimpleDatabase/1.0"

    def __init__(self, *args, **kwargs):
        directory = os.path.join(os.getcwd(), "vue_client", "dist")
        super().__init__(*args, directory=directory, **kwargs)

    def do_POST(self):
        if self.headers.get("Content-Type") != "application/json":
            self.send_error(400, None, "Content-type must be application/json")
            return

        try:
            length = int(self.headers.get("Content-Length"))
            request_data = json.loads(self.rfile.read(length))
        except Exception as e:
            self.send_error(400, None, str(e))
            return

        if "method" not in request_data:
            self.send_error(400, None, "method key not present in JSON")
            return

        try:
            response_data = self.server.method_handler(request_data)
        except Exception as e:
            self.send_error(400, None, str(e))
            return

        response_string = json.dumps(response_data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Content-Length", str(len(response_string)))
        self.end_headers()
        self.wfile.write(response_string)

    def do_OPTIONS(self):
        self.send_response(200,"ok")
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')
        self.end_headers()

class WebInterface(http.server.HTTPServer):
    def __init__(self, port: int, method_handler):
        super().__init__(('', port), Handler)
        self.method_handler = method_handler
