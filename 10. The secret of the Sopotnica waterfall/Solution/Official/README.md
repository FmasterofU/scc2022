## Hints
Because our challenges do not all have the same amount of hints, our deduction system is based on the % of hints used. If a challenge has 4 hints, each hint is worth 25%. If you use the complete solution, you get 0 points.

1. Where to start (-20%)

The additional content or payload can can be basically hidden in two ways: encoded into the real payload (image itself) or in the metadata.
Metadata is encoded in the images usually on a standardized way in EXIF.

2. What is EXIF Data? (-20%)

Exchangeable Image File Format (EXIF) is a standard that defines specific information related to an image or other media captured by a digital camera. It is capable of storing such important data as camera exposure, date/time the image was captured, and even GPS location.

3. Examine the EXIF data (-20%)

Lets look into the metadata.
We can do it by using some GUI image preview tools or programmatically.
Here is the example of a python script to do dump the EXIF information.
```py
from PIL import Image, ExifTags

img = Image.open("sopotnica.png")
exif_dict = img.getexif()

if exif_dict is None:
    print('Sorry, image has no exif data.')
else:
    for key, val in exif_dict.items():
        if key in ExifTags.TAGS:
            print(f'{ExifTags.TAGS[key]}:{val}')
```
If you execute the script the following will be displayed:
ResolutionUnit:2
ExifOffset:333
Make:samsung
Model:5A6D78685A33745451304E664D6A41794D6C3878587A51344F5468664C7A51794E4452664C7A49324D6A45304D7A63794E544D34587938784D4463784E4463784F4638764E4451354D58303D
Software:G960FXXSBETH1
Orientation:1
DateTime:2020:09:04 14:24:31
XResolution:72.0
YResolution:72.0

4. What is odd ? (-20%)

Beside the device and the resolution information the model data looks pretty odd.
There should be some simple string representing the name of the model of the phone.
Instead, we have some string which looks like some hexadecimal numbers.
You can use the CyberChef as the best playground.
If you paste this string into the input field, and drop a ‘From Hex’ operation to the Recipe, it will reveal the next step.
After decoding from hex, the result looks like:
ZmxhZ3tTQ0NfMjAyMl8xXzQ4OThfLzQyNDRfLzI2MjE0MzcyNTM4Xy8xMDcxNDcxOF8vNDQ5MX0=
It’s now looks again familiar. It resembles to base64…
(only these characters are used “A” to “Z”, “a” to “z”, “0” to “9”, “+” and “/”, “=” padding string is used).
If we drop a new operation to the Recipe, the flag will be revealed !!!

5. Complete solution (-100%)

```py
from PIL import Image
import piexif
import base64

im = Image.open("sopotnica.png")
exif_dict = piexif.load(im.info["exif"])

flag_h = exif_dict['0th'][272]
flag_b64 = (bytes.fromhex(flag_h.decode("ascii"))).decode("ascii")
flag = base64.b64decode(flag_b64).decode("ascii")

print(flag)
```
# Lessons learned:

    -   There are many ways how to conceal some payload in images. Even malware payload can be hidden in images.
    -   Data can be encoded in different ways, usually to avoid to detect the real (malicious) content.