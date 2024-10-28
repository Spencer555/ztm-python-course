from PIL import Image, ImageFilter



img = Image.open('./images/pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
# read the  docs for more img methods 
# we use png because it supports most image filters
# (name, fileextension)
filtered_img.save("blur.png", "png")

# convert image to grey scale 
gray_scale = img.convert('L')
gray_scale.save("grey.png", 'png')
# rotate image roatate(degrees)
crooked = gray_scale.rotate(180)

crooked.save('crooked.png' , 'png')
# crooked.show()

# resize
resize = gray_scale.resize((300, 300))

resize.save('resize.png', 'png')
# resize.show()


# crop
box = (100,100,400,400)
cropped = filtered_img.crop(box)

cropped.save('cropped.png', 'png')
# cropped.show()


# show image
# gray_scale.show()

print(img.format)
print(img.size)
print(img.mode) # the coloring of the image



# reduce size of image 
astro = img = Image.open('./images/astro.jpg')
# instead of saying resize if you want to keep the aspect ratio use thumbnail
# it just modify the original it does not return a new one
# the thumbnail is usefull for profile pics it would do anything up to 400 but keeping the aspect ratio
new_astro_img = astro.thumbnail((400, 400))
astro.save('thumbanil.jpg')
print(astro.size)
astro.show()
