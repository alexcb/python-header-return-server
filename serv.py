#!/usr/bin/python3
import http.server
import copy
import datetime
import email.utils
import html
import http.client
import io
import mimetypes
import os
import posixpath
import select
import shutil
import socket # For gethostbyaddr()
import socketserver
import sys
import time
import urllib.parse
from functools import partial

from http import HTTPStatus

PORT = 8088

class Handler(http.server.BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.directory = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../')
        super().__init__(*args, **kwargs)

    def do_GET(self):
        """Serve a GET request."""

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", 'text/plain; charset=UTF-8')
        self.end_headers()

        body = '\n'.join(f'{k}: {v}' for k,v in self.headers.items()) + '\n'
        self.wfile.write(body.encode('utf8'))

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
