#!/bin/sh

cd `dirname $0`

# rc.local    # test on CentOS 7.6
echo -e 'nohup /usr/bin/python3 /opt/package/audit_file.py &' >> /etc/rc.local
chmod 755 /etc/rc.d/rc.local
systemctl enable rc-local
systemctl restart rc-local
systemctl status rc-local


echo -e 'setup completely\n'

exit