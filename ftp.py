#!/usr/bin/python3

import logging
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('ADING', '123456', '.', perm='elrwm')
    authorizer.add_user('ASUO', '123456', '.', perm='elrwm')
    authorizer.add_anonymous('.')
    handler = FTPHandler
    handler.authorizer = authorizer
    # requires SSL for both control and data channel
    #handler.tls_control_required = True
    #handler.tls_data_required = True
    address = ('',4000)
    logging.basicConfig(filename='./pyftpd.log',level=logging.INFO)
    server = FTPServer(address, handler)
    server.serve_forever()

if __name__ == '__main__':
    main()
