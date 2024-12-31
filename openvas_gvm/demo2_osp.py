from gvm.connections import UnixSocketConnection, DebugConnection
from gvm.protocols.gmp import Gmp
from gvm.protocols.latest import Osp
from gvm.transforms import EtreeTransform
from gvm.xml import pretty_print

# https://greenbone.github.io/python-gvm/usage.html
# write according to latest version

# Auth creds
username = 'admin'
password = 'admin'

# If gvmd is provided by a package of the distribution, it should be /run/gvmd/gvmd.sock.
# If gvmd was built from source and did not set a prefix, the default path can be used by setting path = None.
# kali deploy need set /run/gvmd/gvmd.sock
path = '/tmp/ospd-wrapper.sock'

# don't specific path will can not establish connection
connection = UnixSocketConnection(path=path)

# if need debug connection
# socketconnection = UnixSocketConnection(path=path)
# connection = DebugConnection(socketconnection)

osp = Osp(connection=connection)

# using the with statement to automatically connect and disconnect to ospd
with osp:
    # get the response message returned as a utf-8 encoded string
    response = osp.get_version()
    # print the response message
    print(response)

    response = osp.get_scans()
    # print the response message
    print(response)