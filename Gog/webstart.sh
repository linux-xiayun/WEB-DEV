#!/bin/bash
cd /opt/WEB-DEV/
killall -9 uwsgi
uwsgi --ini /opt/WEB-DEV/Gog/uwsgi.ini
tail /opt/WEB-DEV/Gog/log/uwsgi.log
/usr/local/openresty/bin/openresty -s reload
 ps axu |egrep "uwsgi|nginx"|grep -v "grep"|sort