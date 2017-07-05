#!/bin/sh
#server script
case $1 in
start)
    echo "server start"
    echo $0
    # uwsgi --ini ./Muta/uwsgi.ini
    supervisord -c /devsysproj/conf/supervisord.conf
    ;;
stop)
    echo "server stop"
    sudo killall -9 uwsgi
    supervisorctl shutdown
    ps aux | grep celery | awk '{print $2}' | xargs kill -9
    ;;
restart)
    echo "server restart"
    $0 stop
    $0 start
    ;;
*)
    echo "nothing"
    ;;
esac
exit 0
