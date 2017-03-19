#!/usr/bin/env python
# coding=utf-8

import socket
import numpy
import sys
import cv2

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: 
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('172.17.42.1', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    # Bind the socket to the port
    sock.bind(server_address)
    
    # Listen for incoming connections
    sock.listen(1)
    conn, addr = sock.accept()    

    while 1:
        length = recvall(conn, 16)
        stringData = recvall(conn, int(length))
        data = numpy.fromstring(stringData, dtype = 'uint8')
        decimg = cv2.imdecode(data, 1)
        cv2.imshow('server', decimg)
        cv2.waitKey(5);
    
    socket.close()
    
    '''
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
                    print >>sys.stderr, 'Received data successfully'
                else:
                    print >>sys.stderr, 'no data from', client_address
                    break
        finally:
            connection.close()
    '''
