## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where to start? (-16%)

Read the challenge text. Download and open the shadow file. Identify administrator user line.

2. Looking under the hood (-16%)

Understand the shadow file. What type of hash function is used? Where is the salt? Where is the hash?

3. Digging deeper (-16%)

Copy the hash into the separate file and use hashcat. Find the appropriate mode for the hash type used in the shadow file.

4. Trying something simple (-16%)

Check the challenge text and identify which could be the best password database to use in this context.

5. Going even deeper (-16%)

Utilize a brute force search with hashcat. Narrow the solution space by configuring hashcat to use the appropriate password database.

6. Complete solution (-100%)

1. Open the shadow file, find the administrator user!
2. Find the $6$ in the file - this identifies the SHA-512 password. Next thing between two $ symbols is salt, and after that is hash until the semicolon sign.
3. Copy the everything from between two ':' signs, and excluding ':' (hash code, salt and hash) and paste it into a new file e.g. `hash.txt`.
4. Find in the [hashcat documentation](https://hashcat.net/wiki/doku.php?id=hashcat) mode for `$6$` hashes - `1800`.
5. Download the password file and unpack it.
6. Run `hashcat -m 1800 hash.txt german.txt --force` and wait until it goes through the password file (around 10 minutes on an average personal computer).
7. After it cracked the password, type `hashcat -m 1800 hash.txt german.txt --force --show` find at the bottom, after the semicolon the password .
8. Read the password and submit it via the flag submission form/box.
# Lessons learned:

    -   The information contained in the shadow file on Linux systems contains information about the hash function used, salt and hash value.
    -   Brute-force password cracking can be significantly optimized by using databases of known and frequently used passwords as well as by relying on so-called rainbow tables of precomputed hash values.
    -   Hashcat is a tool for password recovery (and cracking).