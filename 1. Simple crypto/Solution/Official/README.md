## Hints

Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where should I start? (-16%)

Read through the challenge text. Notice its claim that the data is encoded and encrypted.

2. Looking under the hood (-16%)

Notice that the text is hexadecimal. Text is often encoded with Base64, especially on the web.

3. Digging deeper (-16%)

AES and its variants are the algorithms of choice for encrypting data online. In both the encryption and decryption stages you need to define the key, initialization, and (block) mode for AES.

4. Trying something simple (-16%)

Online cyphertext analyzer tools can help identify the underlying algorithm. Online analyzers are sometimes less useful, especially if there are multiple rounds of encoding/encryption.

5. Going even deeper (-16%)

When experimenting with AES, remember that the most basic, textbook settings are: (1) key length of 16 bytes, (2) ECB mode, and (3) being lazy and making the IV the same as the key.

6. Complete solution (-100%)

This is the cyphertext:

```4e54eac041dd3cccca8c4f62ff8b4e6b59a7129cb6cbcb4621c86a83f712914d5bbbaf5550c3b47db785604acf48cb19d6f1df33cc4e90c54162ed4923fe96c6b7da24eec1141b0f12dcfd6bed302743cb0471d7b8a42837266748c5ca44a044```
    1. Open CyberChef in your web browser.
    2. Select and add to the recipe the most frequently-used encryption algorithm (AES), i.e. choose AES Decrypt and drag it to the recipe.
    3. Enter the key from the challenge text. Notice that it is of insufficient length. Duplicate it.
    4. Set the simplest AES block mode (ECB).
    5. Set the initialization vector (IV) to be the same as the key.
    6. Select and drag From Base64 to the recipe.
    7. Copy-paste the cyphertext into the Input field.
    8. Press the 'Bake' button (near the bottom of the CyberChef user interface).
    9. Identify the flag value in the plaintext: very_easy_to_find_flag
    10. Submit the flag via the flag submission form/box.
Note: The solution is the following CyberChef recipe:

```
To_Base64('A-Za-z0-9+/=')
AES_Encrypt({'option':'UTF8','string':'CHALENGECHALENGE'},{'option':'UTF8','string':'CHALENGECHALENGE'},'ECB','Raw','Hex',{'option':'Hex','string':''})
```
# Lessons learned:

Cypher Indentifier and Analyzer (https://www.boxentriq.com/code-breaking/cipher-identifier) and similar tools can help identify the encryption/encoding
CyberChef - The Cyber Swiss Army Knife (https://cyberchef.org) is an excellent online resource for experimenting with cryptographic algorithms and different encoding techniques