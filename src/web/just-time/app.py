# ref: https://www.youtube.com/watch?v=U6BzW48-D9A

import json
from http.server import HTTPServer, BaseHTTPRequestHandler

dados = { 
    "Evento" : "#FiqueEmCasaConf", 
    "Palestra" : "Python para web APIs", 
    "Palestrante" : "Bruno Rocha" 
    }

class API(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(dados).encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8000), API)
server.serve_forever()