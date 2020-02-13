
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user('user','12345',"/Users/xueatian", perm="elradfmw")
authorizer.add_anonymous("/Users/xueatian", perm="elradfmw")


handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1",1040), handler)
server.serve_forever()

