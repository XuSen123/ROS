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
    
    while True:
        conn, addr = sock.accept()    
        try:
            while True:
                length = recvall(conn, 16)
                stringData = recvall(conn, int(length))
                data = numpy.fromstring(stringData, dtype = 'uint8')
                decimg = cv2.imdecode(data, 1)
                cv2.imshow('SERVER', decimg)
                if cv2.waitKey(10) == 27:
                    break;
        finally:
            sock.close()
            cv2.destroyAllWindows()
    '''
    while 1:
        length = recvall(conn, 16)
        stringData = recvall(conn, int(length))
        data = numpy.fromstring(stringData, dtype = 'uint8')
        decimg = cv2.imdecode(data, 1)
        cv2.imshow('SERVER', decimg)
        if cv2.waitKey(10) == 27:
            break;
    
    sock.close()
    cv2.destroyAllWindows()
    '''
