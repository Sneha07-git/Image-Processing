from PIL import Image, ImageFilter

img = Image.open('C:\\Users\\acer\\PycharmProjects\\Image_Pro\\astro.jpg')

img.thumbnail((400,400))
img.save('thumbnail.jpg')
img.show()






'''
Image Cropping:

filtered_image = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_image.crop(box)
region.save("grey.png","png")
region.show()


'''
