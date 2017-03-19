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
    
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    
    while ret:
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        cv2.imshow('CLIENT', frame)
        data = np.array(imgencode)
        stringData = data.tostring()
        sock.send(str(len(stringData)).ljust(16))
        sock.send(stringData)
        ret, frame = capture.read()
        if cv2.waitKey(10) == 32:
            break;
    sock.close()
    print >>sys.stderr, 'connection closed!'
    cv2.destroyAllWindows()
