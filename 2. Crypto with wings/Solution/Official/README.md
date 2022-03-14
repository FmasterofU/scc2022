## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where should I start? (-16%)

Read through the challenge text. Notice its claim that the data is encoded or encrypted.

2. Looking under the hood (-16%)

Note that the given text consists of hexadecimal codes preceded by a `0` and closed by an `h`. This is not really encryption, but rather encoding. In fact, the only uppercase letters are `H` and `X`, leading to `HX`, which could make one think about Hexa...

3. Digging deeper (-16%)

Also notice that the hexadecimal values fall roughly in the `020h` to `080h` range (`32` to `128`). Remove the appended characters, `0` and `h`, from every character group to translate the cyphertext block into plain HEXA code.

4. Trying something simple (-16%)

Open **CyberChef** and experiment with From Hex to find the values of the first few characters.

5. Going even deeper (-16%)

Decode all characters one-by-one or by writing Python (or other) code.

6. Complete solution (-100%)

This is the cyphertext:

```052h 065h 064h 020h 042h 075h 06Ch 06Ch 020h 067h 069h 076h 065h 073h 020h 079h 06Fh 075h 020h 077h 069h 069h 069h 06Eh 067h 073h 020h 024h 07Bh 052h 042h 043h 052h 059h 050h 054h 04Fh 043h 048h 041h 04Ch 04Ch 045h 04Eh 047h 045 05Fh 034h 05Fh 053 043h 053h 032h 030h 032h 032h 07Dh```
1. Open CyberChef in your web browser.
2. Select and add From Hex to the recipe.
3. Decode the hexadecimal codes one-by-one.
4. Identify the flag value in the plaintext.
5. Submit the flag via the flag submission form/box.
# Lessons learned:

    -   [CyberChef - The Cyber Swiss Army Knife](https://cyberchef.org/) is an excellent online resource for experimenting with cryptographic algorithms and different encoding techniques
    -   Xynthia is a butterfly
    -   What HEXA is and how it works
    -   Translating HEXA to ASCII with a table or with a script
    -   Red Bull gives you wiiings!