## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where should I start? (-25%)

When accessing a web page a simple CMS will be displayed. The challenge is to login as an admin user so we can start posting new articles. By clicking on the login button, a login form will be presented.

2. First idea (-25%)

Try to bypass the authentication on the web. The first approach is usually testing for a SQL injection code vulnerability. SQL injection is a technique through which attackers can execute their own malicious SQL statements, generally referred to as a malicious payload. Through the malicious SQL statements, attackers can gain access to or steal information from the victim’s database, or even worse, they may be able to make changes to the database.

3. Trying something simple (-25%)

There are situations in real life when programmers just use user input and simple concatenation to make SQL query strings.
For example:

```$query="select * from users where username='". $username ."' and password='". $password ."';"```
By setting the value of $username to:

```admin';-- -```
the SQL query string becomes:

```select * from users where username='admin'; -- - and password='anythin';```
This way, we select the data where username is admin and everything else is commented out ("--").

4. Complete solution (-100%)

By entering:

```admin';-- -```
in the username field and anything in the password field, we can successfully log in.

# Lessons learned:

Code which is vulnerable to SQL injections can be very dangerous.
Developers should be aware of this and implement the appropriate techniques to avoid this vulnerability.
TL;DR Every user input should be checked and sanitized.
More on: [OWASP SQL injection prevention cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).