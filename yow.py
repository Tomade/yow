import random
import http.server


class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        quote = random.choice(quotes)
        self.request.sendall(quote.encode())


quotes = open('zippy').read().split('%\n')
server = http.server.HTTPServer(('', 8080), handler)
server.serve_forever()
