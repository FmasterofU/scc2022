## Decoding:

We find a hidden message (sub-image) in the center of the engine cover. After magnification ([code](PythonPlotter.py) -> [image](RegionOfInterest.png)), we code the pixels as 1 and 0 (1 is yellow, 0 i blue), going from the left to right, and up to down. The extracted binary information is:
```
0010010001111011
0101001001000010
0101111101010011
0100001101010011
0101111101010011
0101010001000101
0100011101111101
```

We now use the [ONLINEBINARTOOLS' binary to ascii](https://onlinebinarytools.com/convert-binary-to-ascii) converter, and the data is:
```${RB_SCS_STEG}```.