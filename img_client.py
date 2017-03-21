#!/usr/bin/env python
# coding=utf-8

import socket
import sys
import cv2
import numpy as np

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('172.17.42.1', 10000)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    
    img = cv2.imread('/home/turtlebot/Pictures/1.jpg')
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    
    while True:
        result, imgencode = cv2.imencode('.jpg', img, encode_param)
        data = np.array(imgencode)
        stringData = data.tostring()
        sock.send(str(len(stringData)).ljust(16))
        sock.send(stringData)
    sock.close()
    

    '''
    try:
        message = '0123456789'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
    '''


