#!/usr/bin/env python
# coding=utf-8

import socket
import sys

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('172.17.42.1', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    # Bind the socket to the port
    sock.bind(server_address)
    
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()

        try:
            print >>sys.stderr, 'connection from', client_address
            while True:
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data
                if data:
                    print >>sys.stderr, 'sending data back to the client'
                    connection.sendall(data)
                else:
                    print >>sys.stderr, 'no data from', client_address
                    break
        finally:
            connection.close()

