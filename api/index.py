from http.server import BaseHTTPRequestHandler
# from cowpy import cow
from yahoo_fin import stock_info as si

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        # message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        # self.wfile.write(message.encode())
        message = 'GME ' + str(si.get_live_price("GME")) + ' 🚀🚀🚀🚀🚀🚀🚀🚀🚀'
        self.wfile.write(message.encode())
        return