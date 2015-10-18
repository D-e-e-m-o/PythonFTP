#!/usr/bin/python3

import logging
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import ThrottledDTPHandler,TLS_FTPHandler
#from pyftpdlib.contrib.handlers import TLS_FTPHandler

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('ADING', '123456', '.', perm='elrwm')
    authorizer.add_user('ASUO', '123456', '.', perm='elrwm')
    authorizer.add_anonymous('.')
    dtp_handler = ThrottledDTPHandler
    dtp_handler.read_limit = 5*1024*1024 # 5Mb/s
    dtp_handler.write_limit = 5*1024*1024
    address = ('',4000)
    handler = TLS_FTPHandler
    handler.certfile = 'keycert.pem'
    handler.authorizer = authorizer
    # requires SSL for both control and data channel
    #handler.tls_control_required = True
    #handler.tls_data_required = True
    logging.basicConfig(filename='./pyftpd.log',level=logging.INFO)
    server = FTPServer(address, handler)
    server.serve_forever()

if __name__ == '__main__':
    main()
