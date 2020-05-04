import http.client
import json


class WebInterface(http.client.HTTPConnection):
    def do_request(self, data):
        self.connect()
        self.request("POST", "/", json.dumps(data).encode(), {"Content-Type": "application/json"})
        response = self.getresponse()
        if response.getcode() != 200:
            raise RuntimeError(f"Error {response.getcode()}: {response.read().decode()}")
        content_type = response.getheader("Content-Type")
        if content_type != "application/json":
            raise RuntimeError(f"Reply content {content_type}, expected application/json")
        reply = json.load(response)
        response.close()
        return reply
