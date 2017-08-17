import random
import http.server


class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        quote = random.choice(quotes)
        self.send_response(200)
        self.end_headers()
        self.request.sendall(quote.encode())


quotes = open('zippy').read().split('%\n')
server = http.server.HTTPServer(('', 8080), handler)
server.serve_forever()
