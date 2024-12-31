from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeTransform
from gvm.xml import pretty_print

# https://forum.greenbone.net/t/generic-web-scanning-gmp-v22-4/14840
# Auth creds
username = 'admin'
password = 'admin'

# If gvmd is provided by a package of the distribution, it should be /run/gvmd/gvmd.sock.
# If gvmd was built from source and did not set a prefix, the default path can be used by setting path = None.
# kali deploy need set /run/gvmd/gvmd.sock
path = '/run/gvmd/gvmd.sock'

# don't specific path will can not establish connection
connection = UnixSocketConnection(path=path)
transform = EtreeTransform()

with Gmp(connection=connection, transform=transform) as gmp:
    # Retrieve GMP version supported by the remote daemon
    version = gmp.get_version()

    # Prints the XML in beautiful form
    pretty_print(version)

    # Login
    gmp.authenticate('admin', 'admin')

    # Retrieve all tasks
    tasks = gmp.get_tasks()

    # Get names of tasks
    task_names = tasks.xpath('task/name/text()')   # list
    pretty_print(task_names)

