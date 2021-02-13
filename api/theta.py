from http.server import BaseHTTPRequestHandler
# from cowpy import cow
from datetime import datetime
# from yahoo_fin import stock_info as si
from twilio.rest import Client
import cryptocompare
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def create_message(data):
    # msg =   '\n' + \
            
            # 'GME: ' + str(si.get_live_price("GME")) + ' 🚀🚀🚀🚀🚀🚀🚀🚀🚀'
    # return msg
    pass

def over_threshold(crypto):
    pass

def under_threshold(crypto):
    pass

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        crypto = fetch_crypto_prices()

        message_body = create_message(crypto)

        # self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
        # message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        # self.wfile.write(message.encode())
        
        send_message = False
        
        if over_threshold(crypto):
            send_message = True            
        else:
            print('HOLD THE LINEEE')
            print(crypto)
            
        if under_threshold(crypto):
            send_message = True
        else:
            print('TIME TO BUYYYYYY')
            print(crypto)
        
        if send_message:
            message = client.messages \
                    .create(
                        body=message_body,
                        from_='+13158733012',
                        to='+14083681318'
                    )
            print(message.sid)
    
        # message = 'GME ' + str(si.get_live_price("GME")) + ' 🚀🚀🚀🚀🚀🚀🚀🚀🚀'
        self.wfile.write(message_body.encode('utf-16'))
        return