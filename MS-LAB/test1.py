from PIL import Image,ImageDraw
import numpy as np
inputImage=Image.open("Lenna_(test_image).png")

width,height=inputImage.size
print("image width ",width)
print("image height ",height)

pixel_val=list(inputImage.getdata())
print(pixel_val[1])
print(len(pixel_val))
pixes=np.array(inputImage.getdata()).reshape(width,height,3)
print(pixes[2,1,0])
print(len(pixes[0]))
in_gray=inputImage.convert('L')
in_gray.show()
in_gray.save("Lena_gray.png")
for i in range(height):
    inputImage.putpixel((i,i),(0,0,0))
inputImage.show()    

txt="not really a fancy text"
imgDrawer=ImageDraw.Draw(inputImage)
imgDrawer.text((5,30),txt)
inputImage.show()
img = inputImage.convert('RGBA')
r, g, b, alpha = img.split()
selection = r.point(lambda i: i > 120 and 150)
selection.save( "COLOR_BAND_MASK.png ")
r.paste(g, None, selection)
img = Image.merge( "RGBA ", (r, g, b, alpha))
img.save( "COLOR_CHANGE_BAND.png")
img.show()