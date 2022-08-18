from PIL import Image, ImageFilter

p = './images/pokedex/'

img = Image.open(p + 'pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save(p + "pikachu_blur.png", 'png')

print(img.format)
print(img.size)
print(img.mode)

