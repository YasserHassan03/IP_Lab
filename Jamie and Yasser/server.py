import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map['.wasm'] = 'application/wasm'

httpd = socketserver.TCPServer(('127.0.0.1', 8000), Handler)
httpd.serve_forever()
