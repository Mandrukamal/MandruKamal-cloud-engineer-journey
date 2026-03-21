from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message = b"Hello from Kamal's Docker Container!"
        self.wfile.write(message)

if __name__ == "__main__":
    print("Server starting on port 8080...")
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()