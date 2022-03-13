# Task: Secrets on the wire - Part 2
Points: `150`
Tags:
  - Challenge
  - Log Analysis
  - Network Security

Difficulty: `Medium`

Length: `19 mins`

## Description and resources

### Mission brief
You received a packet capture that contains an FTP transfer of a secret file. The secret file is password protected. You need to extract meaningful information from the file.

### Instructions
You know that the password of the secret file is obtained by encrypting the secret file's name (without dot and file extension) using the Vigenere cypher and using this same file name as the password. Your final goal is to find the flag in the secret file.