## Method

First, we extract the pasword hash from the shadow file, and place it in a new file [hash.txt](hash.txt).
Now we use [TunnelsUp's hash analyzer](https://www.tunnelsup.com/hash-analyzer/) to determine the hash type as `SHA512-Crypt` which under the `hashcat` tool has the id `1800`. Now we runn the following `hashcat` command:
```hashcat -m 1800 -a 0 -o cracked.txt hash.txt german.txt --force```
The result is a generated file named [cracked.txt](cracked.txt) which holds the `hash`:`plain password` pair.