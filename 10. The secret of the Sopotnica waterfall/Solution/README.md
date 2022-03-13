## Decoding:

We take a look at the EXIF record ([EXIFER service](https://www.thexifer.net/)), in the field "Model" there is a HEX string:
```5A6D78685A33745451304E664D6A41794D6C3878587A51344F5468664C7A51794E4452664C7A49324D6A45304D7A63794E544D34587938784D4463784E4463784F4638764E4451354D58303D```.

When we decode that hex stream into ascii charaters ([ONLINEHEXTOOLS hex to ascii](https://onlinehextools.com/convert-hex-to-ascii)), we get the following Base64 encoded data:
```ZmxhZ3tTQ0NfMjAyMl8xXzQ4OThfLzQyNDRfLzI2MjE0MzcyNTM4Xy8xMDcxNDcxOF8vNDQ5MX0=```

Finally, we decode the Base64 string to actual data using [BASE64](https://www.base64decode.org/) and get:
```flag{SCC_2022_1_4898_/4244_/26214372538_/10714718_/4491}```