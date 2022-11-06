from PIL import Image

im = Image.open('abba.png','r')

pix_val = list(im.getdata())
print(len(pix_val))
val=[i for i in pix_val if i!=(255,255,255)]
print(len(val))
print(pix_val)


