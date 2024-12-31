#!/bin/sh

cd `dirname $0`

echo -e 'start to setup monitor_la ...\n'

mkdir /opt/devops
/bin/cp -a ./monitor_la.py /opt/devops

echo -e 'setup completely ...\n'

exit