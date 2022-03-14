## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where should I start? (-33%)

Prerequisite - Part 1 of this challenge should be solved first. Find all user input forms.

2. First idea (-33%)

Whenever we are presented with an upload form, one of the first things we usually check is whether or not there is a restriction on file types that can be uploaded.
If there isn't a filter applied, then we can try to upload some backend files like PHP, ASP, JSP...

3. Complete solution (-100%)

In this case, the developer didn't check the type of file that is being uploaded.

That means we can upload a PHP file:
```php
<?php
$content = file_get_contents("/var/www/user.txt");
echo $content;
?>  
```
By clicking on the picture icon or directly accessing our PHP script (http://servername/img/script.php) we have access to the server's file system and can read the user.txt file with a flag.

# Lessons learned:

    -   As usual, all user input should be checked and sanitized, especially when it comes to uploading files
    -   Developers should always check file type and MIME type of the uploaded files and deny inappropriate file types
    -   Execution of user-provided files should not be allowed