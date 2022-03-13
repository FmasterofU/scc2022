## Decryption:

AES decryption using [JavaInUse's service](https://www.javainuse.com/aesgenerator). 

The parameters are:

Encrypted plaintext (remove spaces): ```4e54eac041dd3cccca8c4f62ff8b4e6b59a7129cb6cbcb4621c86a83f712914d5bbbaf5550c3b47db785604acf48cb19d6f1df33cc4e90c54162ed4923fe96c6b7da24eec1141b0f12dcfd6bed302743cb0471d7b8a42837266748c5ca44a044```

Input format: `HEX`

Mode: `ECB`

Key size in bits: `128`

Secret Key (repeating given key two times to get key size of 128 bits): `CHALENGECHALENGE`

The decryption results in ```VGhpcyB0ZXh0IGNvbnRhaW5zIHRoZSByZWxldmFudCBmbGFnIHZhbDogdmVyeV9lYXN5X3RvX2ZpbmRfZmxhZw==```
which is a base64 encoded string.

## Decoding:

Base64 decode using [BASE64 service](https://www.base64decode.org/).

And the result is: ```This text contains the relevant flag val: very_easy_to_find_flag```