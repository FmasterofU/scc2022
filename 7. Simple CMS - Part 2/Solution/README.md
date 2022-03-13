## Method

The site is a PHP based application. As an admin user we can add posts, and a post can have a image in itself. All submited files are stored in the `./img/` directory, and there is no check on file type of the submitted file. Therefore, we submit [simple-backdoor](simple-backdoor.php) webshell. Now we can execute shell commands and search for the `user.txt`.
After some searching, we find the flag on the following url:
```https://6b5c2d7659c636b2b7649090795f7894477126e1.next.avatao-challenge.com/img/user.php?cmd=cat%20../../user.txt```
The flag (file content) is: `FLAG{DZIVI:9836478987-USER}`