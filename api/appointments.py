from http.server import BaseHTTPRequestHandler
from datetime import datetime

def construct_message(time, message):
    msg = "Reminder: {message}"
    return msg



class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        # call google calendar API

        # message_body = construct_message("Get dinner ready")
        
        # self.wfile.write(message_body.encode('utf-16'))
        return