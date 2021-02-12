from http.server import BaseHTTPRequestHandler
# from cowpy import cow
from datetime import datetime

# if time is 7am



# if time is 11am

# if time is 12pm


# if time is 4pm

# if time is 7pm


def construct_message(time, message):
    msg = "Reminder: {message}"
    return msg

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        message_body = construct_message("Get dinner ready")

        self.wfile.write(message_body.encode('utf-16'))
        return