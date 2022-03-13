from matplotlib import image

img = image.imread("C:\\Users\\igors\\Downloads\\SCS_Red Bull_SteganographyChallenge.jpg")

print( type(img) )
print( img.shape )

import matplotlib.pyplot as plt
plt.imshow(img)