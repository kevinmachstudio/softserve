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

def fetch_crypto_prices():
    
    btc_price = cryptocompare.get_price('BTC', currency='USD')
    xrp_price = cryptocompare.get_price('XRP', currency='USD')
    ada_price = cryptocompare.get_price('ADA', currency='USD')
    link_price = cryptocompare.get_price('LINK', currency='USD')

    return {
        'BTC': str(btc_price['BTC']['USD']),
        'XRP': str(xrp_price['XRP']['USD']),
        'ADA': str(ada_price['ADA']['USD']),
        'LINK': str(link_price['LINK']['USD'])
    }

def create_message(data):
    msg =   '\n' + \
            '🚀🚀🚀🚀🚀🚀🚀🚀🚀🌕🌕🌕🌕🌕🌕🦍🦍🦍🦍🦍🦍🦍🦍💎💎💎💎💎💎💎' + '\n' + \
            'BTC: ' + data['BTC'] + '\n' + \
            'XRP: ' + data['XRP'] + '\n' + \
            'ADA: ' + data['ADA'] + '\n' + \
            'LINK: ' + data['LINK'] + '\n'
            # 'GME: ' + str(si.get_live_price("GME")) + ' 🚀🚀🚀🚀🚀🚀🚀🚀🚀'
    return msg

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
        
        if float(crypto['BTC']) > 50000 or float(crypto['ADA']) > 1 or float(crypto['LINK']) > 50:
            message = client.messages \
                    .create(
                        body=message_body,
                        from_='+13158733012',
                        to='+14083681318'
                    )
            
            print(message.sid)
        else:
            print('HOLD THE LINEEE')
            print(crypto)
        
            # message = 'GME ' + str(si.get_live_price("GME")) + ' 🚀🚀🚀🚀🚀🚀🚀🚀🚀'
            self.wfile.write(message_body.encode('utf-16'))
        return