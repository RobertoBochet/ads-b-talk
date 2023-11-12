#!/usr/bin/env python3

import sys
from time import sleep
from threading import Thread
from argparse import ArgumentParser
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler as Handler
import webbrowser

# Default arguments
DEFAULT_ADDR = '127.0.0.1'
DEFAULT_PORT = 8080

# Command line arguments
parser = ArgumentParser(description="Serve reveal.js slides.")
parser.add_argument('port', metavar='PORT', type=int, nargs='?',
                    default=DEFAULT_PORT)
parser.add_argument('--show', action='store_true', default=False,
                    help="Open in browser.")
parser.add_argument('--no-cache', action='store_true', default=False,
                    help="Disables caching.")
arg = parser.parse_args()

# Define customizable HTTP request handler
class CustomHandler(Handler):
    def end_headers(self):
        if arg.no_cache:
            self.no_cache_headers()
        Handler.end_headers(self)

    def no_cache_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

# Define HTTPD server
class stoppable_httpd(Thread):
    def run(self):
        print(f"Serving at http://{DEFAULT_ADDR}:{arg.port} [Ctrl + C] to stop")
        self.s = TCPServer((DEFAULT_ADDR, arg.port), CustomHandler)
        self.s.serve_forever()

    def stop(self):
        print("\nShutting down...")
        self.s.shutdown()
        self.s.server_close()
        self.join()

def show():
    webbrowser.open(f"http://{DEFAULT_ADDR}:{arg.port}/")

if __name__ == '__main__':

    # Start server
    TCPServer.allow_reuse_address = True
    httpd = stoppable_httpd()
    httpd.start()

    # Open page in web browser
    if arg.show:
        show()

    try:
        while True:
            sleep(60 * 60 * 24)
    except (KeyboardInterrupt, SystemExit):
        httpd.stop()
        sys.exit(0)
