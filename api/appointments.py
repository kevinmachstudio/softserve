from http.server import BaseHTTPRequestHandler
from datetime import datetime

def is_time_to_pay_rent():
    today = datetime.now()
    
    # check for 1st day of the month
    if today.day == 1:
        return True
    
    return False

def is_time_to_pay_cc():
    today = datetime.now()
    
    # check for 25th day of the month
    if today.day == 25:
        return True
    
    return False

def construct_message(time, message):
    msg = "Reminder: {message}"
    return msg

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        message_body = ""

        if is_time_to_pay_rent():
            message_body += "\n Time to pay rent!!\n"

        if is_time_to_pay_cc():
            message_body += "\n Time to pay off credit cards!!\n"
        
        if message_body != "":
            message = client.messages \
                .create(
                    body=message_body,
                    from_='+13158733012',
                    to='+14083681318'
                )
            print(message.sid)
        
        # call google calendar API

        # message_body = construct_message("Get dinner ready")
        
        self.wfile.write(message_body.encode('utf-16'))
        return