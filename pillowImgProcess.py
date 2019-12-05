from PIL import Image

img=Image.open('./199 pikachu.jpg')

print(img.format)
print(img.size)
print(img.mode)
img.show()