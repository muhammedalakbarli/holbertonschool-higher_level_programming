#!/usr/bin/python3
"""
RESTful API-nin əsaslarını öyrənmək üçün 
http.server modulu ilə qurulmuş sadə server.
"""
import http.server
import json


class HTTPHandler(http.server.BaseHTTPRequestHandler):
    """BaseHTTPRequestHandler-dən miras alan sadə handler klası"""

    def do_GET(self):
        """GET sorğularını idarə edən metod"""

        # Kök endpoint (Root)
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        # /data endpoint - JSON məlumat qaytarır
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # /status endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        # /info endpoint
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info_data).encode('utf-8'))

        # Tanınmayan endpointlər üçün 404 xətası
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # Qeyd: Testlərin keçməsi üçün bu mesaj mütləq belə olmalıdır:
            self.wfile.write("Endpoint not found".encode('utf-8'))


if __name__ == '__main__':
    """Serverin 8000 portunda işə salınması"""
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, HTTPHandler)
    print("Server http://localhost:8000 ünvanında işləyir...")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dayandırıldı.")
        httpd.server_close()
